# Respostas

## 2.1)
Seja **Gen** o algoritmo de geração de chaves, *K* o espaço amostral de chaves e *R* o espaço amostral de fitas utilizadas como entrada para o algoritmo **Gen**. Suponhamos que o algoritmo **Gen** seleciona uma chave *k* $\in$ *K* com uma probabilidade *p*, implicando que *k* não necessariamente é selecionada uniformemente. Como **Gen** é randômico e utiliza fitas randômicas para gerar chaves, temos que uma parcela *p* das fitas possíveis leva **Gen** a gerar *k*. 
Agora vamos redefinir o espaço amostral de chaves como o espaço de todas as fitas randômicas *R*, tal que há uma distribuição uniforme sobre *R* para seleção de fitas *r*. Assim, a probabilidade de gerar um mesmo valor *k* não foi alterada, já que existe uma *fração-p* de fitas *r* que levam **Gen** a gerar *k*, reforçando que *k* não é mais considerada a chave nessa reestruturação.
Podemos definir agora a função de encriptação como **Enc**(*m*, **Gen**(*r*)), onde as chaves *r* são selecionadas uniformemente, mas P[C = *c* | M = *m*] não foi alterada, já que *c* é gerado a partir da encriptação de *m* com um valor *k*, e a probabilidade de tal valor *k* particular ser selecionado não foi alterada, como visto acima.

## 2.3)
A afirmação é falsa. Podemos modificar OTP de modo que, ao final da encriptação, um novo bit *b* seja concatenado ao ciphertext, tal que P[*b* = 0] = 1/4 $\neq$ P[*b* = 1] = 3/4. Com isso, é perceptível que o esquema mantém-se como perfeitamente sigiloso, mas não condiz com a afirmação desejada. 
Por definição, um esquema criptográfico é perfeitamente sigilo se $\forall$ *m* $\in$ *M*, $\forall$ *c* $\in$ *C*, P[M = *m* | C = *c*] = P[M = *m*], ou seja, o plaintext e o ciphertext são independentes e analisar um não apresenta nenhuma informação a mais sobre a natureza do outro. Tal propriedade se mantém na versão modificada de OTP apresentada, já que o bit *b* concatenado não está relacionado com a mensagem *m*, implicando que seu valor (0 ou 1) não afeta a probabilidade de nenhuma mensagem *m* ser o plaintext verdadeiro. 

