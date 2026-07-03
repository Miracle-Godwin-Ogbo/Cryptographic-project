# ==================================================
# Cryptographic
# DecodeLabs Internship - Week 2 Project
#
# Developed by: Miracle Godwin Ogbo
#
# Requirements:
# Encrypt user text using a basic
# Caesar Cipher logic
# Decrypt the encrypted text
# Display both encrypted and decrypted output
#
# ==================================================

# ============================
# USER INPUT
# ============================

plaintext = input("Type your Message: ")
key = int(input("Enter your key: "))

ciphertext = ""

# ============================
# ENCRYPTION
# ============================

for character in plaintext:

    if character.isupper():
        current_letter = ord(character) - ord("A")
        convert_value = (current_letter + key) % 26
        encrypted_message = chr(convert_value + ord("A"))

    elif character.islower():
        current_letter = ord(character) - ord("a")
        convert_value = (current_letter + key) % 26
        encrypted_message = chr(convert_value + ord("a"))

    else:
        encrypted_message = character

    ciphertext += encrypted_message

print("\n==============================")
print("Encrypted Message")
print("==============================")
print(ciphertext)

# ============================
# DECRYPTION
# ============================

receiver_key = int(input("\nEnter key to decrypt: "))

if receiver_key == key:

    decrypted_text = ""

    for character in ciphertext:

        if character.isupper():
            current_letter = ord(character) - ord("A")
            convert_value = (current_letter - receiver_key) % 26
            decrypted_message = chr(convert_value + ord("A"))

        elif character.islower():
            current_letter = ord(character) - ord("a")
            convert_value = (current_letter - receiver_key) % 26
            decrypted_message = chr(convert_value + ord("a"))

        else:
            decrypted_message = character

        decrypted_text += decrypted_message

    print("\n==============================")
    print("Decrypted Message")
    print("==============================")
    print(decrypted_text)

else:
    print("\nWrong key! Decryption failed.")