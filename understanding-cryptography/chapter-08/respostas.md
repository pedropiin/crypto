# Respostas

## 8.1.1)
a     | 1 | 2 | 3 | 4
ord(a)| 1 | 4 | 4 | 2

## 8.1.2)
a     | 1 | 2 | 3 | 4 | 5 | 6
ord(a)| 1 | 3 | 6 | 3 | 6 | 2

## 8.1.3)
a     | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12
ord(a)| 1 | 12| 3 | 6 | 4 | 12| 12| 4 | 3 |  6 | 12 | 2 

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
O valor máximo para as chaves privadas equivale a 2¹⁶⁰ - 1, visto
que a ordem do subgrupo gerado por α é 2¹⁶⁰. Assim, toda chave
privada selecionada no intervalo em questão resultará em uma
potência diferente de α.

## 8.8.2)
Pelo método otimizado explicado pelo livro, a partir da chave 
de máscara, Alice e Bob precisam apenas de uma operação de 
exponenciação para calcular a chave de sessão privada. Alice precisa
realizar βⁱ, e Bob precisa calcular Kₑᵈ. Supondo que ambas chaves
privadas possuem tamanho de 160 bits, utilizando o algoritmo
eficiente de square-and-multiply, ambas operações levariam 160
potenciações e 80 multiplicações, resultando em um tempo de 
700 * 160 + 400 * 80 = 144000 μs = 0,144 s.

## 8.8.3)
Por mais que α agora seja um valor pequeno, não necessariamente
o subgrupo ao qual ele é gerador será menor. O subgrupo pode ser
de tamanho igual ou até maior. Com isso e com os dados do enunciado,
sabe-se que o cálculo da chave da sessão agora demoraria aproximadamente
30 * 160 + 400 * 80 = 36800 μs = 0,0368 s.
Com o algoritmo de square-and-multiply, reduzir o valor de α faz com que
um dos fatores das multiplicaçãoes, isto é, o α, seja menor, sendo,
portanto, um processo menos custoso de ser realizado. Já a exponenciação,
mesmo que α seja um valor menor, a chave privada 'i' utilizada como
expoente não necessariamente diminui, fazendo com que a exponenciação 
se mantenha basicamente a mesma operação em mod p.

## 8.9.1)
Se a = p - 1 em Zₚ, a² = (p - 1)*(p-1) = p² - 2p + 1 ≡ 1 mod p

## 8.9.2)
Se a = p - 1 em Zₚ, temos que ord(a) = 2. Consequentemente, a é
gerador de um subgrupo H, tal que card(H) = 2 e H = {1, a}

## 8.9.3)
Já foi provado em exercícios anteriores a fraqueza de chaves privadas
com valor igual a 1 ou igual a p - 1. Então, tal subgrupo por si só
já apresenta uma fraqueza inerente. Para mais, pelo fato de ter apenas 2 
possibilidades de chaves, um DHKE implementado como schoolbook nesse subgrupo
seria determinístico sob 2 chaves diferentes. Ou seja, caso Alice tentasse
encriptar a mesma mensagem 3 vezes, qualquer atacante conseguiria quebrar
o esquema, pois reconheceria a repetição de uma das chaves.

## 8.10)
α = x², a = 3, b = 12, P(x) = x⁵ + x² + 1
∴ A = αᵃ = x⁶ ≡ x³ + x e B = α¹² = x⁴ + x² + x
∴ Kₐ = Aᵇ = Bᵃ = (x⁴ + x² + x)³ = x¹² + 3x¹⁰ + 3x⁹ + 3x⁸ + 6x⁷ + 4x⁶ + 3x⁵ + 3x⁴ + x³ =
= x¹² + x¹⁰ + x⁹ + x⁸ + x⁵ + x⁴ + x³ = 
= x³ + x + 1

## 8.11)
Se Oscar consegue manipular as mensagens e informações trocadas por
Alice e Bob, basta alterar o valor de uma das chaves públicas das partes
envolvidas. Alterando, por exemplo, a mensagem que envia a chave pública
'B' de Bob para Alice, esta não conseguirá calcular a chave da sessão, já
que realizaria Bᵃ, e, como a base está adulterada, o resultado não será
o mesmo que o calculado por Bob com Aᵇ.

## 8.13.1)
Dados:
p = 467, α = 2, d = 105, i = 213, x = 33
Cálculo das chaves públicas:
Kₑ = αⁱ = 2²¹³ mod 467 = 29
β = αᵈ = 2¹⁰⁵ mod 467 = 444
Encriptação:
Kₘ = βⁱ = 444²¹³ mod 467 = 292
y = x * Kₘ = 33 * 292 mod 467 = 296
Decriptação:
Kₘ⁻¹ = Kₑᵖ⁻ᵈ⁻¹ = 29⁴⁶⁷⁻¹⁰⁵⁻¹ mod 467 = 29³⁶¹ mod 467 = 8
x = y * Kₘ⁻¹ = 296 * 8 mod 467 = 33

## 8.14)
Dados:
p = 31, α = 3, β = 18, Kₑ₁ = Kₑ₂ = 6, y1 = 17, y2 = 25
Por brute-force, temos que
d = 26
Consequentemente:
Kₘ⁻¹ = Kₑᵖ⁻ᵈ⁻¹ mod p = 6³¹⁻²⁶⁻¹ mod 31 = 6⁴ mod 31 = 25
x1 = y1 * Kₘ⁻¹ mod p = 17 * 25 mod 31 = 22
x2 = y2 * Kₘ⁻¹ mod p = 25 * 25 mod 31 = 5

## 8.18.1)
ord(β) = ord(28) mod 29 = 1

## 8.18.2)
Com ord(β) = 1, só existe uma chave de máscara possível: 1. Isso se deve
ao fato de que qualquer exponenciação de β sobre mod29 por qualquer chave
privada