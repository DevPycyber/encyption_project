
def vernam_encrypt(plaintext, mask):
    mask = mask.split(',')
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',\
                 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    index = 0
    cyphertext = ""
    for i in range(len(plaintext)):
        index = ((alphabet.index(plaintext[i]))+int(mask[i]))%26 
        cyphertext += alphabet[index]
    return cyphertext

#version finale
def vernam_decrypt(cyphertext, mask):
    mask = mask.split(',')
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',\
                 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    index = 0
    assert len(cyphertext) == len(mask), "Veuillez entrer des entrées de même longueur"
    plaintext = ""
    for i in range(len(cyphertext)):
        if alphabet.index(cyphertext[i]) - int(mask[i]) < 0 and int(mask[i]) % 26 != 0:
            if int(mask[i]) < 26:
                index = 26 - abs(int(mask[i]) - alphabet.index(cyphertext[i]))
            elif int(mask[i]) > 26:
                if alphabet.index(cyphertext[i]) - int(mask[i]) % 26 < 0:
                    index = 26 - (int(mask[i])%26 - alphabet.index(cyphertext[i]))
                elif alphabet.index(cyphertext[i]) - int(mask[i]) % 26 > 0:
                    index = alphabet.index(cyphertext[i]) - int(mask[i])%26

        elif alphabet.index(cyphertext[i]) - int(mask[i]) >=  0:
            index = alphabet.index(cyphertext[i]) - int(mask[i])

        if int(mask[i]) % 26 == 0 and int(mask[i]) != 0:
            index = alphabet.index(cyphertext[i])
        plaintext += alphabet[index]
    return plaintext

print(vernam_decrypt("hello", "10000,50,20,56,65"))