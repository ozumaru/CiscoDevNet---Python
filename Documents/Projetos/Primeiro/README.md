<p align="center">
  <h2><p align="center">BACKUP/ INTERFACE/ VLAN</p></h2>
</p>

Esse projeto já é focado em mostrar como se é realizado três importantes tarefas, porem como se estive-se tendo uma demanda que utiliza um Gerenciador de Atividades: Trello para fazer com que fica-se proximo a um ambiente de produtividade.

As três tarefas que foram propostas aqui foram:
 - 1° Criação de Rotina de Backup
 - 2° Criar um Relatório de status de interfaces
 - 3° Automatizar a criação de VLANS em Switchs Cisco

E conforme esses codigos foram evoluindo, se é feito a Refatoração do código, que nesse caso é:
  - Fazer a criação de Tarefas que se repetem em outros scripts
    - Acesso ao Device e Coleta de Informação
  - Tratar output de interface para criar um Json com as informações das interface
    - Tratando diversos tipos de interfaces: GigabitEthernet, Loopback, Interface Vlan
  - Aplicação de configuração no Geral

E a ideia aqui no terceiro exercicio foi, além de configurar a Vlan, se é feito a coleta de Antes e Depois da atividade.
Isso mostra como transformar centenas de linhas, em algo mais enxuto e legivel, isso entra muito na ideia da Refatoração do Codigo.

Eu sei que é bonito ver um codigo Gigantesco cheio de linha que nós construimos, mas depois para fazer a manipulação caso necessário se torna exaustivo dependendo de quantas vezes tenhamos que arrumar.
E a Refatoração entra justamente nisso, para simplificar o codigo, e que ele seja Reutilizavel em outras etapas do Programa.

Sigamos para a Tarefa:
 - [Rotina de BACKUP](https://github.com/ozumaru/CiscoDevNet---Python/tree/master/Documents/Projetos/Primeiro/Ambiente/Automation/BACKUP/main_backup.md) - Videos: [Parte 1](https://www.youtube.com/watch?v=vY-c34QwUiY) \ [Parte 2](https://www.youtube.com/watch?v=KFq3nfDjUY8) \ [Parte 3](https://www.youtube.com/watch?v=Gvr0oQE7o6M)
 - [Relatório de INTERFACE](https://github.com/ozumaru/CiscoDevNet---Python/tree/master/Documents/Projetos/Primeiro/Ambiente/Automation/INTERFACE/main_interface.md) - Videos: [Parte 1](https://www.youtube.com/watch?v=NHoNt21UnJs) \ [Parte 2](https://www.youtube.com/watch?v=d-3HldELBnM) \ [Parte 3](https://www.youtube.com/watch?v=Hl1G6pDfuDA) \ [Parte 4](https://www.youtube.com/watch?v=kl-Lj_iU0VY)
 - [Aplicação de Configuração - Criação de Vlans](https://github.com/ozumaru/CiscoDevNet---Python/tree/master/Documents/Projetos/Primeiro/Ambiente/Automation/VLAN/main_vlan.md) - Videos: !!! ⚠️EM PRODUÇÂO 🎥 !!!

E todas as farefas, fazem consulta de Intancias, nesse caso é uma Classe agrupa Funções.
 - [Instancias](https://github.com/ozumaru/CiscoDevNet---Python/tree/master/Documents/Projetos/Primeiro/Ambiente/Automation/Instance/instances.md)

Link para Fluxograma para exemplificar o funcionamento de cada tarefa busca informação na Instancia.
 - [Fluxograma](https://github.com/ozumaru/CiscoDevNet---Python/tree/master/Documents/Projetos/Primeiro/Ambiente/Automation/README.md)

Retornar para:
- [Projetos](https://github.com/ozumaru/CiscoDevNet---Python/tree/master/Documents/Projetos)
- [Perfil Inicial](https://github.com/ozumaru)

---
Por favor, tenham curiosidade, e qualquer coisa, e fiquem a vontade em chamar no LinkedIn:   
<div style="display: inline_block"><br>
  <a href="https://www.linkedin.com/in/jose-osmar-caitano/" target="_blank"><img src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white" target="_blank"></a>  
</div>