# Public-Key Cryptosystems Based on the Discrete Logarithm Problem
- Diffie-Hellman Key Exchange (DHKE)
    - Método para estabelecimento de chaves seguras em 
    um canal não seguro
    - Funciona da forma:
        - Selecione publicamente um primo 'p' grande
        e um inteiro 'α' >= 2 e <= p - 2
        - Alice seleciona um elemento 'a' privado, tal
        que a ∈ {2, ..., p - 2} e calcula A como
        αᵃ mod p. Bob, do outro lado, faz o mesmo:
        seleciona 'b' privado, com b ∈ {2, ..., p - 2}
        e calcula B como αᵇ mod p.
        - Ambos trocam suas respectivas chaves A e B
        - A chave segura que será utilizada pelos dois 
        será k = Bᵃ mod p = Aᵇ mod p
            - A chave estabelecida em conjunto pode
            ser utilizada de forma segura como 
            chave, por exemplo, para um algoritmo
            simétrico como AES.
    - Propriedades e etapas semelhantes às do RSA, o que
    implica em uma complexidade computacional semelhante.
        - Não se pode selecionar um expoente pequeno para
        a implementação de DHKE

- Grupos
    - ord(a) de um elemento 'a' em um grupo (G,◦) é o menor 
    elemento 'k' tal que aᵏ = a ◦ a ◦ ... ◦ a = 1
    - Um grupo que contêm um elemento α com ordem máxima, 
    ou seja, ord(α) = |G| é cíclico.
        - Elementos com ordem máxima são chamados de
        primitivos ou geradores.
    - TEOREMA: Seja G um grupo finito. Para todo 'a' de G
        - aᶜᵃʳᵈ⁽ᴳ⁾ = 1
        - ord(a) divide |G|
    - TEOREMA: Seja G um grupo cíclico finito.
        - O número de elementos primitivos de G é Φ(|G|)
        - Se |G| é primo, todos a != 1 ∈ G são primitivos.
    - Subgrupos
        - Todo elemento a de G com ord(a) = s é elemento
        primitivo de um subgrupo cíclico com s elementos
        -  Se H é subgrupo de G, |H| divide |G|
        - Seja G grupo cíclico de ordem 'n' com gerador α.
        Para todos inteiros 'k' tal que k|n existe um 
        subgrupo cíclico H de G com ordem 'k'. Esse 
        subgrupo é gerado por αⁿ/ᵏ
            - H é contido exatamente pelos elementos a de G
            tais que aᵏ = 1.

- DLP (Discrete Logarithm Problem)
    - Achar valor 'x' tal que aˣ = b mod p em um grupo cíclico
    Zₚ de ordem p-1.
        - Pode ser escrito da forma x = logₐb mod p
        - Extremamente complicado, custoso e demorado quando
        parâmetros são suficientemente grandes
        - Na prática, utilizam subgrupo de cardinalidade prima
        para dificultar ataques
    - O GDLP (Generalized Discrete Logarithm Problem) é da mesma
    forma, porém para a operação de grupo do grupo cíclico G
        - Achar 'x' tal que aˣ = a ◦ a ◦ ... ◦ a = b
    - Ataques
        - Brute-force
        - Baby-Step Giant-Step
            - Time-memory tradeoff
                - Complexidade e espaço adicional na ordem de 
                O(sqrt(|G|))
            - Calcular b = aˣ = aˣ¹*ᵐ⁺ˣ², com x1 e x2 calculados
            separadamente, em um intevalo m = sqrt(|G|)
        - Pollard's Rho
            - Gerar elementos aleatórios do grupo da forma aⁱ * bʲ,
            guardando i e j. Quando houver colisão, sabemos por 
            definição que b = aˣ. Portanto, substituindo, chegamos
            que x = (i₂ - i₁) / (j₁ - j₂) mod |G|
            - Mesma complexidade de baby-step giant-step, porém não
            necessita de espaço adicional
        - Pohlig-Hellman
            - Se baseia no CTR
            - Utilizado em conjunto com outros ataques
            - Ao invés de calcular o logaritmo discreto no grupo G, 
            calcula-se o logaritmo discreto xᵢ para os subgrupos 
            de ordem iguais aos fatores de |G|. Assim, com CTR, o 
            a resposta 'x' buscada pode ser derivada de todos os xᵢ.
        - Index-Calculus
            - Algoritmo mais eficiente, e não genérico.
            - Se baseia na ideia de que, em Zₚ e GF(2ᵐ), grande parte
            dos elementos de um grupo G podem ser escritos como o 
            produto de elementos de um subgrupo de G.
            - Principal motivo pelo qual 'p' tem que ter tamanho, no 
            mínimo, igual a 1024 bits.

- Protocolo de Elgamal
    - Se baseia no Diffie-Hellman, mas a ideia é que ambas partes do
    esquema utilizam a chave calculada para "maskear" o plaintext em
    questão.
    - Geração de chave
        - Bob escolhe e divulga publicamente um primo grande 'p' e um 
        elemento primitivo α de Zₚ ou de um subgrupo de Zₚ. Também 
        seleciona privadamente uma chave privada d ∈ {2,..., p−2} e, com 
        isso, calcula a chave pública Kₚᵤ = β = αᵈ mod p
    - Encriptação
        - Com os elementos públicos de Bob (p, α, β), Alice escolhe
        um elemento i ∈ {2,..., p−2} e, assim, calcula uma chave pública 
        nonce kₑ = αⁱ mod p e uma chave privada kₘ = βⁱ mod p para
        ser usada como mask, na forma y = x * kₘ mod p.
    - Decriptação
        - Para decriptar o ciphertext y, Bob faz a operação inversa, ou
        seja, x = y * kₘ⁻¹ mod p, sendo kₘ = kₑᵈ mod p.
            - A chave pública calculada por Alice kₑ e o elemento 'i' devem
            ser utilizados apenas uma vez por encriptação, pois, caso 
            contrário, o esquema se torna determinístico. 
        - Ao invés de calcular kₘ = kₑᵈ mod p para depois calcular a inversão
        kₘ⁻¹, Bob, aritméticamente, sabe que kₘ⁻¹ = kₑᵖ⁻ᵈ⁻¹
    - Caso os parâmetros sejam selecionados corretamente, é impossível
    de ser quebrado. Caso contrário, um brute-force é possível. Para mais,
    se 'i' e kₑ não são únicos, se torna determinístico.
        - Primo p deve ter no mínimo 1024 bits de tamanho para garantir 
        segurança de 80 bits, e 3072 para segurança de 128 bits. Para mais,
        o menor fator primo de p - 1 deve ter no mínimo 160 e 256 bits de
        tamanho para um nível de segurança respectivo.
    - É maleável, portanto Elgamal schoolbook não é comumente implementado.
    Para solucionar, usam padding assim como em RSA.
