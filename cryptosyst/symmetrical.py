from cryptography.hazmat.primitives import padding as sym_padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os


class Symmetric:
    @staticmethod
    def generate_key(key_size: int) -> bytes:
        """
        Generates an AES key of specified length
        :param key_size: Key length in bits (128, 192, or 256)
        :return: Generated key
        :raises ValueError: For invalid key sizes
        """
        valid_sizes = {128: 16, 192: 24, 256: 32}
        if key_size not in valid_sizes:
            raise ValueError("Key size must be 128, 192, or 256 bits")
        return os.urandom(valid_sizes[key_size])

    @staticmethod
    def apply_padding(data: bytes) -> bytes:
        """
        Applies PKCS7 padding for AES block cipher
        :param data: Input data to pad
        :return: Padded data
        """
        padder = sym_padding.PKCS7(128).padder()
        return padder.update(data) + padder.finalize()

    @staticmethod
    def remove_padding(data: bytes) -> bytes:
        """
        Removes PKCS7 padding
        :param data: Padded data
        :return: Original unpadded data
        """
        unpadder = sym_padding.PKCS7(128).unpadder()
        return unpadder.update(data) + unpadder.finalize()

    @staticmethod
    def encrypt(plaintext: bytes, key: bytes) -> bytes:
        """
        Encrypts data using AES-CBC
        :param plaintext: Data to encrypt
        :param key: Encryption key (16/24/32 bytes for 128/192/256-bit AES)
        :return: IV (16 bytes) + ciphertext
        :raises ValueError: For invalid key lengths
        """
        valid_lengths = {16: 128, 24: 192, 32: 256}
        if len(key) not in valid_lengths:
            raise ValueError(
                "Key must be 16, 24, or 32 bytes (for 128/192/256-bit AES)"
            )

        iv = os.urandom(16)
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
        encryptor = cipher.encryptor()
        padded_data = Symmetric.apply_padding(plaintext)
        return iv + encryptor.update(padded_data) + encryptor.finalize()

    @staticmethod
    def decrypt(ciphertext: bytes, key: bytes) -> bytes:
        """
        Decrypts AES-CBC encrypted data
        :param ciphertext: IV (16 bytes) + encrypted data
        :param key: Decryption key (same as encryption key)
        :return: Original plaintext
        :raises ValueError: For invalid key lengths or malformed input
        """
        if len(key) not in {16, 24, 32}:
            raise ValueError(
                "Key must be 16, 24, or 32 bytes (for 128/192/256-bit AES)"
            )
        if len(ciphertext) < 16:
            raise ValueError("Ciphertext too short to contain IV")

        iv = ciphertext[:16]
        encrypted_data = ciphertext[16:]
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
        decryptor = cipher.decryptor()
        padded_plaintext = decryptor.update(encrypted_data) + decryptor.finalize()
        return Symmetric.remove_padding(padded_plaintext)
