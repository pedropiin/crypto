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
