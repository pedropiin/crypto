import string

def main():
    cyphered_text = input("Texto a ser decifrado: ")
    key = input("Chave utilizada: ")
    plaintext = ""
    alfabeto = list(string.ascii_lowercase)

    for i in range(len(cyphered_text)):
        if cyphered_text[i] == ' ':
            plaintext += ' '
        else:
            i_letra = (alfabeto.index(cyphered_text[i]) + alfabeto.index(key[i])) % 26
            plaintext += alfabeto[i_letra]

    print(plaintext)

main()