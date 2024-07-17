# Respostas

## Prova teorema pós 3.25 (pág. 78)
Objetivamos provar que podemos construir uma função pseudoaleatória (PRF) *F* a partir de um gerador pseudoaleatório (PRG) *G*. Portanto, suponhamos que *G* seja um gerador pseudoaleatório válido. Por definição, |P[D(G(k)) = 1] - P[D(r) = 1] $\le$ negl, ou seja, para qualquer diferenciador *D* PPT, a probabilidade de *D* conseguir diferenciar G(k) de uma string uniforme aleatória é insignificante. Porém, vamos provar que se existe um diferenciador *D'* que consegue diferenciar *Fk* de uma função verdadeiramente aleatória, podemos utilizá-lo para construir um diferenciador *D* que distingue entre *G(k)* e uma string aleatória.
O diferenciador *D* funciona da seguinte forma: dado uma string *s*, com |*s*| = *n* * 2<sup>t(n)</sup>, dada pela entrada, *D* busca descobrir se *s* foi amostrada de uma distribuição uniforme ou se foi gerada por G(k). Como dado pelo parágrafo, *Fk* é interpretada como uma lookup-table de 2<sup>t(n)</sup> colunas com strings de tamanho *n* em cada uma. Portanto, é possível construir uma nova função *F'* com base em *s*, em que *F'(i)* equivale ao *i*-ésimo bloco de tamanho *n* de *s*. Assim, *D* chama *D'* passando *F'(i)* como parâmetro e devolve o mesmo resultado que *D'*. Se *D'* devolver 0, significa que a função *F'(i)* não é aleatória, e 1 caso contrário. Assim, como *F'(i)* foi construída com base na string *s*, sabemos que ambas estruturas possuem as mesmas propriedades, e que, portanto, *D* responderia corretamente toda vez que *D'* respondesse corretamente. Porém, como G é um gerador pseudoaleatório, não é possível existir um *D'* que diferencie *F'* de uma função verdadeiramente aleatória com probabilidade maior que insignificante, já que implicaria em uma contradição com a definição de G. Portanto, conclui-se que *F* gerada por G é pseudoaleatória.
## 3.1)