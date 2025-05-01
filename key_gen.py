# key_gen.py
import base64

# Function to generate a Caesar cipher (encoding) with a given offset
def caesar_cipher(message, offset):
    encoded_message = ""
    for char in message:
        if char.isalpha():
            # Shift the character by the offset
            start = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - start + offset) % 26 + start)
            encoded_message += new_char
        else:
            encoded_message += char  # Non-alphabetic characters remain unchanged
    return encoded_message

# Function to generate the key and print the encrypted message
def generate_key(passphrase):
    # Check if the passphrase matches "Hello, World!"
    if passphrase != "Hello, World!":
        print("Error: Passphrase is incorrect.")
        return

    # Generate the Caesar cipher offset based on "Hello, World!"
    # We ignore spaces and punctuation to count only the letters
    clean_passphrase = ''.join(c for c in passphrase if c.isalpha())  # Remove non-alphabetic characters
    offset = len(clean_passphrase)  # Use the length as the Caesar cipher offset (which is 10 for "HelloWorld")
    
    # Apply Caesar cipher shift of 5
    final_offset = offset + 5  # Add the offset of 5

    print("\n\nHail, Caesar! Here's your key: " + str(final_offset))  # Output the key

    # Now, let's encrypt the predefined message with the generated key
    message = """Hey, dude. I'd like your help on drawing the boundary lines around what my team can/should be agreeing to deliver in light of the squishy asks coming from the top. I would like to avoid the situation where my team falls on the sword of not delivering a "deliverable" that leadership could never define and needs a scapegoat for."""
    
    encrypted_message = caesar_cipher(message, final_offset)
    print("\nAnd here's you encrypted essage:")
    print(encrypted_message)
    print("\n\nHAVE FUN!\n\n")

# If you want the logic to run when this file is executed directly
if __name__ == "__main__":
    # Passphrase riddle
    print('Riddle: How do you say SGVsbG8sIFdvcmxkIQ== in English?')

    # User enters the passphrase (should be "Hello, World!")
    passphrase = input("Enter the passphrase: ")

    # Generate key and handle the print directly
    generate_key(passphrase)
