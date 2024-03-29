import string
import numpy as np

def xor(a, b):
    return (int(a) + int(b)) % 2

def text_to_bits(text):
    alfabeto = list(string.ascii_lowercase)
    for i in range(6):
        alfabeto.append(str(i))

    list_bits = []
    for i in range(len(text)):
        list_bits.append(bin(alfabeto.index(text[i])))

    t_bits = ""
    for i in range(len(list_bits)):
        for j in range(len(list_bits[i])):
            if j < 2:
                continue
            if j == 2 and len(list_bits[i]) != 7:
                for a in range(7 - len(list_bits[i])):
                    t_bits += '0'
            t_bits += list_bits[i][j]
    return t_bits

def find_initialization_vector(plaintext, cyphertext, m):
    ptext_bits = text_to_bits(plaintext)
    ctext_bits = text_to_bits(cyphertext)

    iv = []
    key_stream = []
    for i in range(min(len(ptext_bits), len(ctext_bits))):
        bit = xor(ptext_bits[i], ctext_bits[i])
        key_stream.append(bit)
        if i < m:
            iv.append(bit)

    return iv, key_stream, ctext_bits

def find_feedback(iv, keystream, m): 
    coef_matrix = []
    result_vector = []
    for i in range(m):
        eq = []
        result_vector.append(keystream[m + i])
        for j in range(m):
            eq.append(keystream[i + j])
        coef_matrix.append(eq)

    a = np.array(coef_matrix)
    b = np.array(result_vector)
    feedback = np.linalg.solve(a, b)
    for i in range(m):
        if feedback[i] == -1:
            feedback[i] = 1
        elif feedback[i] == -0:
            feedback[i] = 0
    return feedback

def bin_to_char(num_bin):
    alfabeto = list(string.ascii_lowercase)
    for i in range(6):
        alfabeto.append(str(i))



def lfsr(keystream, feedback_coef, ctext_bits, m):
    alfabeto = list(string.ascii_lowercase)
    for i in range(6):
        alfabeto.append(str(i))

    for i in range(len(keystream), len(ctext_bits)):
        new_s = 0
        for j in range(m):
            new_s += feedback_coef[j] * keystream[len(keystream)- m + j]
        new_s = new_s % 2
        keystream.append(int(new_s))

    ptext_bits = []
    for i in range(len(ctext_bits)):
        ptext_bits.append(xor(keystream[i], ctext_bits[i]))

    plaintext = ""
    num_it = ""
    for i in range(len(ptext_bits)):
        if (i + 1) % 5 == 0:
            num_it += str(ptext_bits[i])
            plaintext += alfabeto[int(num_it, base = 2)]
            num_it = ""
        else:
            num_it += str(ptext_bits[i])

    return plaintext


def main():
    known_plaintext = "wpi"
    cyphertext = "j5a0edj2b"
    m = 6
    iv, key_stream, ctext_bits = find_initialization_vector(known_plaintext, cyphertext, m)
    feedback = find_feedback(iv, key_stream, m)
    plaintext = lfsr(key_stream, feedback, ctext_bits, m)
    
    print(plaintext)

main()