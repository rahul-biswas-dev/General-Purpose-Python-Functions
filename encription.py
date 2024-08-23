# Define the original alphabet and the corresponding encryption characters
alphabet = "abcdefghijklmnopqrstuvwxyz"
encryption_chars = "!@#$%^&*()_+=-`~.,<>/?'[;:"

# Create the encoding and decoding translation tables
encoding_table = str.maketrans(alphabet, encryption_chars)
decoding_table = str.maketrans(encryption_chars, alphabet)


def encode_message(message):
    return message.lower().translate(encoding_table)


def decode_message(encoded_message):
    return encoded_message.translate(decoding_table)


# Ask for text to encrypt
original_message = input("Enter a message to encode: ")
encoded = encode_message(original_message)
print("Encoded message:", encoded)

# Ask for encrypted text to decrypt
encoded_input = input("Enter an encoded message to decode: ")
decoded = decode_message(encoded_input)
print("Decoded message:", decoded)
