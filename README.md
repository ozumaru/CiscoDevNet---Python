# Python para Network

Comecei recentemente nesse mundo da programação para me auxiliar em como otimizar minhas atividades com mais rapidez, busquei por uma linguagem simples para criar ferramentas de automação e agilizar multiplas Tarefas para qualquer coisa.

Mas devido a precisão de criar formas de agilizar meu trabalho com Infra de redes, comecei a buscar formas de automatizar minhas ações a quase Clicks.

Minha intenção aqui é ajudar com o meu breve conhecimento em Python, aqueles que também estão em busca de criar suas próprias soluções para atividades cotidianas em Redes, e dessa forma também conseguirmos criar ferramentas para manusear dados de formas mais isolada, trabalhar com parques de Routers e Switchs utilizando simples scritps em Python para fazer uma coleta em mais de 1000 Switchs, ao em vez de acessar um-por-um e executar o mesmo comando repetidas vezes, o script fará todo o trabalho para você.

Tudo o que venho trazer aqui, é com base em pesquisas por pequenas necessidades... 

- "Preciso levar essa informação de uma Variavel para um Arquivo de texto" ai vou buscar como criar um arquivo com Python e adicionar aquela informação dentro do arquivo de txt.

- "Preciso entender como pegar o nome do Hostname do equipamento para usar como 'Nome_do_arquivo.txt'" lá vou eu buscar entender que tenho que quebrar a Variavel em uma Lista, buscar por indices e trazer o nome do equipamento.

Então são essas pequenas ações que me fazem buscar por uma determinada forma de acrescentar funções e assim construir uma ferramenta na qual eu consiga inserir dentro de uma função maior de acesso.

Sendo assim, devido não ter um aprofundamento a nivel de um Developer que teria muito mais facilidade em construir um Script em dois palitos para fazer tudo isso, eu trago a vocês a visão de um CCNA-R&S que está buscando aprender e compartilhar com base na minha visão, esse Mundo de Programabildiade com a Linguagem Python para utilizar em tarefas do dia-a-dia em uma Infraestrutura de Network. 

## Estruturas
Essa etapa visa mostrar parte por parte de como utilizar cada ação, recomendo que entenda cada uma delas de forma isolada realizando testes no  seu script, copie a formula exata de cada etapa, e teste, e ao compreender, manipular a sua maneira a criação de Variáveis, Condicionais e Estrutura de Loops, realizar essa função de forma mais simples. Fique livre para tentar otimizar o seu script, mas lembrando que essas foram as formas como encontrei para criar o meu próprio. (E que ainda segue em fase de construção)

### 1° Parte
	
Eu começo essa primeira parte com:
- Criar e Ler um Arquivo, pois foi o que eu mais tive dificuldade de entender.
- logo em seguida por 'Dia e hora', isso ira ajudar quando for coletar informação do equipamento, e precisar criar um arquivo diferente para o mesmo equipamento em horas ou dias diferentes, fazendo um Backup da configuração do equipamento.

- Depois como localizar o nome do equipamento dentro de um 'Running-Config', para assim dar o nome ao arquivo posteriormente.

