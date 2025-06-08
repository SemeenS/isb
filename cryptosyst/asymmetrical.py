from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.hazmat.backends import default_backend


class Asymmetric:
    @staticmethod
    def asymmetrical_keygen() -> tuple:
        """
        generates a pair of RSA-keys(private and public)
        :return: tuple of private and public RSA-keys
        """
        private_key = rsa.generate_private_key(
            public_exponent=65537, key_size=2048, backend=default_backend()
        )
        public_key = private_key.public_key()
        return private_key, public_key

    @staticmethod
    def symmetrical_key_encryptor(
        symmetric_key: bytes, public_key: rsa.RSAPublicKey
    ) -> bytes:
        """
        encrypts symmetric key with public RSA-key
        :param symmetric_key: symmetric key for encryption
        :param public_key: public RSA-key
        :return: encrypted symmetric key
        """
        ciphertext = public_key.encrypt(
            symmetric_key,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None,
            ),
        )
        return ciphertext

    @staticmethod
    def symmetrical_key_decryptor(
        ciphertext: bytes, private_key: rsa.RSAPrivateKey
    ) -> bytes:
        """
        decrypts symmetric key with private RSA-key
        :param ciphertext: encrypted symmetric key
        :param private_key: private RSA-key
        :return: decrypted symmetric key
        """
        symmetric_key = private_key.decrypt(
            ciphertext,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None,
            ),
        )
        return symmetric_key
