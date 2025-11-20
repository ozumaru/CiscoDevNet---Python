# BACKUP/ INTERFACE/ VLAN

Esse projeto tem com objetivo: 
 - Criar uma Rotina de Backup
 - Retornar um Relatório de Status de Interfaces
 - Aplicar configuração de Vlans

O Ambiente que vamos utilizar é o Cisco Sandbox, uma iniciativa da Cisco para Incentivar pessoas a aprender mais sobre Programabilidade de Infraestrutura, e utilizar ambientes de teste de forma Gratuita (Até o momento de 11/2025).

Para que você consiga acessar o ambiente, você precisa primeiro fazer um cadastro na pagina, e da para se utilizar apenas do Acesso do Google mesmo, é bem simples.

- Link para acesso: [Cisco SandBox](https://developer.cisco.com/site/sandbox/)

<p align="center">
  <h1><p align="center">  Cisco Developer Sandbox!🚀</p></h1>
  <p align="center"> <img src="https://github.com/ozumaru/CiscoDevNet---Python/blob/master/Documents/img/inicialSandBox.png" width="700">
</p>

E ao realizar o acesso, você ira clicar em "Launch Sandbox ↗" para ser direcionado ao Sandbox, bem no centro da pagina em AZUL.

<p align="center">
  <h1><p align="center">  Area da Caixa de Areia 'Sandbox'!🛝</p></h1>
  <p align="center"> <img src="https://github.com/ozumaru/CiscoDevNet---Python/blob/master/Documents/img/Sandbox.png" width="700">
</p>

Aqui já vemos uma grande quantidade de Devices e Plataformas disponiveis para serem utilizados, porem há alguns padrões para serem utilizados.
Ai temos dois status:
- 'Reservable': É preciso agendar para ser utilizado, acredito por ser uma plataforma que exija muito processamento de uma ambiente virtual, não está tão aberto assim para uso rapido, em alguns casos está até mesmo bloqueado para ser utilizado, pois já está em uso.
- 'Always-On': Pode-se instanciar o device a qualquer momento, e pode programar o tempo que esse device vai permanecer ativo em seu usuario, o tempo padrão é de 2 dias.

O que vamos utilizar aqui é o 'Catalyst 9000 Always-On', ai seguimos os passos abaixo:

Em "Labels" > Always On
<p align="center"> 
  <p align="center"> <img src="https://github.com/ozumaru/CiscoDevNet---Python/blob/master/Documents/img/always_on_gif.gif" width="500">
</p>

Após a filtragem 