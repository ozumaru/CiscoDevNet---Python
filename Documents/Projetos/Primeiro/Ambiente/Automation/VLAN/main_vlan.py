# Importando as bibliotecas necessárias
from Automation.Instance.instances import function_default
from Automation.Instance.credentials import device_info
from datetime import datetime

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

# Loop para cada host na lista
for host in list_host:
    hostname = ""

    # Realizando Backup Antes de iniciar configuração
    backup_antes = default.access_collect(host, device_info, commando=["show running-config"])
    
    # DEPOIS ESSE PARA EXPLICAR COMPREENSÃO DE LISTAS
    hostname = next(name.split()[1] for name in backup_antes.split("\n") if name.startswith("hostname"))

    # Criando o arquivo de coleta com o nome do hostname e data/hora - ANTES 
    with open(f'Data\{hostname}_{now}_antes.txt', 'w') as arq:
        arq.write(backup_antes)
        arq.close()

    # Adicionando print para informar criação do arquivo
    print(f"Criado coleta Inicial: {hostname}_{now}_antes.txt")

    # Loop para criação de configuração e aplicação de configs
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
