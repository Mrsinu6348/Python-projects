def encrypt(message, shift):
    encrypted_message = ""

    for char in message:
        # Encrypt uppercase letters
        if char.isupper():
            encrypted_char = chr((ord(char) + shift - 65) % 26 + 65)
            encrypted_message += encrypted_char
        # Encrypt lowercase letters
        elif char.islower():
            encrypted_char = chr((ord(char) + shift - 97) % 26 + 97)
            encrypted_message += encrypted_char
        # Preserve non-alphabetic characters
        else:
            encrypted_message += char

    return encrypted_message

def decrypt(encrypted_message, shift):
    # Decryption is simply encryption with negative shift
    return encrypt(encrypted_message, -shift)

def main():
    message = "Hello, World!"
    shift = 3

    encrypted_message = encrypt(message, shift)
    print("sudhanshu: Encrypted message:", encrypted_message)

    decrypted_message = decrypt(encrypted_message, shift)
    print("Decrypted message:", decrypted_message)

if __name__ == "__main__":
    main()
