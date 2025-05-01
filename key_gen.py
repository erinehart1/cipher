# key_gen.py
import base64

def generate_key(passphrase):
    # Check if the passphrase matches the decoded Base64 string
    try:
        decoded_passphrase = base64.b64decode(passphrase).decode('utf-8')
    except Exception as e:
        print(f"Error: {e}")
        return

    # Check if the decoded passphrase is exactly "Hello, World!"
    if decoded_passphrase != "Hello, World!":
        print("Error: Passphrase is incorrect.")
        return

    # Generate the Caesar cipher offset based on "Hello, World!"
    # We ignore spaces and punctuation to count only the letters
    clean_passphrase = ''.join(c for c in decoded_passphrase if c.isalpha())  # Remove non-alphabetic characters
    offset = len(clean_passphrase)  # Use the length as the Caesar cipher offset (which is 10 for "HelloWorld")
    
    # Apply Caesar cipher shift of 5
    final_offset = offset + 5  # Add the offset of 5

    print("Hail, Caesar! Here's your key: " + str(final_offset))  # Output the key

# If you want the logic to run when this file is executed directly
if __name__ == "__main__":
    # Passphrase riddle
    print('Riddle: How do you say SGVsbG8sIFdvcmxkIQ== in English?')

    # User enters the passphrase (Base64 encoded string)
    passphrase = input("Enter the passphrase: ")

    # Generate key and handle the print directly
    generate_key(passphrase)