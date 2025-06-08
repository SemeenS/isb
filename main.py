import sys
from crypt_system import Cryptosys


def show_menu():
    print("\nCryptosystem Menu")
    print("1. Set AES key size (128/192/256)")
    print("2. Generate keys")
    print("3. Encrypt text file")
    print("4. Decrypt text file")
    print("5. Exit")


def main():
    global crypto
    crypto = Cryptosys()

    while True:
        show_menu()
        choice = input("Choose option (1-5): ").strip()

        try:
            if choice == "1":
                size = int(input("Enter key size (128, 192 or 256): "))
                crypto.set_key_size(size)
                print(f"Key size set to {size} bits")

            elif choice == "2":
                if crypto._key_size is None:
                    print("Error: You must set key size first!")
                    continue
                crypto.generate_keys()
                print("Keys generated successfully")

            elif choice == "3":
                if not crypto._keys_generated:
                    print("Error: You must generate keys first!")
                    continue
                crypto.encrypt_text()
                print("Text encrypted successfully")
                print(f"Encrypted file: {crypto._settings['encrypted_text']}")

            elif choice == "4":
                if not crypto._keys_generated:
                    print("Error: You must generate keys first!")
                    continue
                crypto.decrypt_text()
                print("Text decrypted successfully")

            elif choice == "5":
                print("Exiting...")
                sys.exit(0)

            else:
                print("Invalid choice, please try again")

        except ValueError as e:
            print(f"Value Error: {str(e)}")
        except Exception as e:
            print(f"Unexpected Error: {str(e)}")


if __name__ == "__main__":
    main()
