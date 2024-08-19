# CCA-Security and Authenticated Encryption

- ## 5.1 - Ataques de texto cifrado escolhido (CCA) e Segurança-CCA
	- Um ataque de texto cifrado é baseado na habilidade de um adversário/indivíduo malicioso de interferir ou modificar mensagens enviadas de um remetente à um destinatário. A ideia é que o adversário faz com que o receptor decripte mensagens geradas pelo próprio adversário.
		- Analisamos os efeitos disso na integridade da comunicação, e agora analisaremos a segurança.
	- 5.1.1 - Ataques de Oráculos de *Padding* (Preenchimento)
		- PKCS #7
			- Padrão de preenchimento extremamente popular
			- Seja *L* o número de bytes do bloco da função *F<sub>k</sub>* e *b* > 0 o número de bytes que faltam para que a mensagem *m* tenha tamanho múltiplo de *L*. O preenchimento adiciona *b* vezes o número *b* (representado em hexadecimal) no final da mensagem e depois ela é encriptada.
				- Se *b* = 4, é adicionado ao final da mensagem os bytes 0x04040404.
				- A mensagem antes de ser encriptada, com o padding adicionado, é chamada de codificada.
			- Decriptação usando PKCS funciona normalmente: o ciphertext é decriptado e depois há uma checagem para ver se o padding é válido, isto é, se o último byte *b* é repetido *b* vezes no final. Caso não seja, a função devolve um erro.
		- 