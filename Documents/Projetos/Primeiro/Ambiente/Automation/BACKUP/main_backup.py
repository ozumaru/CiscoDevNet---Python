from Automation.Instance.instances import function_default
from Automation.Instance.credentials import device_info
from datetime import datetime

default = function_default()

now = datetime.today().strftime('%d-%m-%Y_%Hh%Mm')

list_host = open("..\hosts")

for host in list_host: 
    commando = ["show running-config"]

    try:
        cisco = default.access_collect(host, device_info, commando) 
        lista_cisco = cisco.split("\n")
            
        hostname = next(name.split()[1] for name in lista_cisco if name.startswith("hostname"))

        with open(f'Data\{hostname}_{now}.txt', 'w') as arq:
            arq.write(cisco)
            arq.close()
            
    except Exception as e:
        print(f"Não foi possível conectar ao host {host.strip()}. Erro: {e}")
        