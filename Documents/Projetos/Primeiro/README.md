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

O que vamos utilizar aqui é o **Catalyst 9000 Always-On**, ai seguimos os passos abaixo:

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

Segue o link de Download, nem precisa ser instalado, pois é Portatil.

 - Link: [Putty](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html)

Você escolhe a com base na versão do seu sistema, os de hoje em dia geralmente é de 64-bit, ao clicar, ele já baixa e está pronto para uso.
<p align="center"> 
  <p align="center"> <img src="https://github.com/ozumaru/CiscoDevNet---Python/blob/master/Documents/img/putty_page.png" width="700">
</p>

E essa é a interface dele:
<p align="left"> 
  <p align="left"> <img src="https://github.com/ozumaru/CiscoDevNet---Python/blob/master/Documents/img/int_putty.png" width="400">
</p>    

Para realizar o teste é simples, passe o mouse no hostname do site, e clica no quadrado a frente do nome que já copia, e colocamos o Hostname do device no Putty no espaço Host, já está na porta 22 de acesso SSH (Secure Shell), e clique em "Open".
Após a abertura do Terminal, copiar o Usuario e colar no terminal, Enter, logo em seguida faça o mesmo com a senha conforme abaixo:
<p align="center"> 
  <p align="center"> <img src="https://github.com/ozumaru/CiscoDevNet---Python/blob/master/Documents/img/access_device.gif" width="700">
</p>

Bom, device está acessivel, o ambiente já ta pronto? ainda não... vamos agora iniciar a preparação do ambiente Python.

Antes de tudo, vamos primeiro criar a estrutura de pastas das tarefas que vamos executar, e também já deixar pronto a pasta de "Instancias de Dependencias" que vamos criar.

Abaixo a Arvore de diretórios a serem utilizados:
```bash
|-- Primeiro					⇐ Diretorio Raiz
|   |-- Virtual_Enviroment		⇐ Sub_Diretorio de Ambiente Virtual
|   |-- Instance				⇐ Sub_Diretorio
|   |   `-- instances.py 		⇐ Arquivo Python
|   |-- BACKUP					⇐ Sub_Diretorio
|   |   |-- Data				⇐ Sub_Diretorio de Backup
|   |   `-- main_backup.py		⇐ Arquivo Python
|   |-- INTERFACE				⇐ Sub_Diretorio
|   |   |-- Data				⇐ Sub_Diretorio de Interface
|   |   `-- main_interface.py	⇐ Arquivo Python
|   `-- VLAN					⇐ Sub_Diretorio
|       |-- Data				⇐ Sub_Diretorio de Vlan
|       `-- vlan.py				⇐ Arquivo Python
```

Com tudo isso já feito, vamos começar com Python e Visual Code, para isso temos que ter o Python acima do 3.3 instalado, e para verificar isso, vai em iniciar > cmd > e digite o comando **python --version**
Caso não retorna, é que o python não está instalado, então siga para a pagina abaixo de download do Python: 

- [Python Download](https://www.python.org/downloads/)
<p align="left"> 
  <p align="left"> <img src="https://github.com/ozumaru/CiscoDevNet---Python/blob/master/Documents/img/python_download.gif" width="700">
</p>

Instalado o Python, caso não tenha, instale também o Visual Studio Code, já na pagina inicial mostra para fazer o Download.

- [Visual Studio Code Download](https://code.visualstudio.com/)

Após instalado essa duas ferramentas, vamos abrir o Visual Code, e vamos ativar a extensão do Python no Visual Code, conforme abaixo, no meu caso já está instalado.
Clique **Install**
<p align="left"> 
  <p align="left"> <img src="https://github.com/ozumaru/CiscoDevNet---Python/blob/master/Documents/img/vs_code_Python.gif" width="700">
</p>

<p align="center">
  <h2><p align="center">Python VENV</p></h2>
</p>
Porque é importante que o python esteja acima da versão 3.3, pois já possui Nativamente uma função chamada VENV (Virtual Environment), e porque isso é importante.

Demos o exemplo de que, você está em um ambiente de produção e precisa testar uma Biblioteca especifica do Python, porem, outros funções internas do sistema já utilizam algumas bibliotecas na versão em que estão, caso você vá diretamente e instale uma biblioteca direto no ambiente de produção, pode parar outras aplicações de funcionar.

Para evitar isso, é possivel criar Ambientes Virtuais para baixar as bibliotecas do jeito que quisermos para realizar os testes.

E conforme criamos a estrutura de diretorios acima, vamos iniciar agora o passo-a-passo para ativar o ambiente, entrar nele e vamos aprender a sair dele quando terminar a tarefa.

Para começar, no Visual Code, vamos abrir o Diretorio "Primeiro"
<p align="left"> 
  <p align="left"> <img src="https://github.com/ozumaru/CiscoDevNet---Python/blob/master/Documents/img/dir_primeiro.gif" width="700">
</p>

Vamos abrir o terminal e ai vamos começar com uns comandos, a principio, para Criar o VENV, Entrar no Ambiente, e Sair do Ambiente.
Em alguns casos pode ocorrer um erro, mas também vou explicar como passar por eles para seguir com o Lab.

Primeira parte: Abrir o terminal, e executar o comando "**python -m venv .**"
Ali tem um ponto mesmo no Comando, e para que ele serve?
É utilizado dessa forma para usar o nome da pasta como nome do ambiente, você tem 3 modos:
 - 1° python -m venv                       |Nesse modo o Ambiente vai ser criado como **venv** mesmo
 - 2° python -m venv .                     |Nesse modo vai usar o nome do diretorio Atual/Current que o terminal está aberto
 - 3° python -m venv <NOME_DO_AMBIENTE>    |Aqui você pode alterar o nome do ambiente como desejar

Ao abrir o terminal, faça o comando "cd Virtual_Enviroment" para entrar no diretorio que vai criar o ambiente 
Nota-se que ao aplicar o comando que ele cria outros arquivos:
<p align="center"> 
  <p align="center"> <img src="https://github.com/ozumaru/CiscoDevNet---Python/blob/master/Documents/img/venv.gif" width="700">
</p>

Esse é o ambiente que o python cria para que isole os seus testes do ambiente de produção.

Agora para entrar nele, você precisa executar o comando "**.\Scripts\activate**" pode ocorrer de aparece um erro de permissão mostrando o erro a baixo, para corrigir isso executar o comando a seguir:
Caso erro ocorra, vai em Iniciar > Powershell (Abrir como Admininstrador) > executar o comando: Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned

<p align="center"> 
  <p align="center"> <img src="https://github.com/ozumaru/CiscoDevNet---Python/blob/master/Documents/img/erro.png" width="1000">
</p>

Mas caso não ocorra erro, ele tem que entrar nesse modo:
<p align="center"> 
  <p align="center"> <img src="https://github.com/ozumaru/CiscoDevNet---Python/blob/master/Documents/img/in_venv.png" width="700">
</p>