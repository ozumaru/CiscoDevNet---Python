<p align="center"><h1><p align="center">Fluxograma de funcionamento da Automação e suas Dependencias</p></h1></p>

Abaixo um Fluxograma exemplificando o processo de cada automação do projeto, e todas estão buscando acessando [Instancias](https://github.com/ozumaru/CiscoDevNet---Python/tree/master/Documents/Projetos/Primeiro/Ambiente/Automation/Instance/instances.md) para realizar alguma ação, seja para:
 - Acessar algum device e coletar comados
 - Aplicar configuração
 - Tratar informação de Status de Interfaces
 
# Rotina de Backup - Link: [BACKUP](https://github.com/ozumaru/CiscoDevNet---Python/tree/master/Documents/Projetos/Primeiro/Ambiente/Automation/BACKUP/main_backup.md)
 - Videos: [Parte 1](https://www.youtube.com/watch?v=vY-c34QwUiY) \ [Parte 2](https://www.youtube.com/watch?v=KFq3nfDjUY8) \ [Parte 3](https://www.youtube.com/watch?v=Gvr0oQE7o6M)
```mermaid
flowchart TD
    A[Main_Backup] --> B[Automation.Instance.function_default]
    B --> C[func - access_collect]
    C --> D[Retorna: Running-config]
    D --> E[Localiza Hostname]
    E --> F[Salva Arquivo de Bakcup]
    F --> G[Fim]
```
---
# Relatório de Interfaces - Link: [INTERFACE](https://github.com/ozumaru/CiscoDevNet---Python/tree/master/Documents/Projetos/Primeiro/Ambiente/Automation/INTERFACE/main_interface.md)
 - Videos: [Parte 1](https://youtu.be/NHoNt21UnJs) \ [Parte 2](https://youtu.be/d-3HldELBnM) \ [Parte 3](https://www.youtube.com/watch?v=Hl1G6pDfuDA) \ [Parte 4](https://youtu.be/kl-Lj_iU0VY)
```mermaid
flowchart TD
    A[Main_Interface] --> B[Automation.Instance.function_default]
    B --> C[func - access_collect]
    C --> D[Retorna: show ip interface brief]
    D --> E[func - access_collectget_interface_function]
    E --> F[Cria JSON com informação de Interfaces]
    F --> G[Salva Arquivo CSV]
    G --> H[Fim]
```
---
# Configuração de VLANs - Link: [VLAN](https://github.com/ozumaru/CiscoDevNet---Python/tree/master/Documents/Projetos/Primeiro/Ambiente/Automation/VLAN/main_vlan.md)
```mermaid
flowchart TD
    A[Main_Vlan] --> B[Automation.Instance.function_default]
    B --> C[func - access_collect]
    C --> D[Coleta Backup ANTES de configurar]
    D --> E[Cria configuração de Vlans com Lista de Nomes e um Loop de contagem com saltos de 5 até 50]
    E --> F[func - send_config_default]
    F --> G[Coleta Backup DEPOIS de configurar]
    G --> H[Fim] 
```
---
Links:
\
Inicio do Projeto: [Inicio](https://github.com/ozumaru/CiscoDevNet---Python/blob/master/Documents/Projetos/Primeiro)