# Python para Network

Comecei recentemente nesse mundo da programação para me auxiliar em como otimizar minhas atividades com mais rapidez, busquei por uma linguagem simples para criar ferramentas de automação e agilizar multiplas Tarefas para qualquer coisa.

Mas devido a precisão de criar formas de agilizar meu trabalho com Infra de redes, comecei a buscar formas de automatizar minhas ações a quase Clicks.

Minha intensão aqui é ajudar com o meu breve conhecimento em Python, aqueles que também estão em busca de criar suas próprias soluções para atividades contidianas em Redes, e dessa forma também conseguirmos criar ferramentas para manusear dados de formas mais isolada, trabalhar com parques de Routers e Switchs utilizando simples scritps em Python para fazer uma coleta em mais de 1000 Switchs, ao em vez de acessar um-por-um e executar o mesmo comando repetidas vezes, o script fará todo o trabalho para você.

Tudo o que venho trazer aqui, é com base em pesquisas por pequenas necessidades... 

- "Preciso levar essa informação de uma Variavel para um Arquivo de texto" ai vou buscar como criar um arquivo com Python e adicionar aquela informação dentro do arquivo de txt.

- "Preciso entender como pegar o nome do Hostname do equipamento para usar como 'Nome_do_arquivo.txt'" lá vou eu buscar entender que tenho que quebrar a Variavel em uma Lista, buscar por indices e trazer o nome do equipamento.

Então são essas pequenas ações que me fazem buscar por uma determinada forma de acrescentar funções e assim construir uma ferramenta na qual eu consiga inserir dentro de uma função maior de acesso.

Sendo assim, devido não ter um aprofundamento a nivel de um Developer que teria muito mais facilidade em construir um Script em dois palitos para fazer tudo isso, eu trago a vocês a visão de um CCNA-R&S que está buscando aprender e compartilhar com base na minha visão, esse Mundo de Programabildiade com a Linguagem Python para utilizar em tarefas do dia-a-dia em uma Infraestrutura de Network. 

## Estruturas
Essa etapa visa mostrar parte por parte de como utilizar cada ação, recomendo que entenda cada uma delas de forma isolada realizando testes no  seu script, copie a formula exata de cada etapa, e teste, e ao compreender, manipular a sua maneira a criação de Variaveis, Condicionais e Estrutura de Loops, realizar essa função de forma mais simples fique livre para tentar otimizar o seu script, mas lembrando que essas foram a forma como encontrei para criar o meu próprio. (E que ainda segue em fase de construção)

## Primeira Parte
	
Eu começo essa primeira parte em com:
- Criar e Ler um Arquivo, pois foi o que eu mais tive dificuldade de entender.
- logo em seguida por 'Dia e hora' isso ira ajudar quando for pegar informação de coleta de informação do equipamento, e precisar criar arquivo diferente para o mesmo equipamento em horas ou dias diferete, fazendo um Backup da configuração do equipamento.

- Depois como localizar o nome do equipamento dentro de um 'Running-Config', para assim dar o nome ao arquivo posteriormente.

- E enfim, como acessar os equipamento com a Biblioteca Netmiko por meio do protocolo SSH (Secure Shell).
	- [1.1 - Criando e Lendo um Arquivo] 
	- [1.2 - Dia e Hora]
	- [1.3 - IF e FOR - Localizar Hostname]
	- [1.4 - SSH_Netmiko] 

## Segunda Parte

A segunda parte já para aplicar comandos dentro equipamento, embora tenha uma visão um pouco mais complexa, quando aplicar fica mais compreensivel o que está acontecendo enquanto o programa roda, mas busquei detalhar o maximo possivel cada parte com comentários.
	- [2.1 - Criação de Multiplas Vlans]
	- [2.2 - Criação de interface Loopback]
	- [2.3 - Configurando e Validando um P2P]
	- [2.4 - Configurando Roteamento em Devices multiplos]

## Terceira Parte

Na terceira parte começo a Definir Funções que possam otimizar as aplicações mais complexas separando cada ação em Funções, para que na Quarta parte seja juntado todas etapas em um unico Script.
	- [3.1 - Criando Função - Tomada de Decisão de criar Loopback em 1 ou Multiplos Devices]

## Junção 
Essa etapa visa 

## Autor

José Osmar Caitano

https://www.linkedin.com/in/jose-osmar-caitano-06089113a/


