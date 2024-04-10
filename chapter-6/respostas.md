# Respostas

## 6.1)
Criptografia simétrica tende a apresentar uma segurança
maior, utilizando chaves menores. Assim, com mais eficiência,
é preferível para ser utilizada na maioria das aplicações
atualmente. Porém, apresenta múltiplas falhas ainda sim,
que podem ser resolvidas com criptografia de chave pública,
estabelecendo, portanto, um sistema de criptografia híbrido.

## 6.2)
Utilizando OpenSSL, chegamos que:
1 GByte = 8GBits => 8*10⁹ / 100*10³ = 80000 segundos
Utilizando AES:
8*10⁹ / 17*10⁶ = 470 segundos
Portanto, concluímos que decriptar tal filme utilizando 
criptografia simétrica é 80000 / 470 = 170 vezes mais rápido.

## 6.3)
Seria necessário utilizar e armazenar 120 * 119 / 2 = 7140 
chaves diferentes.

## 6.4.1)
De acordo com livro, o tempo para as operações em RSA aumenta
com o cubo do aumento do tamanho da chave. Portanto, se um
determinado protocolo de RSA-1024 leva 15.7ms, triplicar o 
tamanho da chave implica em um aumento de 3³ = 27 vezes no
tempo necessário. Portanto, a mesma operação passa a demorar
15,7 * 27 = 405ms

## 6.4.2)
Com o mesmo raciocínio, aumentar o tamanho da chave de 1024
para 15360 bits, representa um aumento de 15 vezes na chave.
Consequentemente, o aumento no tempo será de 15³ = 3375 vezes,
isto é, passará de 15,7 ms para 15,7 * 3375 = 52987,5 ms, ou
52 segundos.

## 6.4.3)
O equivalente a aumentar RSA de 1024 para 3072 seria aumentar 
ECC-160 para 256, processo esse que aumenta em 4 vezes o tempo
necessário (no exemplo, passa de 1.3ms para 5.2ms). Para mais, 
RSA-1024 para 15360 é o mesmo que ECC-160 para 512. Assim, deixa
de demorar 1.3ms e passa a levar 42.6ms.

## 6.5.1)

