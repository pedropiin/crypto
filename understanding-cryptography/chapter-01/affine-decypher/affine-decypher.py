import string

x, y = 0, 1

def acha_mdc(a, b):
    global x, y
    if (a == 0):
        x = 0
        y = 1
        return b

    mdc = acha_mdc(b % a, a)
    x_temp = x
    y_temp = y
    x = y_temp - (b // a) * x_temp
    y = x_temp
    return mdc

def inverso_multiplicativo(a, mod):
    mdc = acha_mdc(a, mod)
    if (mdc != 1):
        return 0
    else:
        return (x % mod + mod) % mod

def stream_decypher_function(inv_mul, b, mod, indice_letra):
    return (inv_mul * (indice_letra - b)) % mod

def decypher(a, b, mod):
    alfabeto = list(string.ascii_lowercase)
    inv_mul = inverso_multiplicativo(a, mod)
    with open ('./cypher.txt', 'r', encoding='utf-8') as cifra:
        with open('./decyphered.txt', 'w', encoding='utf-8') as decifra:
            while True:
                char_cifra = cifra.read(1)
                if not char_cifra:
                    break
                if char_cifra == ' ':
                    decifra.write(' ')
                    continue
                elif char_cifra == '\n':
                    decifra.write('\n')
                    continue
                
                index_letra_cifrada = alfabeto.index(char_cifra)
                index_letra_decifrada = stream_decypher_function(inv_mul, b, mod, index_letra_cifrada)
                decifra.write(alfabeto[index_letra_decifrada])


def main():
    a, b = [int(x) for x in input("Digite os valores de 'a' e 'b' da função afim\n").split()]
    mod = 26
    decypher(a, b, mod)

main()