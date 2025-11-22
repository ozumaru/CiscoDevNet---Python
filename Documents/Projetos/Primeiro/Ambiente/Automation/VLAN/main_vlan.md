<p align="center">
  <h1><p align="center">Aplicando configuração de VLAN</p></h1> 
</p>

Abaixo importamos a instancia criada para algoritimos repetitivos, conforme no arquivo [instances](https://github.com/ozumaru/CiscoDevNet---Python/blob/master/Documents/Projetos/Primeiro/Ambiente/Automation/Instance/instances.md), abaixo está a forma de se invocar a classe **function_default**, e está nesse formato pois **Automation.Instance.** é o Caminho do diretorio onde essa classe se encontra, juntamente sendo invocando também informações de [credentials](https://github.com/ozumaru/CiscoDevNet---Python/blob/master/Documents/Projetos/Primeiro/Ambiente/Automation/Instance/credentials.py) de acesso em formato de Tupla.

Também importando a biblioteca **datetime** para se criar uma parametro de tempo ao criar o arquivo de backup.
```Python
# Importando as bibliotecas necessárias
from Automation.Instance.instances import function_default
from Automation.Instance.credentials import device_info
from datetime import datetime
```
---
- **default**: O seguinte trecho faz a invocação das funções da Classe **function_default** na função nomeada como **default** podendo utilizar todas as funções que existem dentro da classe.

- **name_vlan**: Lista que contem um total de 10 nomes de função para cada Vlan no ambiente de infraestrtura

- **now**: A variavel **NOW** ira armazenar a data do sistema para ter como parametrô na criação do nome do arquivo de backup, dessa forma não sendo sobrescrito e de fato criar uma rotina de backup.

- **Hosts**: O Arquivo [hosts](https://github.com/ozumaru/CiscoDevNet---Python/blob/master/Documents/Projetos/Primeiro/Ambiente/Automation/hosts) possui a lista de acesso aos devices, no caso de um ambiente com multiplos devices, é nesse arquivo que será armazenado os endereço de acesso, sempre linha por linha.
```Python
# Instanciando a classe
default = function_default()

# Definindo nomes das Vlans
name_vlan = [
    "CABLE",
    "WIRELESS",
    "VOICE",
    "CAMERA",
    "PRINTER",
    "USER",
    "GUEST",
    "EVENT",
    "ACCESS",
    "DISTRIBUTION",
    ]

# Coletando data e hora para nome do arquivo
now = datetime.today().strftime('%d-%m-%Y_%Hh%Mm')

# Abrindo o arquivo com a lista de hosts
list_host = open("..\hosts")
```
---
```Python
# Loop para cada host na lista
for host in list_host:
    hostname = ""

    # Realizando Backup Antes de iniciar configuração
    backup_antes = default.access_collect(host, device_info, commando=["show running-config"])
    
    # Extraindo o hostname da coleta com compreensão de listas
    hostname = next(name.split()[1] for name in backup_antes.split("\n") if name.startswith("hostname"))

    # Criando o arquivo de coleta com o nome do hostname e data/hora - ANTES 
    with open(f'Data\{hostname}_{now}_antes.txt', 'w') as arq:
        arq.write(backup_antes)
        arq.close()

    # Adicionando print para informar criação do arquivo
    print(f"Criado coleta Inicial: {hostname}_{now}_antes.txt")

    # Loop para criação de configuração e aplicação de configs
    # Contem dois valores de saida "x, name" e dois valores em zip (O range numérico com saltos de 5) e a lista contendo o nome das Vlans.
    commando = []
    for x, name in zip(range(5, 55, 5), name_vlan):
        commando.extend([
            f"vlan {x}",
            f"name {name}",
            "!"
        ])
    
    # Enviando configuração de Vlans
    cisco = default.send_config_default(host, device_info, commando)

    # Print para informar aplicação de configuração
    print(f"Aplicado a configuação da lista de Vlans: {list(zip(range(5, 55, 5), name_vlan))} ")

    # Realizando Backup Antes de iniciar configuração
    backup_depois = default.access_collect(host, device_info, commando=["show running-config"])

    # Criando o arquivo de coleta com o nome do hostname e data/hora - DEPOIS
    with open(f'Data\{hostname}_{now}_depois.txt', 'w') as arq:
        arq.write(backup_depois)
        arq.close()

    # Adicionando print para informar criação do arquivo
    print(f"Criado coleta Final: {hostname}_{now}_depois.txt")
```
Links essenciais:
\
Script Limpo: [main_vlan](https://github.com/ozumaru/CiscoDevNet---Python/blob/master/Documents/Projetos/Primeiro/Ambiente/Automation/VLAN/main_vlan.py)
\
Inicio do Projeto: [Inicio](https://github.com/ozumaru/CiscoDevNet---Python/blob/master/Documents/Projetos/Primeiro)
\
Video de Exeplicação: ⚠️ !!! EM PRODUÇÃO !!! ⚙️