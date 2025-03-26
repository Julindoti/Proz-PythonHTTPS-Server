Questões a serem respondidas: 

1-O que acontece quando tentamos acessar https://localhost:8443  no navegador? 

R= A nossa configuração .py faz uma conexão do nosso servidor e encripta os dados de conexão obtidos, fazendo que todo processo de comunicação seja seguro

2-Por que aparece um aviso de segurança?

R= Por ser uma assinatura propria, sem nenhum tipo de verificação de autenticidade

3-Filtro tls no wireshark. Os dados são legiveis?

R=Não, não é legivel justamente pelo papel das verificações TLS, essa resposta em "branco" é gerada pela validação dos dados encriptados da comunicação entre cliente e servidor, ou seja, esta tudo correndo bem em questões de invisibilidade de dados.

4-quais os pacotes que aparecem na negociação do protocolo TLS?

R=Alguns pacotes de dados de aplicação, Server Hello e Client Hello

5-o que significam Server Hello e Client Hello?

R=Client Hello é a mensagem que um cliente envia para um servidor dando inicialização a uma conexão segura, essa mensagem contem ,por exemplo, versões especificas de TLS. Server Hello é a resposta do server aos requerimentos feitos pelo cliente no Client Hello , ele responde com as versões de TLS citadas a cima, criando compatibilidade e assegurando todo processo.

6-Qual a principal vantagem do HTTPS  em relação ao HTTP?

R= Segurança, o HTTPS criptografa todo trafego evitando possiveis sniffings de dados

6- Por que não devemos inserir senhas ou informações sensíveis em sites sem HTTPS?

R= Por essa falta de camada de segurança, qualquer pessoa conectada a rede consegue ver claramente seus dados, acarretando em invasões e perda de dados pessoais

7-O que aconteceria se um atacante capturasse pacotes HTTP em uma rede pública (Wi-Fi de um café, por exemplo)?

R= Ele conseguiria ler todo trafego que esta ocorrendo no local, seja uma simples conversa a um login com informações pessoais como bancos, redes sociais, emails, etc.

8-Como o Wireshark pode ser usado para diagnosticar problemas de rede além de capturar pacotes HTTP/HTTPS?

R=Ele pode ser configurado para ler uma perda de dados por exemplo, ajudando a encontrar em qual setor da rede o problema se encontra.

9-Dê um exemplo de uma aplicação real onde a análise de tráfego de rede pode ser útil.

R= O Wireshark pode ser utilizado em uma sessão de pentest, fazendo esse sniffing na rede ele pode encontrar falhas em comunicações entre dispositivos, rotas com exploits de segurança (acesso a senhas, informações privadas, dados no geral ), captura de movimentações suspeitas com uma ampla gama de ferramentas em todas as verificações.

10-Como funciona o processo de verificação de um certificado SSL em um site real?

R= Apartir do momento que o navegador se conecta a um dominio seguro por SSL/TLS  é gerada uma solicitação de informações indentificaveis, como uma verificação de documentos, em seguida o servidor envia os certificados SSL/TLS que possuem a chave pública da conexão, assim estabelecendo uma comunicaçãp segura.

11-O HTTPS pode ser quebrado? Se sim, como e em quais casos?

R= Sim, pode ser quebrado. criptografia desatualizada (de baixa qualidade), MITM, Utilização de certificados falsos dentre varios outros meios de exploração.