- E enfim, como acessar o equipamento com a Biblioteca Netmiko por meio do protocolo SSH (Secure Shell).
	- [1.1 - Criando e Lendo um Arquivo](https://github.com/ozumaru/CiscoDevNet---Python/blob/master/Documents/Material/1.1%20-%20Criando%20e%20Lendo%20um%20Arquivo.md)
	- [1.2 - Dia e Hora](https://github.com/ozumaru/CiscoDevNet---Python/blob/master/Documents/Material/1.2%20-%20Dia%20e%20Hora.md)
	- [1.3 - IF e FOR - Localizar Hostname](https://github.com/ozumaru/CiscoDevNet---Python/blob/master/Documents/Material/1.3%20-%20IF%20e%20FOR%20-%20Localizar%20Hostname.md)
	- [1.4 - SSH_Netmiko](https://github.com/ozumaru/CiscoDevNet---Python/blob/master/Documents/Material/1.4%20-%20SSH_Netmiko.md)
		- [1.4.1 - Adicionar Hostname ao nome do Arquivo](https://github.com/ozumaru/CiscoDevNet---Python/blob/master/Documents/Material/1.4.1%20-%20Adicionar%20Hostname%20ao%20nome%20do%20Arquivo.md)
		- [1.4.2 - Adicionar Data e Hora atual ao nome do Arquivo de texto](https://github.com/ozumaru/CiscoDevNet---Python/blob/master/Documents/Material/1.4.2%20-%20Adicionar%20Data%20e%20Hora%20atual%20ao%20nome%20do%20Arquivo%20de%20texto.md)
		- [1.4.3 - Usado estrutura de Loop para acessar mais de um devide](https://github.com/ozumaru/CiscoDevNet---Python/blob/master/Documents/Material/1.4.3%20-%20Usado%20estrutura%20de%20Loop%20para%20acessar%20mais%20de%20um%20devide.md)
		- [1.4.4 - Usando Lista externa de IP para acessar multiplos devices](https://github.com/ozumaru/CiscoDevNet---Python/blob/master/Documents/Material/1.4.4%20-%20Usando%20Lista%20externa%20de%20IP%20para%20acessar%20multiplos%20devices.md)

### 2° Parte

- A segunda parte já para aplicar comandos dentro equipamento, embora tenha uma visão um pouco mais complexa, quando aplicar fica mais compreensivel o que está acontecendo enquanto o programa roda, mas busquei detalhar o maximo possivel cada parte com comentários.
	- [ 2.1 - Criação de Multiplas Vlans](https://github.com/ozumaru/CiscoDevNet---Python/blob/master/Documents/Material/2.1%20-%20Criação%20de%20Multiplas%20Vlans.md)
	- [ 2.2 - Criação de interface Loopback](https://github.com/ozumaru/CiscoDevNet---Python/blob/master/Documents/Material/2.2%20-%20Criação%20de%20interface%20Loopback.md)
	- [ 2.3 - Configurando e Validando um P2P](https://github.com/ozumaru/CiscoDevNet---Python/blob/master/Documents/Material/2.3%20-%20Configurando%20e%20Validando%20um%20P2P.md)

### 3° Parte

- Na terceira parte começo a Definir Funções que possam otimizar as aplicações mais complexas separando cada ação em Funções.
	- [ 3.1 - Criando Função: Tomada de Decisão de criar Loopback em 1 ou Multiplos Devices](https://github.com/ozumaru/CiscoDevNet---Python/blob/master/Documents/Material/3.1%20-%20Função%20-%20Tomada%20de%20Decisão%20de%20criar%20Loopback%20em%201%20ou%20Multiplos%20Devices.md)

### 4° Parte

- Nessa quarta parte eu trago com base em minhas vivencias nesse mundo de automação com Python para Network, alguns pontos importantes de Tratamento de Dados, é que o retorno do comando enviado ao Device, esse pontos são;
	- Tratamento de dados em como retornar essas informações em arquivos de textos para cada equipamento.
	- Organizando dos dados de Output de cada equipamento, pois dependendo da quantidade de informações que são exigidas por comandos, organizar essa informação por arquivo para localizar ficar mais Legivel.
		- [4.1 - Loop for para adicionar Dicionarios dentro de uma Lista](Adicionar)
		- [4.2 - Criando arquivos CSV para adicionar listas em ordem](Adicionar)

	- Recentemente uma das minha validações foi para solicitar uma informação muito especifica usando o protocolo CDP (Cisco Discovery Protocol), no entanto, o retorno dessa informação no equipamento tem uma estrura que, quem geralmente usa esse comando, fica mais facil identificar o output, no entanto, em uma grande escala, e dependendo de quantos devices conectados: Switchs, Router, Access Points que usam o protocolo CDP que é proprietário Cisco.
	- Então nessa parte trago tramento de CDP com saida em CSV de forma bem mais estruturada e mais amigavel de se entender.
		- [4.3 - Coleta de CDP e criação de CSV com as informação estruturadas](Adicionar)

### 5° parte
- Rotina de Backup em Linux - Em progresso


## Referencial Bibliografico
 - Variaveis
	- [Tipos de Variaveis: Python Academy](https://pythonacademy.com.br/blog/tipos-de-variaveis-no-python#dicionários-dict)

 - Lista
    - [Manipulação de Lista: Codin Game](https://www.codingame.com/playgrounds/52499/programacao-python-intermediario---prof--marco-vaz/manipulando-listas-continuacao)
    - [Substituir elemento na Lista: DelftStack](https://www.delftstack.com/pt/howto/python/python-list-replace-element/)
    - [Concatenar Itens de uma Lista: Stack Overflow](https://pt.stackoverflow.com/questions/324979/como-concatenar-itens-de-uma-lista-em-python)

 - Funções
    - [Declarando Funções - 1: Stack Overflow](https://pt.stackoverflow.com/questions/324979/como-concatenar-itens-de-uma-lista-em-python)
    - [Declarando Funções - 2: Python Progressivo](https://www.pythonprogressivo.net/2018/06/Como-Declarar-Chamar-Usar-Funcoes-em-Python.html)

- Manipulação de Arquivos
    - [Manipulação de Arquivos - 1: Diego Mariano](https://diegomariano.com/manipulando-arquivos/)
    - [Manipulação de Arquivos - 2: Cafeina Codificada](https://cafeinacodificada.com.br/arquivos-no-python/)

- Biblioteca
    - [Datetime: DelftStack](https://www.delftstack.com/pt/howto/python/python-get-date-today/)
    - [Netmiko - 1: Pypi](https://pypi.org/project/netmiko/)
    - [Netmiko - 2: Python for Network Engineers](https://pyneng.readthedocs.io/en/latest/book/18_ssh_telnet/netmiko.html)

## Autor

José Osmar Caitano

https://www.linkedin.com/in/jose-osmar-caitano-06089113a/

# Licenciamento

[![NPM](https://img.shields.io/npm/l/react)](https://github.com/ozumaru/CiscoDevNet---Python/blob/master/LICENSE)