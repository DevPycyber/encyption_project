
def caesar_encrypt(plaintext, key):
    """
    input = string plaintext, int key
    output = string cyphertext
    """
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',\
                 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    index = 0
    cyphertext = ""
    for i in range(len(plaintext)):
        index = (alphabet.index(plaintext[i])+key)%26
        cyphertext += alphabet[index]
    return cyphertext

assert caesar_encrypt("saluz", 2) == "ucnwb"
assert caesar_encrypt("bonjour", 10) == "lyxtyeb"

def caesar_decrypt(cyphertext, key):
    """
    input = str cyphertext, int key
    output = str plaintext
    """
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',\
                 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    index = 0
    plaintext = ""
    for i in range(len(cyphertext)):
        if alphabet.index(cyphertext[i]) - key < 0:
            if key < 25:
                index = 26 - (abs(key) -alphabet.index(cyphertext[i]))
            elif key % 26 > 0:
                index = 26 - (key%26  -alphabet.index(cyphertext[i]))
        elif alphabet.index(cyphertext[i]) - int(key) >=  0:
            index = alphabet.index(cyphertext[i]) - int(key)

        if key % 26 == 0 and key != 0:
            index = alphabet.index(cyphertext[i])
        plaintext += alphabet[index]
    return plaintext


assert caesar_decrypt("tata", 2) == "ryry"
assert caesar_decrypt("bonjour", 10) == "redzekh"