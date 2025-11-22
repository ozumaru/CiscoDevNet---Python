from Automation.Instance.instances import function_default
from Automation.Instance.credentials import device_info
from datetime import datetime

default = function_default()

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

now = datetime.today().strftime('%d-%m-%Y_%Hh%Mm')

list_host = open("..\hosts")

for host in list_host:
    hostname = ""

    backup_antes = default.access_collect(host, device_info, commando=["show running-config"])
    
    hostname = next(name.split()[1] for name in backup_antes.split("\n") if name.startswith("hostname"))

    with open(f'Data\{hostname}_{now}_antes.txt', 'w') as arq:
        arq.write(backup_antes)
        arq.close()

    print(f"Criado coleta Inicial: {hostname}_{now}_antes.txt")

    commando = []
    for x, name in zip(range(5, 55, 5), name_vlan):
        commando.extend([
            f"vlan {x}",
            f"name {name}",
            "!"
        ])
    
    cisco = default.send_config_default(host, device_info, commando)

    print(f"Aplicado a configuação da lista de Vlans: {list(zip(range(5, 55, 5), name_vlan))} ")

    backup_depois = default.access_collect(host, device_info, commando=["show running-config"])

    with open(f'Data\{hostname}_{now}_depois.txt', 'w') as arq:
        arq.write(backup_depois)
        arq.close()

    print(f"Criado coleta Final: {hostname}_{now}_depois.txt")
