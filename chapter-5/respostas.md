# Respostas

## 5.1) 
Caso usássemos, por exemplo, CBC (Cypher Block Chaining Mode),
teríamos que o cyphertext de cada record dependeria do de outros, 
resultado esse não muito interessante para o caso, já que temos 
independência entre cada dado. Assim, o caso ideal seria utilizar
CTR (Counter Mode), pois não temos interdependência entre os
dados, podemos paraleliza-los, e o processo de encriptação não é
determinístico.

## 5.2.1)
Para quebrar uma cifra em ECB, é necessário apenas um bloco de 
plaintext-cyphertext, já que tal método não realiza nada além
da passagem do plaintext pela cifra de bloco. Assim, nota-se que
ter o par plaintext/ciphertext não reduz em nada o número de 
operações necessárias para quebrar a cifra, mas, na verdade, 
serve como método de verificação da chave. De qualquer jeito 
o atacante vai ter que realizar 2^k operações, mas com o par 
em mãos, ele pode checar se a chave encontrada é a chave correta.
Sem o par, qualquer chave poderia ser válida, e o atacante
não teria nenhum método de checagem.

## .2.2) 
Se o IV (Vetor de Inicialização) é conhecido, o atacante necessita
apenas de um bloco de plaintext/cyphertext para ter uma perspectiva 
de quebrar a cifra com um brute-force. O fato de n > k permite que
a chave encontrada por um brute-force tenha uma chance ínfima de ser 
incorreta. Portanto, conhecendo IV e um bloco de plaintext/cyphertext,
o atacante precisa de 2ᵏ operações para quebrar a cifra, sendo essas
operações associadas ao espaço amostral de chaves.

## 5.2.3)
Sem conhecimento do IV (Vetor de Inicialização), o atacante precisaria
de dois pares plaintext/ciphertext, pois, com o primeiro, mesmo
sabendo o plaintext, o atacante não saberia a entrada da cifra
de bloco, já que ela equivale a um XOR com o IV. Então, na iteração
do segundo par conhecido, ele teria conhecimento de x2, y2 e de x1,
sendo possível, então, fazer o brute-force de 2^k operações, pois 
agora se sabe o input e o output da cifra de bloco. Após essa etapa,
o atacante teria informações suficientes para descobrir o valor de
IV também.

## 5.2.4)
Pode-se afirmar que quebrar uma cifra rodando em CBC é mais difícil
do que a mesma em ECB, já que ECB por si só é inseguro. Ao descobrir
a chave, pode-se afirmar que o atacante quebrou a cifra. Já em CBC, 
o atacante a princípio precisa de mais informações do que ECB, assim
como explicado acima. Mas para ambos os casos, se usam a mesma cifra
em bloco, o número de operações necessárias para um brute-force seria
o mesmo, que, para cifras utilizadas atualmente, é um número irreal
de operações.

## 5.3)
Tendo conhecimento do arquivo automático e de seu conteúdo após ser 
encriptado, basta fazer o processo inverso, ou seja, decriptar o 
arquivo, de modo a conseguir o input da cifra de bloco. Sabe-se que 
o input equivale a um XOR entre o arquivo e o IV. Portanto, basta
apenas realizar um XOR entre o input e o arquivo para conseguir
o IV utilizado. 
Já para o arquivo desconhecido, tem-se conhecimento de seu resultado
encriptado e da chave. Portanto, basta apenas realizar o processo
de decriptação padrão de CBC, isto é: xᵢ = eₖ⁻¹(yᵢ)⊕yᵢ₋₁. No último
caso, já tem-se conhecimento do IV e dos blocos cifrados anteriores,
sendo, portanto, trivial também.

## 5.4)
Para quebrar uma cifra de bloco rodando em OFB, seria necessário
que o atacante tivesse acesso à dois pares de plaintext/ciphertext.
Assim, basta fazer o XOR entre x1 e y1 para descobrir o valor dos
primeiros 128 bits da keystream (supondo AES), ou seja, o primeiro
bloco gerado pela cifra. Porém, não se tem conhecimento do IV, então,
consequentemente, o atacante não sabe o input da cifra que gerou
os 128 bits b em questão. Portanto, ele necessita realizar mais 
uma iteração do processo, onde, do mesmo modo, utilizando x1 e y2,
descobre b2. Com isso, agora o atacante tem conhecimento do output 
b2 e do input b1 da cifra de bloco em questão, restando apenas 
realizar um ataque brute-force para descobrir as possíveis chaves.

