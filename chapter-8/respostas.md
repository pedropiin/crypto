# Respostas

## 8.1.1)
a     | 1 | 2 | 3 | 4
ord(a)| 1 | 4 | 4 | 2

## 8.1.2)
a     | 1 | 2 | 3 | 4 | 5 | 6
ord(a)| 1 | 3 | 6 | 3 | 6 | 2

## 8.1.3)
a     | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12
ord(a)| 1 | 12| 3 | 6 | 4 | 12| 12| 4 | 3 |  6 | 12 | 2]

## 8.2) 
Sabemos que para todo a ε G, ord(a) | |G|. Desse modo, podemos afirmar
que as ordens possíveis são 1, 2, 4, 13, 26 e 52, já que são os únicos
divisores de 52. Temos que, se α é primitivo de G, para todo k | n, 
temos que αⁿ/ᵏ é gerador de um subgrupo de G de ordem k, composto 
exatamente pelos elementos 'a' tais que aᵏ = 1. Portanto, temos 52 
1 elemento de ordem 1, 2 elementos de ordem 2, 4 elementos de ordem 4,
13 elementos de ordem 13 e 26 elementos de ordem 26.

## 8.3.1)
Assim como falado na questão acima, cada subgrupo multiplicativo de G
têm sua ordem equivalente a um divisor da ordem de G. Portanto, tem-se
grupos com 1, 2, 4, 13 e 26 elementos.

## 8.3.2)
Sim. A ordem de todos os grupos divide a ordem do grupo "original"

## 8.3.3)
Em Z*₅, os elementos primitivos são 2 e 3.
Em Z*₇, os elementos primitivos são 3 e 5.
Em Z*₁₃, os elementos primitivos são 2, 6, 7 e 11.

## 8.3.4)
|Z*₅| = 4 ==> ϕ(|Z*₅|) = (2² - 2¹) = 2
|Z*₇| = 6 ==> ϕ(|Z*₇|) = (2¹ - 2⁰)*(3¹ - 3⁰) = 2
|Z*₁₃| = 12 ==> ϕ(|Z*₁₃|) = (2² - 2¹)*(3¹ - 3⁰) = 4
Portanto, verifica-se o solicitado.

## 8.4.1)
ϕ(|Z*₄₉₆₉|) = ϕ(4968) = (2³ - 2²) * (3³ - 3²) * (23¹ - 23⁰) = 1584

## 8.4.2)
P(aεZ*₄₉₆₉ primitivo) = 1584 / 4968 = 0,31884 = 31,884%

## 8.4.3)
O menor gerador a ε Z*₄₉₆₉, tal que a > 1000 é 1005.

## 8.4.4)
Um método eficiente para acelerar a procura por geradores de um
grupo arbitrário Z*ₚ é o proposto no enunciado do exercício acima.
Funciona da seguinte forma: ao invés de calcular todas as potências
de um possível elemento 'a' dentro do invervalo (p - 1) de modo a 
checar se o resultado equivale a 1 mod p apenas quanto o expoente é |Z|,
deve-se calcular os fatores de (p - 1), e checar se o elemento 'a',
quando elevado a todos esses, tem resultado diferente de 1.
Para acelerar ainda mais esse processo, uma estratégia válida é 
utilizar um algoritmo eficiente para encontrar os fatores de p.

## 8.5.1)
A = αᵃ mod p = 2³ mod 467 = 8
B = αᵇ mod p = 2⁵ mod 467 = 32
K = Aᵇ mod p = Bᵃ mod p = 8⁵ mod 467 = 78

## 8.5.2)
A = αᵃ mod p = 2⁴⁰⁰ mod 467 = 137
B = αᵇ mod p = 2¹³⁴ mod 467 = 84
K = Aᵇ mod p = Bᵃ mod p = 137⁴⁰⁰ mod 467 = 90

## 8.5.3)
A = αᵃ mod p = 2²²⁸ mod 467 = 394
B = αᵇ mod p = 2⁵⁷ mod 467 = 313
K = Aᵇ mod p = Bᵃ mod p = 394⁵⁷ mod 467 = 206

As chaves são idênticas, pois:
A = αᵃ e B = αᵇ
k = Aᵇ = (αᵃ)ᵇ = (αᵇ)ᵃ = Bᵃ

## 8.7)
Escolher o valor 1 como chave privada, faz com que um possível
atacante tenha acesso à chave comum secreta facilmente através das
chaves públicas trocadas por Alice e Bob. Verifica-se isso abaixo:
Suponha 'a' chave privada escolhida por Alice = 1 (sem perda de
generalidade, já que o raciocínio é exatamente o mesmo caso Bob
selecionasse). Assim, sua chave pública A = αᵃ = α¹ = α, e a de
Bob será B = αᵇ. Com isso, a chave comum k será equivalente a
Aᵇ = (αᵃ)ᵇ = αᵇ = B ≡ Bᵃ = B.
Portanto, observando apenas as chaves públicas de fácil acesso,
um atacante conseguiria decriptar qualquer informação secreta
trocada por Alice e Bob.
Semelhantemente, caso um dos dois lados selecione (p - 1) como 
chave privada, teríamos que:
A = αᵃ = αᵖ ≡ 1 mod p e B = αᵇ
K = Aᵇ = 1ᵇ = 1
Consequentemente, o atacante teria fácil acesso à chave comum
privada.

## 8.8.1)