## 2.4)
A afirmação é falsa. Suponhamos um esquema criptográfico $\Pi$ perfeitamente sigiloso. Por Naive-Bayes, P[M = *m* | C = *c*] = (P[C = *c* | M = *m*] * P[M = *m*]) / P[C = *c*] (1). Por definição, P[C = *c* | M = *m*] = P[C = *c*], e como do mesmo modo P[C = *c* | M = *m'*] = P[C = *c*], implica-se que P[C = *c* | M = *m*] = P[C = *c* | M = *m'*]. Aplicando tal resultado em (1), vemos que P[M = *m* | C = *c*] = (P[C = *c* | M = *m'*] * P[M = *m*]) / P[C = *c*] (2). Assim, (2) só é igual a P[M = *m'* | C = *c*] se a probabilidade de *m'* for igual a de *m*. Porém, o enunciado busca uma prova para qualquer distribuição sobre o espaço de mensagens *M*, incluindo distribuição não uniformes. Consequentemente, basta selecionar algum esquema perfeitamente sigiloso em que uma mensagem *m* tem probabilidade *p* $\neq$ *p'*, probabilidade de *m'*. Portanto, prova-se que a proposição do enunciado é falsa.

## 2.5)
Seja *A* um adversário probabilístico que utiliza a distribuição randômica do lançamento de moedas para selecionar um bit *b'* como resposta no experimento. Podemos construir um adversário *A'* que utiliza sempre uma sequência ótima de moedas lançadas por *A* como resposta. Assim, *A'* é determinístico e mantém um desempenho no mínimo igual do de *A* na média, já que seleciona os resultados otimizados do mesmo. Desse modo, podemos sempre assumir que *A* é um adversário determinístico, já que qualquer adversário probabilístico pode ser convertido e otimizado como um novo adversário determinístico.

## 2.6)
$\implies$ Buscamos provar que se um esquema criptográfico é perfeitamente sigiloso, é também perfeitamente indistinguível. Suponhamos $\Pi$ um esquema criptográfico perfeitamente sigiloso. Por definição, P[**Enc<sub>k</sub>(*m0*)** = *c*] == P[**Enc<sub>k</sub>(*m1*)** = *c*]. Sejam *m0* e *m1* as mensagens dadas como entrada por um adversário *A* em um experimento de indistinguibilidade. Definimos também *C0* como o conjunto de ciphertext para quais o adversário *A* dá como resposta do experimento *b'* = 0, e *C1* o conjunto equivalente para *b'* = 1. Válido notar que *C0* $\cup$ *C1* equivalem a todos os ciphertext possíveis. Assim:
P[**PrivK**<sub>A, Π</sub><sup>eav</sup> = 1] == 1/2 * P[**PrivK**<sub>A, Π</sub><sup>eav</sup> = 1 | *b* = 0] + 1/2 * P[**PrivK**<sub>A, Π</sub><sup>eav</sup> = 1 | *b* = 1] == 1/2 * P[*A* responder 0 | *b* = 0] + 1/2 * P[A responder 1 | *b* = 1] == 1/2 * $\sum\limits_{c ∈ C0}$ P[**Enc<sub>k</sub>(*m0*)** = *c*] + 1/2 * $\sum\limits_{c ∈ C0}$ P[**Enc<sub>k</sub>(*m1*)** = *c*] == 1/2 * $\sum\limits_{c ∈ C0}$ P[**Enc<sub>k</sub>(*m0*)** = *c*] + 1/2 * $\sum\limits_{c ∈ C0}$ P[**Enc<sub>k</sub>(*m0*)** = *c*] == 1/2 * $\sum\limits_{c ∈ C}$ P[**Enc<sub>k</sub>(*m0*)** = *c*]  = 1/2 * 1 = 1/2

## 2.7)
0x012345 ^ 0xffeedd = 0xfecd98

## 2.8.a)
O esquema não é perfeitamente sigiloso, já que P[M = 0] = 1/5, porém P[M = 0 | C = 0] = 1/3 (probabilidade da chave ser 0 ou 5). Assim, P[M = *m* | C = *c*] $\neq$ P[M = *m*], contrariando a definição.

2.8.b)
O esquema é perfeitamente seguro e isso pode ser provado pela semelhança com o One-Time Pad (OTP). O esquema descrito funciona da mesma forma que OTP, com o único diferencial sendo concatenar um bit extra = 0 no final. Porém, como a encriptação e a decriptação também concatenam um 0 à chave, tal bit nunca vai ser alterado, e, portanto, pode ser ignorado.

## 2.9.a)
O esquema não é perfeitamente sigiloso. P[Enc(0) = 0] = P[K = 0] = 1/2, porém P[Enc(1) = 0] = P[K = 2] = 0. Portanto, P[Enc(0) = 0] $\neq$ P[Enc(1) = 0], contrariando a definição de sigilo perfeito

## 2.9.b)
Sabemos pelo enunciado que |*M*| = 3 = |*K*| = 3 = |*C*| = 3. Juntamente, nos é informado que **Gen()** seleciona uma chave uniformemente do espaço de chaves. Portanto, $\forall$ *k* $\in$ *K*, P[**Gen()** = k] = 1/|*K*| = 1/3. Juntamente, cada par de plaintext / ciphertext (*m*, *c*) só é ligado por uma chave única *k*, já que só para cada um desses pares, existe apenas um valor que satisfaça a equação de encriptação dentro do espaços amostrais apresentados. Portanto, como ambas condições do Teorema de Shannon foram satisfeitas, o esquema é perfeitamente sigiloso.

2.9.c)
O esquema não é perfeitamente sigiloso, porque quebra a relação *a priori* e *a posteriori* entre mensagem e ciphertext. Por exemplo: P[M = 0] = 1/2, mas P[M = 0 | C = 2] = P[K = 2] = 1/3. Portanto, P[M = *m* | C = *c*] $\neq$ P[M = m].