## 5.5)
Caso o IV não altere para cada execução da encriptação, temos que
a key stream será sempre a mesma, já que o mesmo IV gera um certo 
s0, que, por sua vez, será usado como input para gerar o s1, e 
segue o ciclo. Assim, com o mesmo IV, todos os inputs de todas as
iterações será exatamente o mesmo. Assim, qualquer cifra de bloco
rodando em OFB se torna determinística, isto é, um mesmo plaintext
será sempre encriptado da mesma forma, gerando o mesmo ciphertext.
Assim, caso o atacante não conheça nenhum par plaintext/ciphertext,
os ataques que ele pode fazer são os do mesmo tipo que os exemplos
do livro para ECB, isto é, envolvendo alteração de informações
no próprio ciphertext. Caso ele tenha conhecimento de, por exemplo,
um par, torna-se trivial descobrir um bloco da key stream.

## 5.6)
Considerando que o apertar de uma tecla represente um byte, podemos
iniciar o processo escolhendo um IV aleatório para a cifra. Assim, 
passamos-lhe pela cifra de bloco e, do output, selecionamos apenas
o byte mais significativo, isto é, aquele mais à esquerda. Com ele,
realizamos um XOR com byte proveniente do teclado para gerarmos o 
ciphertext, isto é, o valor do teclado encriptado. Como próximo 
input da cifra de bloco, uma estratégia interessante seria realizar
um shift para a esquerda de 1 byte no output da cifra de bloco,
e colocar o byte selecionado na iteração anterior nas posições menos
significativas, gerando um IV novo.

## 5.7.2) 
Tal método de encriptação é extremamente fraco, pois a entrada
da cifra de bloco sempre terá apenas 8 bits variando, implicando em
256 possibilidades de entrada, mesmo com o bloco sendo de 128 bits.
Assim, nota-se que o output da cifra entrará em um ciclo muito cedo,
pois são poucas as possibilidades de entradas para a cifra de bloco.
Mais especificamente, temos 256 possibilidades de entradas para 
saídas de 128 bytes. Desse modo, 256 * 128 = 32768 bits = 4096 bytes 
= 2 kBytes é o tamanho máximo do ciclo da keystream sᵢ utilizada no
XOR com o plaintext. Com isso, se um indivíduo tentar encriptar um 
arquivo de 100kBytes, muitas das iterações vão ter chaves repetidas.
Por fim, se um atacante tem conhecimento de 2kBytes do plaintext 
(equivalente a 256 blocos), ele consegue quebrar o esquema.

## 5.7.3) 
O esquema não fica mais seguro, já que ainda sim ele disponibiliza
apenas 256 possibilidades de bytes de feedback FB. Assim, por mais que
os bytes restantes não sejam iguais a zero, são apenas uma repetição,
característica essa que não influencia em nada no aumento da segurança.

## 5.9) 1TB = 1024 GB = 2¹⁰ GB = 2⁴⁰ Bytes
Portanto, o tamanho máximo do IV é de 88 bits, ou 11 Bytes, já que 
se utilizasse um bit a mais, por exemplo, o contador não conseguiria
atingir 1TB, sendo necessário repetir números, e, portanto, poderia 
haver chaves repetidas no processo de encriptação.

## 5.10.1) 
Se a encriptação e a decriptação forem feitas usando ECB, Bob terá 
problemas apenas no entendimento do plaintext xᵢ relacionado ao bloco
cifrado yᵢ em questão. Isso se deve ao fato de que ECB não relaciona
iterações do processo de encriptação. Portanto, cada bloco é independente.

## 5.10.2)
Diferentemente, ao utilizar CBC, todos os blocos de plaintext encriptados
após yᵢ são afetados, devido à propriedade de feedback do modo em 
questão. Assim, caso i = 1, por exemplo, todos menos o primeiro bloco
de texto seriam encriptados com um erro.

## 5.10.3)
Assim como caso o erro ocorresse no bloco cifrado, o erro será disperso
para os blocos seguintes. A única diferença nesse caso, isto é, quando 
o erro ocorre no plaintext, todos os blocos cifrados serão afetados 
em grande quantidade, devido a propriedade de difusão. Já quando o
erro aparece no ciphertext, apenas os próximos blocos encriptados terão
grandes alterações, enquanto o bloco da iteração em questão terá apenas
um bit alterado.

## 5.10.4)
Utilizando CFB no modo de 8 bits, temos que, no caso do AES, o erro será
propagado no input da cifra de bloco ao longo de 16 iterações, pois o 
byte continuará no input, mudando apenas de posição através dos shifts
para a esquerda. Nas iterações seguintes, por mais que o byte alterado
não esteja mais no input diretamente, os outputs gerados por ele terão
em si seus respectivos erros difundidos, já que são frutos de uma 
encriptação ou decriptação utilizando uma entrada adulterada. Então, 
resumindo, nesse caso, ocorrerá dois tipos de erros: os diretamente 
relacionados à entrada da cifra e os relacionados ao sistema de feedback 
do modo utilizado.

