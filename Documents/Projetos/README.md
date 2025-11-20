# Projetos de Automação para Infraestrutura de Redes

Nesse novo topico, eu me inspirei graças a uma Iniciativa da Cisco para Mulheres chamado Women Rock IT (WRIT), onde tem-se o intuito de auxiliar elas a ter um conhecimento além focado na tecnologia ou até mesmo realizar a migração de area.

<p align="center">
  <h2><p align="center"> 🤖 Women Rock IT (WRIT) 🚀 </p></h2>
  <p align="center"> <img src="https://github.com/ozumaru/CiscoDevNet---Python/blob/master/Documents/img/writ.png" width="700">
</p>

E eu estou aqui para dar essa força, pois é compartilhando conhecimento que nós alcançamos maiores objetivos, isso tanto vai ajudar a elas e a outras pessoas, quando a me ajudar a me auto-desafiar para Mostrar o que tenho de conhecimento, e aprender mais para retornar mais conhecimento.

Dia 18/11/2025 eu ministrei uma aula de Python focado em Infraestrutura de Redes.
 - No Exemplo da atividade, buscamos fazer Boas Praticas em Python para Refatoração de Codigo, criando Classes e Dicionarios para serem reutilizados.
    Pontos que foram vistos:
     - Preparando o Ambiente Virtual do Python (VENV) para instalação de dependencias.
     - Principal Biblioteca utilizada: NETMIKO 
     - Como Manipular Textos em Python e suas estruturas: TUPLA, LISTA, DICIONARIO
     - Utilizado variações do 'SPLIT' para transformar uma 'STRING' em uma 'LISTA'
     - Utilizado o FOR para varredura de dados nas listas
     - Criar, fazer a Leitura e Manipular um dado do tipo JSON.

 - Foi utilizado como Ambiente de Teste o Cisco Sandbox para emular um Switch Catalyst 9K.

E agora eu vou iniciar aqui uma nota etapa para compartilhar mini projetos com esse intuito que gosto de chamar de 'NetDevOps' para compartilhar a todos que buscam criar uma ferramenta para auxiliar no dia a dia, em um vasto ambiente onde que geralmente só estamos apagando Incêndio atrás de Incêndio, que nesse caso é ambiente de Redes de Alta Criticidade, e onde Tudo é Critico, e Tudo é sempre problema de Redes "CRIA WAROOM E CHAMA O POVO DE REDES PRA ANALISAR SE O PROBLEMA É DO LADO DELES! 🔥🤯🔥"... isso as 3 da manhã.

Aqui, eu vou iniciar com o primeiro projeto com base na aula que foi feita com o WRIT, onde que eu tinha preparado 3 projetos, e não consegui passar os 3, e por causa de falta de "!!!IDENTAÇÃO!!!" eu não consegui mostrar de fato o resultado...
A quem estava presente na aula Ao Vivo, peço desculpas encarecidamente.

# Novo Objetivo

Nessa nova etapa, eu preciso Criar mini-projetos, e postar eles já pronto para uso, porem, o "A Mais" que pretendo fazer é criar videos para mostrar como eu cheguei nesse resultado passando por cada etapa.
Eu não sou Youtuber, e não tenho conhecimento algum de manipulação de Video, pois não dá pra fazer com Python.

Outra coisa que eu acho muito importante a se deixar Claro é...
O que venho trazer aqui são Experiencias que eu adiquiri que foram se somando desde 2017 até os dias de hoje.
Meu foco Principal é Infraestrutura de Redes, mas sei um pouco de Python, então eu sou uma pessoa de Infra que aprendeu programação para lidar com o dia a dia nesse mundo de redes, e agora estou a compartilhar isso.

Caso você chegou aqui por algum milagre em busca de aprender Python do Zero de formas mais Didatica e bem mais focado em Conceito, eu vou te passar exatamente o caminho que fiz, e é o caminho que eu passo para TODO MUNDO para aprender.

Segue essas duas Playlists:

⚠️ OBS: Tudo que for link que direcione para outro lugar a não ser internamente no GITHUB como os projetos abaixo, abra com o botão direito + nova aba, pois assim vai abrir uma nova aba e vai manter essa em aberto.

Onde você vai aprender o Basico sobre Algoritimo e Lógica Computacional
- [ME SALVA](https://www.youtube.com/watch?v=ntBxoTSnfkA&list=PLf1lowbdbFIBoLeVGwkCYySkLS1lV3ixF)

Onde você vai aprender de forma FANTASTICA sobre Python Conceito por Conceito, tendo Diversos exercicios, com o Mestre Renomado: Gustavo Guanabara
- [Curso em Video](https://www.youtube.com/watch?v=S9uPNppGsGo&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=2)

Esses são meus dois pontos de referencia para começar nesse mundo de programação, e foi onde eu comecei, sou muito grato a eles.

Antes de seguir para o primeiro projeto, eu preciso informar que aqui eu vou publicar o conteudo já em seu estato final, e aos poucos (conforme vou aprendendo também) eu vou publicando o video, mostrando cada etapa até chegar naquele resultado.

# Primeiro
### 🥸 BACKUP/INTERFACE/VLAN

Nesse projeto primeiro projeto, alem dos 3 desafios principais que são: Rotina de BACKUP, Documentação de Status de Interface, Aplicação de Configuração de Vlans
Vamos focar também na parte de Refatoração do Codigo, já que teremos algumas estruturas que iram se repetir algumas vezes, vamos criar Funções para reutilização desses Algoritimos, e quando tivermos mais funções, vamos criar uma Classe para agrupar essas funções de acordo com cada função.

- [1° - BACKUP/ INTERFACE/ VLAN](https://github.com/ozumaru/CiscoDevNet---Python/tree/master/Documents/Projetos/Primeiro)

