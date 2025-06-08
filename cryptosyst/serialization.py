from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.serialization import (
    load_pem_public_key,
    load_pem_private_key,
)


def serialization_public_key(path: str, public_key: rsa.RSAPublicKey) -> None:
    """
    serializes public RSA-key and saves it to a file in PEM

    :param path: path to file
    :param public_key: public RSA-key
    :return: None
    """
    try:
        with open(path, "wb") as file:
            file.write(
                public_key.public_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PublicFormat.SubjectPublicKeyInfo,
                )
            )
    except Exception as e:
        raise Exception(f"Error with serialization public key: {e}")


def serialization_private_key(path: str, private_key: rsa.RSAPrivateKey) -> None:
    """
    serializes private RSA-key and saves it to a file in PEM without encryption

    :param path: path to file
    :param private_key: private RSA-key
    :return: None
    """
    try:
        with open(path, "wb") as file:
            file.write(
                private_key.private_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PrivateFormat.TraditionalOpenSSL,
                    encryption_algorithm=serialization.NoEncryption(),
                )
            )
    except Exception as e:
        raise Exception(f"Error with serialization private key: {e}")


def serialization_symmetrical(path: str, symmetrical_key: bytes) -> None:
    """
    saves symmetric key to a file in bytes

    :param path: path to file
    :param symmetrical_key: symmetric key
    :return: None
    """
    try:
        with open(path, "wb") as file:
            file.write(symmetrical_key)
    except Exception as e:
        raise Exception(f"Error with serialization symmetric key: {e}")


def deserialization_public_key(path: str) -> rsa.RSAPublicKey:
    """
    deserializes public RSA-key from file in PEM

    :param path: path to file
    :return: public RSA-key
    """
    try:
        with open(path, "rb") as file:
            public_bytes = file.read()
            d_public_key = load_pem_public_key(public_bytes)
            return d_public_key
    except Exception as e:
        raise Exception(f"Error with deserialization public key: {e}")


def deserialization_private_key(path: str) -> rsa.RSAPrivateKey:
    """
    deserializes private RSA-key from file in PEM

    :param path: path to file
    :return: private RSA-key
    """
    try:
        with open(path, "rb") as file:
            public_bytes = file.read()
            d_public_key = load_pem_private_key(public_bytes, password=None)
            return d_public_key
    except Exception as exc:
        raise Exception(f"Error with deserialization private key: {exc}")


def deserialization_symmetrical(path: str) -> bytes:
    """
    deserializes symmetric key

    :param path: path to file
    :return: symmetric key
    """
    try:
        with open(path, "rb") as file:
            return file.read()
    except Exception as e:
        raise Exception(f"Error with deserialization symmetric key: {e}")
