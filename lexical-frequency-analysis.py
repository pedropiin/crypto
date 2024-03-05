from matplotlib import pyplot as plt
import string
import sys

#inicializar vetor alfabeto
#receber cifra
#vetor frequencia de letras cifradas
#ordenar vetor frequencia acompanhando alfabeto
#plotar frequencia

#associar frequencia da cifra com frequencia ingles
#traduzir

def frequency_analysis():
    alfabeto = list(string.ascii_lowercase)
    vetor_frequencia = []
    
    for i in range(26):
        vetor_frequencia.append(0)

    with open('cypher.txt', 'r', encoding='utf-8') as file:
        while True:
            char = file.read(1)
            if not char:
                break

            if char == ' ' or char == '\n':
                continue
            
            index_letra = alfabeto.index(char)
            vetor_frequencia[index_letra] += 1

    num_chars = sum(vetor_frequencia)
    for i in range(26):
        vetor_frequencia[i] = round((float(vetor_frequencia[i])/num_chars), 4)
    
    frequencia_cifra = [list(letra) for letra in zip(*sorted(zip(vetor_frequencia, alfabeto), reverse=True))]
    print(frequencia_cifra)
    plt.bar(frequencia_cifra[1], frequencia_cifra[0])
    plt.show()

    return frequencia_cifra

def decypher(frequencia_cifra):
    alfabeto = list(string.ascii_lowercase)
    frequencia_ingles = ["0.0817", "0.0150", "0.0278", "0.0425", "0.1270", "0.0223", "0.0202", "0.0609", "0.0697", "0.0015", "0.0077", "0.0403", "0.0241", "0.0675", "0.0751", "0.0193", "0.0010", "0.0599", "0.0633", "0.0906", "0.0276", "0.0098", "0.0236", "0.0015", "0.0197", "0.0007"]
    frequencia_ingles_ordenada = [list(letra) for letra in zip(*sorted(zip(frequencia_ingles, alfabeto), reverse=True))]
    print(frequencia_ingles_ordenada)

    with open('cypher.txt', 'r', encoding='utf-8') as cifra:
        with open('decyphered.txt', 'w', encoding='utf-8') as decifra:
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

                index_letra_cifrada = frequencia_cifra[1].index(char_cifra)
                decifra.write(frequencia_ingles_ordenada[1][index_letra_cifrada])

    return frequencia_ingles_ordenada

def main():
    frequencia_lexical_cifra = frequency_analysis()
    frequencia_ingles_ordenada = decypher(frequencia_lexical_cifra)

main()