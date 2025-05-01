# key_gen.py
import base64

def generate_key(passphrase):
    # Check if the passphrase matches the decoded Base64 string
    try:
        decoded_passphrase = base64.b64decode(passphrase).decode('utf-8')
    except Exception as e:
        return f"Error: {e}"

    # Check if the decoded passphrase is exactly "Hello, World!"
    if decoded_passphrase != "Hello, World!":
        return "Error: Passphrase is incorrect."

    # Generate the Caesar cipher offset based on "Hello, World!"
    # We ignore spaces and punctuation to count only the letters
    clean_passphrase = ''.join(c for c in decoded_passphrase if c.isalpha())  # Remove non-alphabetic characters
    offset = len(clean_passphrase)  # Use the length as the Caesar cipher offset (which is 10 for "HelloWorld")
    
    # Apply Caesar cipher shift of 5
    final_offset = offset + 5  # Add the offset of 5

    return str(final_offset)  # Return the offset as a string (this will be the 'key')
