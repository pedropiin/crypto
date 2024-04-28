# Key Establishment

- Esquemas e propriedades estudados até então pressupõem
a pré-existência de um canal seguro para transmissão e
estabelecimento das chaves utilizadas.
    - Estabelecimento de chaves = Transporte de chaves
    + Concordância de chaves
    - Frescor de chaves 
        - Garante que chaves geradas são efêmeras, isto 
        é, só são válidas por um pequeno tempo.
        - Garante que caso uma chave seja vazada, haverão
        menos problemas, já que atacantes terão acesso 
        apenas às mensagems passadas durante a validade
        da chave em questão.
        - Para mais, quebrar uma chave implica em pouca
        informação. Para acessar um grande montaten de 
        plaintext, um atacante teria que realizar múltiplos
        ataques e quebras de chave bem-sucedidos.
            - Normalmente implementado através de uma 
            função de derivação de chaves, em que chaves
            efêmeras são geradas a partir de uma mesma
            chave inicial e um parâmetro aleatório 'r'.
                - Pode ser feito com MAC, hash, cifras
                de bloco simétricas, contador, entre 
                outros métodos.
    - Uma implementação ingênua envolve estipular para 
    cada usuário da rede, uma chave para cada outro membro.
    Então, uma rede com n membros, teria que possuir n²
    chaves

- Estabelecimento de chaves com técnicas de Criptografia
Simétrica
    - Muitos sistemas não necessitam de canais seguros 
    para transmissão de chaves entre usuários, pois, por
    exemplo, em uma rede de computadores, a etapa de 
    configuração é considerada um momento seguro em que 
    o organizador é capaz de associar à cada máquina uma
    chave dentro da rede
        - Seria necessário a criação de um canal seguro 
        apenas na entrada de novos membros
    - Key Distribution Center (KDC)
        - Todos os usuário da rede possuem uma chave KEK 
        (Key Encryption Key) kᵤ segura com o centro de 
        distribuiçãod de chaves.
        - Quando Alice deseja falar com Bob, envia um 
        request para o centro, indicando os IDs dos
        envolvidos na futura conversa. O centro avalia
        o pedido, gera uma chave efêmera kₛₑₛ aleatória
        e envia para Alice e Bob uma versão encriptada 
        através de suas KEKs. Assim, ambos lados recebem
        a chave que vão utilizar para se comunicar de 
        modo que apenas eles conseguem ter acesso ao seu 
        conteúdo.
            - yₐ = eₖₐ(kₛₑₛ) e yb = eₖb(kₛₑₛ)
        - Permite que existam apenas n chaves no sistema
        e que cada usuário precise armazenar permanentemente
        apenas uma chave.
        - Replay Attack 
            - Alice e Bob não sabem se a chave efêmera é
            fresca ou reutilizada. Assim, se um atacante
            conseguir acesso à uma chave antiga e enviar
            para ambos fingindo ser o KDC, vai ter acesso
            às informações trocadas com ela.
        - Key Confirmation Attack   
            - Alice não recebe uma confirmação de que a
            chave que recebeu de fato é para se comunicar 
            com Bob. Então um atacante pode interceptar 
            seu request e substituir o ID de Bob pelo 
            seu próprio ID. Assim, a chave efêmera gerada
            será para uma comunicação entre Oscar e Alice,
            enquanto Alice acha que está em um canal seguro
            com Bob.
    - Kerberos
        - Protocolo mais avançado, padronizado pelo RFC, 
        que também garante autenticação dentro do servidor.
        - Alice envia um request para o KDC juntamente 
        com um nonce 'r'. O servidor gera a chave efêmera
        juntamente com uma timestamp associada à validade 
        da chave. Com isso, envia de volta para Alice um
        pacote yₐ = eₖₐ(kₛₑₛ, r, T, IDb) e para Bob um outro
        yb = eₖb(kₛₑₛ, IDₐ, T). 
        - Assim, Alice verifica se o nonce 'r' recebido é
        igual ao enviado, e, portanto, se certifica de
        que o pacote recebido provém do KDC. Para mais, 
        consegue ter certeza de que o canal seguro foi 
        formado entre ela e Bob, assim como planejado, pelo
        fato de receber novamente IDb. Por último, ao 
        verificar a validade da chave, gera também uma
        timestamp associada às suas próprias mensagens, 
        garantindo que Bob tenha certeza de que os recebidos
        não sao reutilizados.
            - Esse sistema de autenticação é chamado de
            challenge-response-protocol, pois, basicamente,
            Alice convida e desafia o KDC a encriptar o 
            seu nonce com sua KEK.
        ![]("./assets/kerberos.png")
    - Problemas com distribuição de chaves baseada em 
    criptografia simétrica
        - Todos os usuários precisam se comunicar com o
        KDC para gerar um canal seguro. Prático para um 
        servidor de uma empresa, mas não para uma escala
        global da internet inteira
        - Dependem da existência de canais seguros na etapa
        de configuração do sistema
        - Se o KDC for comprometido, todo a segurança do
        servidor também é.
        - Não garante PFS (perfect forward secrecy), ou 
        seja, se um atacante tiver acesso à KEK de um 
        usuário, pode tanto ter acesso às próximas mensagens
        quanto às que foram trocadas anteriormente, caso
        tenha guardado-as.

- Estabelecimento de chaves com criptografia assimétrica
    - Resolvem a maioria dos problemas com distribuição
    de chaves baseada em criptografia simétrica
        - Na prática, transporte e concordância de chaves
        são realizadas a partir de criptografia de chave
        pública e a encriptação de dados é feita com 
        criptografia simétrica com as chaves estabelecidas.
    - Man-in-the-Middle Attack
        - Maior problema quando chaves públicas não são
        autenticadas.
        - Em uma Diffie-Hellman Key Exchange (DHKE), um
        atacante ativo consegue interceptar as chaves 
        públicas enviadas por Alice e Bob e repassar 
        para ambos lados sua própria chave pública αᴼ
        fingindo que o protocolo funcionou assim como 
        esperado. Assim, a chave supostamente concordada
        por Alice e Bob será útil apenas para Oscar
        ![]("./assets/mim-dhke.png")
            - Tanto Alice quanto Bob terão diferentes que, 
            além de não permitirem a comunicação entre si,
            só são válidas para comunicações com Oscar.
        - Se bem feito, quando Alice enviar uma mensagem
        'x' para Bob, Oscar pode interceptar e decriptar
        com a chave kₐₒ, obtendo o plaintext supostamente
        secreto. Posteriormente, para simular o funcionamento
        do canal para Alice e Bob, encripta 'x' com kbₒ e
        envia para Bob
            - O atacante, além de obter acesso à mensagem,
            consegue editá-la antes de enviar para Bob, 
            demonstrando ainda mais o potencial de tal 
            ataque.
        