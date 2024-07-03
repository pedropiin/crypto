# Introduction and Classical Cryptography

- Princípio de Kerckhoff
    - Um esquema criptográfico deve ser seguro mesmo que algum
    indivíduo malicioso saiba tudo sobre o esquema, exceto a chave.
    Isso significa que a segurança de uma cifra deve se basear
    na distribuição e escolha da chave, já que todo o resto 
    deve ser tido como conhecimento público.

- Cifras clássicas ^7a72d0
    - Shift Cipher
        - Chave é um valor k ϵ [0, 25] que representa o número 
        de trocas das letras
        - Cifra de César tinha k = 3
        - ROT-13 é uma shift cipher com k = 13
    - Cifra de substituição monoalfabética
        - Basicamente uma cifra afim, em que agora cada letra é
        associada à uma nova letra do texto cifrado individualmente.
            - Portanto, o espaço amostral de chaves contêm todas as 
            possibilidade de bijeções no alfabeto.
        - "Seguro" contra brute-force, mas extremamente vulnerável
        à análises de distribuição de frequência por índice de 
        coincidência.
    - Cifra de Vigenère ou cifra de substituição polialfabética
        - A chave agora é um conjunto de caracteres (uma palavra)
        que é aplicada em blocos individuais do texto em claro.
        Então a mesma letra pode ser mapeada para mais de uma
        outra letra no texto cifrado.
            - Obscura a frequência de cada caractere
        - Se o tamanho da chave é conhecido, pode ser quebrada por
        análise de distribuição de frequência para cada uma das 
        't' streams em O(26*t)
        - Se não conhecido, pode-se utilizar o método de exame de
        Kasiski ou, novamente, índice de coincidência para uma stream,
        de modo a descobrir um palpite provável para 't'.
        - Se uma Cifra de Vigenère for utilizada com uma chave 
        aleatória do tamanho do plaintext, pode ser considerada 
        inquebrável.

- Criptografia Moderna X Criptografia Clássica
    - Princípio I: Definições formais
        - Criptografia moderna estabeleceu como necessário definir,
        previamente ao design de qualquer esquema criptográfico, seus
        objetivos
        - Segurança, informalmente, é definida pela garantia de 
        segurança e pelo modelo de ameaça
            - Garantia de segurança: informalmente, implica que 
            independentemente da quantidade de informação sob 
            conhecimento de um atacante, ele deve ser incapaz de 
            extrair qualquer informação extra do plaintext a partir
            do ciphertext.
            - Modelo de ameaça: relacionado às capacidades de um 
            atacante. A estratégia adotada por um dadas certas habilidades
            é imprevisível, porém, pode-se supor quanto "poder" um
            indivíduo malicioso tem em mãos.
                - Ciphertext-only attack
                - Known-plaintext attack
                - Chosen-plaintext attack
                - Chosen-ciphertext attack
    - Princípio II: Suposições precisas
        - Muitos esquemas criptográficos são baseados em problemas que
        não foram provados que pertencem à NP-completo, mas são problemas
        sem solução eficiente, ou seja, a melhor estratégia envolve
        tentativa e erro. 
        - Portanto, pressupõe-se que são problemas de fato difíceis. Mas
        para que tal suposição seja válida, deve ser precisa e clara 
        para que possa ser provada ou refutada.
    - Princípio III: Prova de segurança
    