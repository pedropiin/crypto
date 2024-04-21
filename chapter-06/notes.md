# Introduction to Public-Key Crytography
- Criptografia simétrica é rápida e segura, porém possui
    problemas:
    - Distribuição de chaves de forma segura entre ambas 
        partes
    - Cada indivíduo de uma rede precisa de uma chave para
        cada outro membro da rede. Assim, o número de chaves
        cresce quadraticamente.
    - Não é a prova de desonestidade, ou seja, não há forma
        de verificar se algo enviado por Alice de fato foi
        enviado por ela. 
        - Não há forma prática de garantir não repúdio
    - Para garantir mesma segurança de, por exemplo, uma cifra
        AES, é necessária uma chave de mais de 3000 bits. Assim,
        no geral, sistemas de chave pública são mais lentos 
        que assimétricos por 2-3 ordens de magnitude.

- Criptografia assimétrica (ou de chave pública) consegue 
    garantir múltiplas propriedades
    - Estabelecimento seguro de chaves
        - Distribuição de chaves públicas garante segurança
            através de propriedades matemáticas
    - Não repúdio
    - Identificação
    - Encriptação

- Algoritmo de Euclides Extendido
    - Estabelece mdc(r0, r1) = s * r0 + t * r1
        - Permite achar inversos multiplicativos de inteiros
            em um grupo rapidamente, já que, no final, o valor 
            encontrado de t é um inverso válido.
    - Pode ser realizado com polinômios em corpos de Galois

- Teorema de Euler
    - a^Φ(m) = 1 (mod m)
        - a^(Φ(m) - 1) = a⁻¹ (mod m)