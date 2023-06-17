alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',\
         'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def shift_alpha():
    alphas = []
    for i in range(26):
        alpha_mot = []
        index = i
        for i in range(26):
            index  = (index+1)%26
            alpha_mot.append(alpha[index])
        alphas.append(alpha_mot)
    return alphas

def determine_key(key, mot):
    if len(key) < len(mot):
        key_2 = ""
        white = len(mot) - len(key)
        if white <= len(mot):
            key_2 += (key+key[:white])
        elif white > len(mot):
            key_2 += (key+str(white%len(key)))
        return key_2
    elif len(key) > len(mot):
        white = len(key) - len(mot)
        key_2 = key[:len(mot)]
        return key_2
    elif len(key) == len(mot):
        return key
    
def vigenere_encryption(mot, key):
    key = determine_key(key, mot)
    alphabets = shift_alpha()
    cypher_text = ""
    for i in range(len(mot)):
        cypher_text += alphabets[alpha.index(key[i])][alpha.index(mot[i])]
    return cypher_text


def vigenere_decryption(cyphertext, key):
    key = determine_key(key, cyphertext)
    plaintext = ""
    alphabets = shift_alpha()
    for i in range(len(key)):
        for j in range(25):
            if alphabets[alpha.index(key[i])][j] == cyphertext[i]:
                plaintext += alpha[j]
    return plaintext




