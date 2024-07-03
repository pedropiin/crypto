# Respostas

## 1.1)
Qualquer ferramenta online de decripção pode ser utilizada.
O texto claro, portanto, é: "Cryptographic systems are 
extrememly difficult to build. Nevertheless, for some reason, 
many non-experts insist on designing new encryption schemes 
that seem to them to be more secure than any other scheme 
on earth. The unfortunate truth, however, is that such 
schemes are usually trivial to break."

## 1.5) 
Ter um oráculo de texto em claro, ou seja, um ataque de
chosen-plaintext, torna decifrar a cifra de Vigenère trivial,
já que um atacante passa a ter acesso a aos mapeamentos
e transformações realizadas para cada caracter. Assim, com
uma rápida análise, é possível formar a chave, analisando
qual caracter foi aplicado em cada posição do plaintext.
A quantidade de caracteres de plaintext necessárias está
associada ao tamanho da chave. Se tal característica é 
satisfeita, sabe-se o valor 'k' da transformação para 
cada posição seguinte de qualquer plaintext ou ciphertext.

## 1.6)
Ao utilizar uma cifra de shift com chave uma chave 'k', as
duas possíveis senhas "abcd" e "bedg" sempre vão apresentar 
textos cifrados diferentes, já que, por exemplo, (a + k) mod 26
!= (b + k) mod 26. Para mais, temos que, para um 'k', uma
encriptação de "abcd" gerará um texto cifrado da forma 
"(a+k)|(b+k)|(c+k)|(d+k)" ≡ "(k)|(k+1)|(k+2)|(k+3)", enquanto
o da senha "bedg" será da forma "(k+1)|(k+4)|(k+3)|(k+6)".
Portanto, basta verificar qual dos dois formatos o ciphertext
observado se encaixa em.


