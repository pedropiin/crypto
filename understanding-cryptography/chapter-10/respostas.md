# Respostas

## 10.1)
Um bom algoritmo de assinatura implementado corretamente faz com
que a assinatura dependa da mensagem inteira. Então, caso a mensagem 
sofra alguma alteração durante o seu transporte, por exemplo, a
etapa de verificação vai gerar um resultado negativo, implicando
que a assinatura criada não está relacionada à mensagem que foi 
recebida. Resumidamente, percebe-se que alterar a mensagem implica
em uma alteração da assinatura. Semelhantemente, o processo contrário
também é válido, ou seja, integridade implica em autenticação de
mensagens. Isso se deve ao fato que, dado integridade, um indivíduo
não autorizado é incapaz de alterar o conteúdo da mensagem sem ser
percebido, ou seja, sem ser autenticado.

## 10.2.1)
Privacidade não garante integridade. Uma cifra como AES, por exemplo,
garante que um indivíduo malicioso seja incapaz de ver o conteúdo do
objeto criptografado. No entanto, tal característica não impede que 
ele altere qualquer parte do ciphertext, fazendo com que, por exemplo,
a mensagem chegue alterada para o receptor designado.

## 10.2.2)
Para garantir tanto privacidade como integridade, a mensagem deve ser 
primeiro encriptada para depois passar por um processo de autenticação,
como geração de assinatura. Isso, pois algoritmos de assinatura dependem
do conteúdo inteiro do ques lhe é passado. Caso contrário, a assinatura
não estará relacionada à mensagem criptografada enviada. Consequentemente,
quando o receptor tentasse verificar a autenticação, teria um resultado
negativo.

## 10.4.1)
É muito importante que o sistema que o pintor fosse utilizar garantisse
integridade, confidencialidade, não repudiação e autenticação de mensagens.

## 10.4.2)
Para a encriptação das fotos, o pintor pode utilizar/recomendar que o cliente
utilize criptografia assimétrica, por exemplo, com uma cifra em bloco como
AES. Para a comunicação e transporte da chave utilizada nessa etapa, pode-se
utilizar algum algoritmo de criptografia simétrica, como RSA ou o protocolo
de Elgamal. Por fim, objetivando garantir integridade e não repudiação 
em todas essas etapas, é de suma importância a utilização de algum esquema
de assinaturas digitais, como o protocolo de assinatura de RSA. Se seguido
corretamente por ambas partes, tal protocolo descrito garantirá todos os 
serviços necessários para a segurança do sistema. Alterações como, por exemplo,
utilizar criptografia de chave pública para a encriptação das imagens não
seria uma ideia interessante já que, considerando que os dados encriptados
serão da ordem de múltiplos megabytes, a velocidade oferecida por esses
esquemas não seria interessante.

## 10.5.1)
Para que seja válida, sig(x)ᵉ mod n = x.
∴ 6292¹³¹ mod 9797 = 123 = 123
Portanto, válida.

## 10.5.2)
Para que seja válida, sig(x)ᵉ mod n = x.
∴ 4768¹³¹ mod 9797 = 9644 != 4333
Portanto, inválida.

## 10.5.3)
Para que seja válida, sig(x)ᵉ mod n = x.
∴ 1424¹³¹ mod 9797 = 4333 = 4333
Portanto, válida.

## 10.6)
Para realizar um ataque de forjery, basta selecionar um elemento 's' e 
calcular sᵉ mod n = x. Assim, selecionando s = 7336, temos que a mensagem
aleatória enviada por Oscar seria sᵉ = 7336¹³¹ mod 9797 = 326

## 10.7)
Caso Oscar consiga interferir sem nenhum problema no canal de comuniação
entre Alice e Bob e alterar a chave pública de Bob, basta alterar as mensagens
enviadas. Assim, quando Bob enviar o par (x, s) para Alice, Oscar precisa
interferir, de modo a alterar a mensagem conforme desejado, e, com base nova
estrutura, calcular uma nova assinatura com os parâmetros que ele substituiu
inicialmente. Depois, resta apenas enviar (xₐₗₜ, sₐₗₜ) para Alice como se
fosse a mensagem enviada originalmente por Bob. Quando Alice for realizar
a verificação da assinatura, conseguirá um resultado positivo, já que a 
chave pública (n, e) que utilizou para essa etapa era, na verdade, a de Oscar.

## 10.9.1)
No geral, expoentes usados para a assinatura são do tamanho do primo p, ou
seja, de 1024 bits. Portanto, em média, tem-se 512 bits com valor 1, e,
portanto, são realizadas 512 multiplicações, isto é, l/2. Já a verificação 
com um expoente pequeno (e.g. e = 2¹⁶ + 1), apenas 2, já que temos apenas 
dois bits equivalentes a 1.

## 10.9.2)
A assinatura é a etapa mais demorada, pois, na prática, os expoentes utilizados
são muito maiores do que na verificação, implicando em cálculos mais custosos

