from cryptosyst.work_with_files import *
from cryptosyst.serialization import *
from cryptosyst.asymmetrical import Asymmetric
from cryptosyst.symmetrical import Symmetric
import os


class Cryptosys:
    def __init__(self, settings_path="settings.json"):
        self._settings = open_json_file(settings_path)
        self._key_size = None
        self._keys_generated = False
        self._text_encrypted = False

    def set_key_size(self, size: int) -> None:
        if size not in (128, 192, 256):
            raise ValueError("Key size must be 128, 192 or 256 bits")
        self._key_size = size

    def generate_keys(self) -> None:
        if self._key_size is None:
            raise ValueError("First set key size using set_key_size()")

        private_key, public_key = Asymmetric.asymmetrical_keygen()
        symmetric_key = Symmetric.generate_key(self._key_size)

        serialization_public_key(self._settings["public_key"], public_key)
        serialization_private_key(self._settings["private_key"], private_key)
        encrypted_sym_key = Asymmetric.symmetrical_key_encryptor(
            symmetric_key, public_key
        )
        bytes_file_save(self._settings["encrypt_symmetric_key"], encrypted_sym_key)

        self._keys_generated = True
        self._text_encrypted = False

    def encrypt_text(self) -> None:
        if not self._keys_generated:
            raise ValueError("First generate keys using generate_keys()")

        text = open_txt_file(self._settings["text"])
        private_key = deserialization_private_key(self._settings["private_key"])
        encrypted_sym_key = bytes_file_read(self._settings["encrypt_symmetric_key"])

        symmetric_key = Asymmetric.symmetrical_key_decryptor(
            encrypted_sym_key, private_key
        )
        ciphertext = Symmetric.encrypt(text.encode("utf-8"), symmetric_key)
        bytes_file_save(self._settings["encrypted_text"], ciphertext)
        self._text_encrypted = True

    def decrypt_text(self) -> None:
        if not self._keys_generated:
            raise ValueError("First generate keys using generate_keys()")
        if not os.path.exists(self._settings["encrypted_text"]):
            raise ValueError("First encrypt text using encrypt_text()")

        ciphertext = bytes_file_read(self._settings["encrypted_text"])
        private_key = deserialization_private_key(self._settings["private_key"])
        encrypted_sym_key = bytes_file_read(self._settings["encrypt_symmetric_key"])

        symmetric_key = Asymmetric.symmetrical_key_decryptor(
            encrypted_sym_key, private_key
        )
        plaintext = Symmetric.decrypt(ciphertext, symmetric_key)
        save_txt_file(self._settings["decrypted_text"], plaintext.decode("utf-8"))
        self._text_encrypted = False
