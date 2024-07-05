# Perfectly Secret Encryption

- Geração de números pseudoaleatórios
	- Necessário coletar dados com alta entropia e processá-los para que se tornem uniformes e independentes
		- É possível obter dados de alta entropia a partir de fontes externas, como delays entre eventos em algum servidor na web, cliques no mouse, ou até ruído na variação térmica de processadores

- Definições
	- Corretude perfeita
		- **Enc**<sub>k</sub>(m) = *c*, tal que *c* pode ter valores diferentes, isto é, probabilístico; enquanto **Dec**<sub>k</sub>(c) = *m* gerará o mesmo resultado com probabilidade = 1, ou seja, é determinístico.
	- Distribuições probabilísticas sobre *K* dependem do algoritmo de geração de chaves, isto é, **Gen**
	- Distribuições probabilísticas sobre *M* dependem do contexto ao qual o compartilhamento das mensagens faz parte. 
	- Sigilo computacional perfeito
		- Um esquema criptográfico (**Gen**, **Enc**, **Dec**) com espaço amostral de mensagens *M* é **perfeitamente sigiloso** se, para cada distribuição probabilística M, ∀ *m* ϵ *M*, e ∀ *c* ϵ *C*, tem-se que  P[M = *m* | C = *c*] == P[M = *m*]
		- Semelhantemente, podemos definir como: ∀ *m*, *m'* ϵ *M*, ∀ *c* ϵ *C*, temos que P[**Enc**<sub>k</sub>(*m*) = c] = P[**Enc**<sub>k</sub>(*m'*) = c]
		- Para que um esquema criptográfico seja perfeitamente sigiloso,  |*K*| >= |*M*|.
	- Indistinguibilidade computacional perfeita
		- Experimento de indistinguibilidade do adversário
			- Um adversário *A* seleciona um par de mensagens *m0* e *m1*.
			- Uma chave *k* é gerada a partir de **Gen** e um bit *b* é selecionado uniformemente dentro de {0, 1}. 
			- O ciphertext *c* é definido como **Enc**<sub>k</sub>(*m*<sub>b</sub>) e entregado ao adversário *A*. *c* é denotado como o ciphertext de desafio.
			- O adversário *A* produz um bit *b'*.
			- A saída do experimento é 1 se *b'* = *b* e 0 caso contrário. Simultaneamente, **PrivK**<sub>A, Π</sub><sup>eav</sup> = 1 se a saída do experimento é 1 e, consequentemente, o adversário *A* foi bem sucedido. 
		- Seja um esquema criptográfico Π = (**Gen**, **Enc**, **Dec**) com espaço amostral de mensagens *M*. Seja também **PrivK**<sub>A, Π</sub><sup>eav</sup> um experimento de indistinguibilidade do adversário. Π é **perfeitamente indistinguível** ⟺ Pr[**PrivK**<sub>A, Π</sub><sup>eav</sup> = 1] = 1/2.

- One-Time Pad (OTP)
	- Esquema de encriptação perfeitamente sigiloso em que cada mensagem *m* é encriptada através de um XOR com uma chave aleatória *k* única.
		- len(*m*) = len(*k*)
		- Chave *k* deve ser compartilhada através de método seguro e de confiança para ambas partes envolvidas na comunicação.
	- Não eficiente, pois armazenar uma chave do mesmo tamanho de cada mensagem é extremamente inviável. Para mais, deve-se gerar uma chave única para cada mensagem, tal que é impossível prever o tamanho da mensagem a ser encriptada.

- Teorema de Shannon
	- Seja (**Gen**, **Enc**, **Dec**) um esquema criptográfico com |*M*| = |*K*| = |*C*|. O esquema é perfeitamente sigiloso ⟺ 
		- ∀ *k* ϵ *K* tem P[**Gen**() = k] = 1/|*K*|
		- ∀ *m* ϵ *M* e ∀ *c* ϵ *C*, ∃! *k* ϵ *K* | **Enc**<sub>k</sub>(*m*) = c
