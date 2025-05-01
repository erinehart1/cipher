from key_gen import generate_key

# Passphrase riddle
print('Riddle: How do you say SGVsbG8sIFdvcmxkIQ== in English?')

passphrase = input("Enter the passphrase: ")

# Check if the passphrase is correct and generate the key (offset)
generate_key(passphrase)