## 10.9.3)
Caso n = 512:
m = 16 => 1 op leva 16² = 256 time units
Se 'd' e 'e' são de tamanho completo, i.e., 512 bits, uma assinatura/verificação
leva necessita de 768 operações.
Assim, 768 * 256 = 196608 t.e. = 196,608 ms
Se 'e' é otimizado para um tamanho pequeno, como 2¹⁶ + 1, a verificação precisa
de 18 operações
Assim, verificação leva 18 * 256 = 4608 t.e. = 4,608 ms

Caso n = 1024:
m = 32 => 1 op leva 32² = 1024 time units.
Se 'd' e 'e' de tamanho completo, assinatura e verificação leva 1536 operações
Assim, 1536 * 1024 = 1572864 t.e. = 1,572 s
Se 'e' é otimizado para um valor pequeno, como 2¹⁶ + 1, a verificação precisa 
de 18 operações
Assim, verificação leva 18 * 1024 = 18432 t.e. = 18,432 ms

## 10.10.1)
p = 97, α = 23, β = 15, d = 67, x = 17 e kₑ = 31
r = αᵏₑ mod p = 23³¹ mod 97 = 87
s = (x - d * r) * kₑ⁻¹ mod p - 1 = (17 - 67 * 87) * 31 mod 96 = 20
∴ (r, s) = (87, 20)
t = βʳ * rˢ mod p = 15⁸⁷ * 87²⁰ mod 97 = 68
αˣ mod p = 23¹⁷ mod 97 = 68 = t
Portanto, segue o esquema.

## 10.10.2)
1:
t = βʳ * rˢ mod p = 15³⁷ * 37³³ mod 97 = 49
αˣ mod p = 23²² mod 97 = 49
∴, a mensagem provém de Bob

2:
t = βʳ * rˢ mod p = 15¹³ * 13⁶⁵ mod 97 = 54
αˣ mod p = 23⁸² mod 97 = 32
∴, a mensagem não provém de Bob.

## 10.10.3)
A assinatura digital baseada em RSA possui algumas vantagens em relação à 
baseada em Elgamal. A principal e mais relevante é a velocidade, já que 
envolve menos operações de exponenciação, e, portanto, menos operações de
multiplicação e potenciação. A verificação por si só fica ainda mais rápida
caso o expoente público 'e' escolhido seja pequeno. Além disso, a etapa de 
geração de chaves do Elgamal é bem mais demorada e complexa, pois aleḿ de um
primo muito grande, é necessário encontrar um corpo finito juntamente a seu
gerador. Já para RSA, basta encontrar dois primos de "meio tamanho". 
Para mais, ela possui uma fraqueza a menos quando ambas implementadas no estilo 
"schoolbook", já que não depende da efemeridade de uma chave aleatória. 
Em Elgamal, caso a chave pública efêmera kₑ seja repetida, um atacante 
consegue bquebrar sem esforço todo o esquema. 
Por último, RSA permite que mensagens sejam enviadas juntamente à assinatura, 
muitas vezes com uma "misturada" na outra, já que suas propriedades garantem a 
validade da recuperação da mensagem. Já em Elgamal, a utilização de uma 
função de hashing é intrínseca à seu funcionamento, característica essa que
impede que o receptor recupere a mensagem 100% das vezes a partir do hashing
Portanto, é necessário que a mensagem seja concatenada à assinatura.

## 10.12)
p = 97, α = 23, β = 15
Seja j = 37 e i = 64. Válidos, pois gcd(j, p - 1) = gcd(37, 96) = 1
r = αⁱ*βʲ mod p = 23⁶⁴ * 15³⁷ mod 97 = 59
s = -r * j⁻¹ mod 96 = -59 * 13 mod 96 = 1
x = s * i mod 96 = 64

## 10.13)
// Por resolução feita na mão, tem-se que o resultado é a fórmula a seguir:
d = (x₁ - s₁ * (x₁ - x₂ + s₂) / (s₁ - s₂)) / r mod p - 1

## 10.14.1)
Dados:
p = 59, q = 29, α = 3, d = 23, h(x) = 17, kₑ = 25
Geração de chaves:
β = αᵈ mod p = 3²³ mod 59 = 45
Assinatura:
r = (αᵏₑ mod p) mod q = (3²⁵ mod 59) mod 29 = 22
s = (h(x) + d * r) * kₑ⁻¹ mod q = (17 + 23 * 22) * 7 mod 29 = 7
Verificação:
w = s⁻¹ mod q = 7⁻¹ mod 29 = 25
u1 = w * h(x) mod q = 25 * 17 % 29 = 19
u2 = w * r mod q = 25 * 22 mod 29 = 28
v = (αᶸ¹ * βᶸ² mod p) mod q = (3¹⁹ * 45²⁸ mod 59) mod 29 = 11
Sei la o que fiz de errado :)
