# Respostas

## 5.1) Show that the CBC, OFB and CTR modes of operation do not give CCA-security encryption schemes.
CBC: Um esquema criptográfico $\Pi$ não é seguro implica que qualquer adversário *A* arbitrário tem P[PrivK<sub>A, Π</sub><sup>cca</sup> = 1] > 1/2 + *negl*, ou seja, *A* consegue acertar o bit *b* de desafio para uma mensagem *m* arbitrária com probabilidade melhor do que de chute. Para isso, ao receber o ciphertext desafio *c<sub>b</sub>*, basta *A* mudar o último bit de *c<sub>0<sub>b</sub></sub>*, consultar Dec<sub>k</sub>(.) com o ciphertext alterado e comparar o recebido com as duas mensagens *m<sub>1</sub>* e *m<sub>2</sub>* recebidas. A que tiver todos os bits iguais, exceto pelo último do segundo bloco, é a selecionada pelo desafio, já que *m<sub>1<sub>b</sub></sub>F<sub>k</sub><sup>-1</sup>(*c<sub>1<sub>b</sub></sub>*) $\oplus$ *c<sub>0<sub>b</sub></sub>*.
OFB: A vulnerabilidade passível de ser explorada aqui é a mesma do modo CBC, ou seja, "flipar" um bit no ciphertext "flipa" também um bit no plaintext. Portanto, basta um adversário *A* mudar o último bit de algum bloco do ciphertext desafio, consultar o oráculo de decriptação e comparar o resultado com as mensagens selecionadas para o desafio.
CTR: Por definição, *c<sub>i</sub>* = *y<sub>i</sub>* $\oplus$ *m<sub>i</sub>*. Portanto, novamente, alterações no ciphertext implicam em alterações no plaintext. Assim, a estratégia para o ataque é exatamente a mesma da apresentada no modo OFB e no modo CBC: um atacante *A* arbitrário pode "flipar" um bit de algum bloco do ciphertext desafio, consultar o oráculo de decriptação Dec(.) e comparar o resultado com as mensagens selecionadas, verificando qual difere por apenas o bit na posição alterada.

## 5.2) Write pseudocode for obtaining the entire plaintext for a 3-block ciphertext via a padding-oracle attack on CBC-mode encryption using PKCS #7 padding is used to pad messages to a multiple of the block length before encrypting.
*n* $\leftarrow$ *block_size*
for *i* $\leftarrow$ 0 to *block_size*
	*c'<sub>1</sub>* $\leftarrow$ *c<sub>2</sub>*
	*c'<sub>1</sub>*.invert[*i*]
	*out* $\leftarrow$ Dec(*c'<sub>0</sub>*, *c'<sub>2</sub>*)
	if (*out*)
		continue
	else
		*b* $\leftarrow$ *n* - 1
	for *p* $\leftarrow$ (*n* - *b*) to 0
		for *i* $\leftarrow$ 0 to 255
			*delta* $\leftarrow$ [0x00 * (*p* - 1) + 0x*i* + 0x(*n* - *p* + 1) * (*n* - *p*)] $\oplus$ [0x00 * *p* + 0x*b*(*n* - *p*)]
		*c'<sub>1</sub>* $\leftarrow$ *c<sub>1</sub>* $\oplus$ *delta*
		*out* $\leftarrow$ Dec(*c'<sub>1</sub>*||*c'<sub>2</sub>*||IV)
		if (*out*)
			*m*[*p*] $\leftarrow$ *byte*
			break
	for *p* $\leftarrow$ *n* to 0
		for *i* $\leftarrow$ 0 to 255
			*delta* $\leftarrow$ [0x00 * (*p* - 1) + 0x*i* + 0x(*n* - *p* + 1) + 0x(*n* - *p*)] $\oplus$ [0x00 * *p* + 0x(*n* - *p*) * (*n* - *p*)]
			*IV'* $\leftarrow$ *IV* $\oplus$ *delta* 
			*out* $\leftarrow$ Dec(*IV'*||*c<sub>1</sub>*)
			if (*out*)
				*m*[*p*] $\leftarrow$ 0x(*n* - *p* + 1) $\oplus$ 0x*i*
				break

## 5.3) Describe a padding-oracle attack on CTR-mode encryption, assuming PKCS #7 padding is used to pad messages to a multiple of the block length before encrypting.
O ataque funciona semelhantemente ao ataque quando realizado para uma encriptação em modo CBC. A única diferença é esta na utilização do contador para consultar o oráculo. Formalmente, temos que cada bloco de ciphertext *c<sub>i</sub>* $\coloneqq$ *m<sub>i</sub>* $\oplus$ *F<sub>k</sub>*(*IV*||*i*) = *m<sub>i</sub>* $\oplus$ *y<sub>i</sub>* $\implies$ *m<sub>i</sub>* $\coloneqq$ *c<sub>i</sub>* $\oplus$ *y<sub>i</sub>*, permitindo-nos notar que qualquer $\Delta$ que modifique algum bloco de ciphertext, vai modificar da mesma forma o bloco equivalente de plaintext após decriptação. Basta um adversário *A* arbitrário aplicar o mesmo ataque descrito no livro, porém passando também um contador referente ao bloco sujeito ao ataque, de modo a permitir que a decriptação ocorra como desejada.

## 5.4) Show that Construction 5.6 is not necessarily CCA-secure if it is instantiated with a secure MAC that is not *strongly* secure.
A segurança forte de um MAC garante que um adversário não conseguirá gerar com probabilidade maior do que insignificante uma nova tag *t<sub>i</sub>* $\neq$ *t<sub>1</sub>* para uma mensagem *m* arbitrária tal que Vrfy(*m*, *t<sub>i</sub>*) = 1. Com um MAC não fortemente seguro, um adversário *A* arbitrário é capaz de gerar nova tag para uma das mensagens *m* do desafio, de modo a construir um novo ciphertext (*m*, (*c*, *t<sub>i</sub>*)) $\neq$ (*m*, (*c*, *t<sub>1</sub>*)), com *c* = Enc<sub>k</sub>(*m*) e *t<sub>i</sub>* $\neq$ *t<sub>1</sub>*. Por mais que a encriptação da mensagem seja ainda a mesma, por possuir uma tag diferente, o ciphertext é considerado diferente e pode ser avaliado no oráculo Dec<sub>k</sub>(.). Portanto, basta o adversário *A* consultar tal oráculo com o novo ciphertext para ter, trivialmente, a resposta para o desafio com probabilidade maior do que 1/2 + *negl*, quebrando a segurança CCA do esquema criptográfico.

