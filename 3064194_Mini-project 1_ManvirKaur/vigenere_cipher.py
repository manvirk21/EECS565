import time


def vigenere_cipher(text, key, mode):
    text = text.replace(" ", "").lower()
    key = key.lower()
    result = ""

    for i in range(len(text)):
        char = text[i]
        if char.isalpha():
            key_char = key[i % len(key)]
            if mode == "encrypt":
                shift = (ord(char) - ord('a') + ord(key_char) - ord('a')) % 26
                result += chr(ord('a') + shift)
            elif mode == "decrypt":
                shift = (ord(char) - ord('a') - (ord(key_char) - ord('a'))) % 26
                result += chr(ord('a') + shift)
        else:
            result += char

    return result


def load_dictionary(file_path):
    with open(file_path, 'r') as file:
        return set(word.strip().lower() for word in file.readlines())


def vigenere_cracker(ciphertext, key_length, first_word_length, dictionary):
    start_time = time.time()
    decrypted_messages = []

    for key_candidate in generate_key_candidates(key_length):
        plaintext = vigenere_cipher(ciphertext, key_candidate, "decrypt")
        first_word = plaintext[:first_word_length].lower()
        if first_word in dictionary:
            decrypted_messages.append((plaintext, key_candidate))

    end_time = time.time()
    elapsed_time = end_time - start_time
    return decrypted_messages, elapsed_time


def generate_key_candidates(key_length):
    # Generate all possible key candidates of length key_length
    from itertools import product
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return [''.join(candidate) for candidate in product(alphabet, repeat=key_length)]



# Load the dictionary from dict.txt
dictionary = load_dictionary('dict.txt')

# Messages to decrypt
messages_to_decrypt = [
    ("MSOKKJCOSXOEEKDTOSLGFWCMCHSUSGX", 2, 6),
    ("PSPDYLOAFSGFREQKKPOERNIYVSDZSUOVGXSRRIPWERDIPCFSDIQZIASEJVCGXAYBGYXFPSREKFMEXEBIYDGFKREOWGXEQSXSKXGYRRRVMEKFFIPIWJSKFDJMBGCC", 3, 7),
    ("MTZHZEOQKASVBDOWMWMKMNYIIHVWPEXJA", 4, 10),
    ("SQLIMXEEKSXMDOSBITOTYVECRDXSCRURZYPOHRG", 5, 11),
    ("LDWMEKPOPSWNOAVBIDHIPCEWAETYRVOAUPSINOVDIEDHCDSELHCCPVHRPOHZUSERSFS", 6, 9),
    ("VVVLZWWPBWHZDKBTXLDCGOTGTGRWAQWZSDHEMXLBELUMO", 7, 13)
]

for ciphertext, key_length, first_word_length in messages_to_decrypt:
    decrypted_messages, elapsed_time = vigenere_cracker(ciphertext, key_length, first_word_length, dictionary)

    print(f"Decrypted message for key length {key_length}, first word length {first_word_length}:")
    for message, key in decrypted_messages:
        print(f"Plaintext: {message}")
        print(f"Key: {key}")
    print(f"Time elapsed: {elapsed_time} seconds\n")
