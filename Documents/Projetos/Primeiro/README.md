<p align="center">
  <h2><p align="center">BACKUP/ INTERFACE/ VLAN</p></h2>
</p>

Esse projeto tem com objetivo: 
 - Criar uma Rotina de Backup
 - Retornar um Relatório de Status de Interfaces
 - Aplicar configuração de Vlans

O Ambiente que vamos utilizar é o Cisco Sandbox, uma iniciativa da Cisco para Incentivar pessoas a aprender mais sobre Programabilidade de Infraestrutura, e utilizar ambientes de teste de forma Gratuita (Até o momento de 11/2025).

Para que você consiga acessar o ambiente, você precisa primeiro fazer um cadastro na pagina, e da para se utilizar apenas do Acesso do Google mesmo, é bem simples.

- Link para acesso: [Cisco SandBox](https://developer.cisco.com/site/sandbox/)

<p align="center">
  <h2><p align="center">  Cisco Developer Sandbox!🚀</p></h2>
  <p align="center"> <img src="https://github.com/ozumaru/CiscoDevNet---Python/blob/master/Documents/img/inicialSandBox.png" width="700">
</p>

E ao realizar o acesso, você ira clicar em "Launch Sandbox ↗" para ser direcionado ao Sandbox, bem no centro da pagina em AZUL.

<p align="center">
  <h2><p align="center">  Area da Caixa de Areia 'Sandbox'!🛝</p></h2>
  <p align="center"> <img src="https://github.com/ozumaru/CiscoDevNet---Python/blob/master/Documents/img/Sandbox.png" width="700">
</p>

Aqui já vemos uma grande quantidade de Devices e Plataformas disponiveis para serem utilizados, porem há alguns padrões para serem utilizados.
Ai temos dois status:
- '**Reservable**': É preciso agendar para ser utilizado, acredito por ser uma plataforma que exija muito processamento de uma ambiente virtual, não está tão aberto assim para uso rapido, em alguns casos está até mesmo bloqueado para ser utilizado, pois já está em uso.
- '**Always-On**': Pode-se instanciar o device a qualquer momento, e pode programar o tempo que esse device vai permanecer ativo em seu usuario, o tempo padrão é de 2 dias.

O que vamos utilizar aqui é o 'Catalyst 9000 Always-On', ai seguimos os passos abaixo:

Em "Labels" > Always On
<p align="center"> 
  <p align="center"> <img src="https://github.com/ozumaru/CiscoDevNet---Python/blob/master/Documents/img/always_on_gif.gif" width="500">
</p>

Após a filtragem, no device **Catalyst 9000 Always-On Sandbox**, Click em: "🚀 Launch" > "Review Summary" > "Launch Enviroment"
E em alguns minutos o seu device já está instanciado na plataforma pronto para uso com Usuario e senha que foram gerados para você.

<p align="center"> 
  <p align="center"> <img src="https://github.com/ozumaru/CiscoDevNet---Python/blob/master/Documents/img/start_c9k.gif" width="700">
</p>

E conforme abaixo, o device já pronto para uso, e na marcação em vermelho, consta Caminho de Acesso do Device, Usuario e Senha.

<p align="center"> 
  <p align="center"> <img src="https://github.com/ozumaru/CiscoDevNet---Python/blob/master/Documents/img/instancia_c9k.gif" width="700">
</p>

Pronto, device já instanciado, tudo no jeito? ainda estamos em processo de preparar o ambiente, e testar ele também faz parte, e para validar a conectividade, podemos utilizar uma ferramenta de acesso muito conhecida entre o povo de redes, é o famoso Putty, ele é um terminal de acesso que utiliza portas logica para comunicação com Servidores Linux ou equipamentos de infra **Router/ Switch, Firewall, Load Balancers**...

Segue o link de Download, ele nem precisa ser instalado, ele é Portatil.

 - Link: [Putty](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html)

Você escolhe a com base na versão do seu sistema, os de hoje em dia geralmente é de 64-bit, ao clicar, ele já baixa e está pronto para uso.
<p align="center"> 
  <p align="center"> <img src="https://github.com/ozumaru/CiscoDevNet---Python/blob/master/Documents/img/putty_page.png" width="700">
</p>

E essa é a interface dele:
<p align="center"> 
  <p align="center"> <img src="https://github.com/ozumaru/CiscoDevNet---Python/blob/master/Documents/img/int_putty.png" width="400">
</p>    

Para realizar o teste é simples, passe o mouse no hostname do site, e clica no quadrado a frente do nome que já copia, e colocamos o Hostname do device no Putty no espaço Host, já está na porta 22 de acesso SSH (Secure Shell), e clique em "Open".
Após a abertura do Terminal, copiar o Usuario e colar no terminal, Enter, logo em seguida faça o mesmo com a senha conforme abaixo:
<p align="center"> 
  <p align="center"> <img src="https://github.com/ozumaru/CiscoDevNet---Python/blob/master/Documents/img/access_device.gif" width="700">
</p>