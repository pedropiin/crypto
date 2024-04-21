# Respostas

## 7.1.1)
// Feitos à mão no caderno, pois são exercícios aritméticos.

## 7.4.1)
Considerando que o tempo para realizar uma multiplicação é
igual a x. Assim, utilizando uma chave pública de comprimento
igual a 2048 bits, o algoritmo realizaria 2048 potenciações
e 1024 multiplicações. Portanto, demoraria 2560x. No segundo
caso, utilizando a chave pública como e = 2¹⁶ + 1, seriam 
necessárias 17 potenciações e apenas 2 multiplicações, 
resultando em uma demora de 14,75x. Portanto, há um speedup 
de 182x.

## 7.4.2) 
Não é interessante usar expoentes do formato 2ⁿ - 1, já que 
tais números são da forma 1111111...10 em base binária. Assim,
com o algoritmo square-and-multiply, seriam realizadas muitas
multiplicações e potenciações, enquanto com 2ⁿ + 1, são feitas
apenas 2 multiplicações no meio das potenciações.

## 7.5.1)
Para a etapa de decriptação, é necessário apenas o valor 
de 'n' e de 'd'. Mas 'n' é público por definição. Portanto,
para dificultar um possíve ataque, 'n' tem que ser grande
o suficiente, pois caso contrário, um ataque de brute-force
seria extremamente viável. Já para o 'e' da chave pública, 
por ser público, não há diferença em questões de segurança
se é um valor muito grande ou pequeno.

## 7.5.2)
Um valor mínimo interessante para o tamanho de 'd' é de 
0,3 vezes o tamanho de 'n'. Caso contrário, já existem 
ataques conhecidos e publicados que conseguem descobrir
uma chave privada caso essa tenha um tamanho menor do que
o sugerido acima.

## 7.7)
// Feito a mão no caderno

## 7.9)
O protocolo mais intuitivo para o estabelecimento de uma
chave para um esquema de criptografia de chave simétrica 
é da seguinte forma:
- Bob fala para Alice sua chave pública
- Alice escolhe uma chave privada aleatória com formato
de acordo com as regras sugeridas pela cifra e esquema de
organização de escolha dos dois.
- Alice encripta e envia a chave selecionada utilizando RSA
com a chave pública de Bob
- Bob recebe o ciphertext e o decripta utilizando sua própria
chave privada, conseguindo a chave privada para a cifra
simétrica desejada.
Desse modo, vemos que, a não ser que algum outro processo 
seja adicionado no esquema, Alice que decide qual a chave
da cifra simétrica utilizada.

## 7.10)
Para que ambos lados do protocolo sejam capazes de opinar
e decidir sobre a chave utilizada na cifra simétrica, basta
que ambos enviem a chave desejada para o outro, encriptando-a
no processo, obviamente. Assim, ambos analisam a chave 
proposta pelo outro, e através do RSA, conseguem se comunicar
sobre qual utilizar.

## 7.11.1)
A fórmula de encriptação é x²¹¹¹ = 1141 mod 2623. Porém, não 
é posssível resolver a equação, pois, além de ser um expoente
grande, teria que testar milhares de valores possíveis de x
para encontrar um que resolvesse a equação. No entanto, mesmo
assim, não teria certeza da validade do que foi encontrado, 
pois por se tratar de aritmética modular, existem infinitos
valores que, quando elevados a 2111 em mod 2623 dão 1141.

## 7.11.2)
Não podemos utilizar a fórmula para Φ(n), pois não temos os
fatores de 2623, e fatorar um número grande como esse é 
um processo, matematicamente, extremamente custoso e lento.

## 7.11.3)
Caso calculasse os fatores 'p' e 'q' de 'n', conseguiria
quebrar a cifra. Porém, nesse caso, o meu 'n' tinha um 
tamanho de 11 bits, e, por si só, já seria um processo 
demorado. Portanto, realizar o mesmo com chaves com 
tamanho maior ou igual a 1024 é absolutamente inviável.

## 7.13.1)
Por ser determinístico e não-probabilístico, um RSA 
implementado como apresentado em um schoobook faz com que um 
mesmo plaintext, quando encriptado pela mesma chave, gere o
mesmo ciphertext. Assim, sabendo a chave pública de Bob,
Oscar poderia realizar uma pré-computação dos valores 
encriptados dos caracteres da tabela ASCII com a chave pública
de Bob. Assim, quando analisasse o ciphertext enviado por 
Alice, saberia o que cada número representaria.

## 7.13.2)
n = 3763 ==> p = 53 e q = 71 ==> Φ(n) = 3640
e = 11 ==> d = e⁻¹ mod Φ(n) = 11⁻¹ modo 3640 = 331
Portanto,
x1 = 2514³³¹ mod 3763 = 83 = S
x2 = 1125³³¹ mod 3763 = 73 = I
x3 = 333³³¹ mod 3763 = 77 = M
x4 = 3696³³¹ mod 3763 = 80 = P
x5 = 2514³³¹ mod 3763 = 83 = S
x6 = 2929³³¹ mod 3763 = 79 = O
x7 = 3368³³¹ mod 3763 = 78 = N
x8 = 2514³³¹ mod 3763 = 83 = S
x = SIMPSONS

## 7.13.3)
O ataque deixa de ser possível com a utilização de um 
padding na implementação do RSA, porque, desse modo, o esquema
deixa de ser determinístico. Assim, mesmo que Alice mande 
com caracteres repetidos, todo o ciphertext irá parecer 
aleatório, impedindo com que Oscar pré-computasse os valores
dos caracteres da tabela ASCII.