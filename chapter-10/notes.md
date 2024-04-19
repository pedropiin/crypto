# Digital Signatures
- Esquemas de criptografia simétrica e assmétrica vistos até
então impediam que um terceiro indivíduo fora da troca de mensagens
fosse capaz de visualizar/alterar as informações trocadas.
    - Não apresentam nenhuma segurança para casos em que o indivíduo
    mal intencionado fosse um dos dois lados do esquema
- Assinaturas digitais permitem certificar de que uma mensagem 
de fato foi gerada pelo suposto indivíduo X que a enviou.
    - São uma função de uma chave privada e da própria mensagem x
        - Receptor consegue checar se foi enviada por quem esperava
        atrvés da mensagem, assinatura e chave pública recebida.
            - Impede que um indivíduo negue que enviou a mensagem
            em questão e, também, que uma pessoa maliciosa envie
            uma mensagem fingindo ser outra.
- Serviços de segurança
    - Primários
        - Confidencialidade
        - Integridade
        - Autenticação de mensagens
        - Não repudiação
    - Secundários
        - Identificação/autenticação
        - Controle de acesso
        - Disponibilidade
        - Auditoria
        - Segurança física
        - Anonimato
- SChoolbook RSA Digital Signature Protocol
    - Computar parâmetros do RSA: n = p * q, ϕ(n), e ε [1,ϕ(n)) 
    e d = e⁻¹ mod ϕ(n)
    - Autor da mensagem 'x' realiza s = xᵈ mod n e envia (x, s) para
    o receptor da mensagem, que com a chave pública e, verifica se
    x' = sᵉ mod n = x.
        - Não encripta a mensagem. Apenas garante autenticação e 
        integridade
        - Papéis invertidos do RSA
    - Na maioria das aplicações, uma assinatura é gerada apenas uma vez,
    enquanto a verificação dela é realizada múltiplas. Portanto, uma 
    chave pública pequena permite que a exponenciação da verificação
    seja um processo muito rápido.
    - Permite ataque de forgery
        - Oscar, com base na chave pública (n, e) de Bob, escolhe uma 
        assinatura s, calcula x = sᵉ mod n e envia para Alice fingindo
        ser Bob. 
        - Alice checa que sᵉ = x mod n e não consegue reconhecer que a 
        mensagem não veio de Bob
        - Oscar não tem controle sobre a mensagem x que vai ser enviada.
