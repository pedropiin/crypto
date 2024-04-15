# Notes
--> Diffie-Hellman Key Exchange (DHKE)
    --> Método para estabelecimento de chaves seguras em 
        um canal não seguro
    --> Funciona da forma:
        --> Selecione publicamente um primo 'p' grande
            e um inteiro 'α' >= 2 e <= p - 2
        --> Alice seleciona um elemento 'a' privado, tal
            que a ∈ {2, ..., p - 2} e calcula A como
            αᵃ mod p. Bob, do outro lado, faz o mesmo:
            seleciona 'b' privado, com b ∈ {2, ..., p - 2}
            e calcula B como αᵇ mod p.
        --> Ambos trocam suas respectivas chaves A e B
        --> A chave segura que será utilizada pelos dois 
            será k = Bᵃ mod p = Aᵇ mod p
                --> A chave estabelecida em conjunto pode
                    ser utilizada de forma segura como 
                    chave, por exemplo, para um algoritmo
                    simétrico como AES.
    --> Propriedades e etapas semelhantes às do RSA, o que
        implica em uma complexidade computacional semelhante.
        --> Não se pode selecionar um expoente pequeno para
            a implementação de DHKE

--> Grupos
    --> ord(a) de um elemento 'a' em um grupo (G,◦) é o menor 
        elemento 'k' tal que aᵏ = a ◦ a ◦ ... ◦ a = 1
    --> Um grupo que contêm um elemento α com ordem máxima, 
        ou seja, ord(α) = |G| é cíclico.
        --> Elementos com ordem máxima são chamados de
            primitivos ou geradores.
    --> TEOREMA: Seja G um grupo finito. Para todo 'a' de G
        --> aᶜᵃʳᵈ⁽ᴳ⁾ = 1
        --> ord(a) divide |G|
    --> TEOREMA: Seja G um grupo cíclico finito.
        --> O número de elementos primitivos de G é Φ(|G|)
        --> Se |G| é primo, todos a != 1 ∈ G são primitivos.
    --> Subgrupos
        --> Todo elemento a de G com ord(a) = s é elemento
            primitivo de um subgrupo cíclico com s elementos
        -->  Se H é subgrupo de G, |H| divide |G|
        --> Seja G grupo cíclico de ordem 'n' com gerador α.
            Para todos inteiros 'k' tal que k|n existe um 
            subgrupo cíclico H de G com ordem 'k'. Esse 
            subgrupo é gerado por αⁿ/ᵏ
            --> H é contido exatamente pelos elementos a de G
                tais que aᵏ = 1.