# Respostas

## 12.1
/* 
Exercício mal estruturado, pois não explicita a existência
da chave pública 'e' para o protocolo de assinatura digital. 
Para mais, não define nenhum padrão de separação da concatenação
entre a mensagem 'x' e sig(h(x)). Seria necessário que houvesse
um padrão no tamanho da mensagem ou da assinatura, ou algum
outro método (caracteres especiais entre ambos, formato de 
arquivo que permite separação em seções, etc).
*/

Protocolo A:
    - x||h(k₂||x) = eₖ₁⁻¹(y) 
    - Como a função de hash é implementada com SHA-1, sabemos 
    que os últimos 160 bits do conjunto x||h(k₂||x) equivalem
    ao hash, enquanto o restante é a mensagem 'x'. Portanto, 
    basta separá-los
    - Checar se m' = h(k₂||x) é igual ao recebido.

Protocolo B:
    - x||sigₖₚᵣ(h(x)) = eₖ⁻¹(y)
    - Assinatura digital é feita com algoritmo de chave pública.
    Portanto, é necessário que o receptor tenha acesso à chave
    pública 'e'. 
    - Para mais, é necessário que o receptor tenha algum modo 
    para separar a mensagem 'x' de sua assinatura, como a definiçao
    de um tamanho padrão para x ou para sig(h(x)). Caso tal
    esquem não seja definido, não há como o receptor decriptar
    o conteúdo.
    - Com 'x' separado de sig(h(x)), o receptor calcular h(x)
    - Com a chave pública 'e', o receptor calcula h(x)ᵉ mod n =
    = sig'(h(x)).
    - Basta então checar se sig'() é igual à assinatura recebida.

## 12.2)
Para funções de hash, um ataque baseado no paradoxo do aniversário
faz com que o número necessário de operações para se achar uma 
colisão é de 2ⁿ/², sendo n o tamanho da saída da função h(x). Porém,
nota-se que em HMACs, um MAC é gerado através de h(k||x). Assim, 
mesmo que um atacante encontre uma colisão, ou seja, um x1 tal que
h(x1) = h(k||x), na hora que o receptor original da mensagem 
realizar a verificação, verá que ocorreu alguma interferência na 
transmissão, já que a verificação é feita através da comparação
entre m' e o MAC recebido. Ou seja, mesmo que o atacante substitua
x por x1 e passe (x1, MAC(x)) para o receptor original, a variável
m' da verificação será calculada através de h(k||x1), tal que,
com altíssima probabilidade, m' = h(k||x1) != h(k||x) = m. Portanto,
ataques de colisão com substituição não são tão eficientes quando
realizados em protocolos que utilizam MACs.
Assim, um método não necessariamente eficiente de atacar o sistema 
descrito é realizar um brute-force na chave e tentar descobrir
qual a correta. Assim, tendo conhecimento de k, o possível atacante
consegue calcular m = h(k||xₐ) para qualquer xₐ arbitrário desejado.
??Qual outro ataque possível??

## 12.3.1)
Uma stream cipher funciona a partir da realização de um XOR entre 
cada bit do plaintext 'x' e cada bit da keystream 's'. Desse modo, 
se o atacante tem conhecimento de todo o plaintext 'x', ele é capaz
de calcular h(x). Assim, dado que c = eₖ(x||h(x)) = (x||h(x)) ⊕ k,
é possível reverter a operação tal que k = c ⊕ (x||h(x)). Assim, 
tendo conhecimento da chave secreta, o atacante consegue selecionar 
qualquer x' arbitrário desejado, calcular seu h(x') e aplicar a função
de XOR, de modo a garantir-lhe acesso à um c' que, ao passar pelo
processo de verificação do receptor, será considerado legítimo.
Assim, nota-se que o ataque funcionaria até para casos em que a 
encriptação é realizada utilizando one-time pad, porque tal padrão
impede uma chave de ser reutilizada. No entanto, nota-se que o 
atacante deriva a chave 'k' durante o envio da mensagem. Portanto, 
a chave 'k' de uso único será a mesma para o receptor. Caso OTP 
fosse implementado e o atacante tentasse realizar o mesmo ataque 
uma segunda vez, só que com a mesma chave 'k', o ataque falharia,
já que, por definição, a chave seria totalmente nova e independente.

## 12.3.2)
