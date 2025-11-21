from Automation.Instance.instances import function_default
from Automation.Instance.credentials import device_info
from datetime import datetime

# Instanciando a classe
default = function_default()

# Coletando data e hora para nome do arquivo
now = datetime.today().strftime('%d-%m-%Y_%Hh%Mm')

# Abrindo o arquivo com a lista de hosts
list_host = open("..\hosts")

# Loop para cada host na lista
for host in list_host: 
    # Definindo lista de comandos
    commando = ["show running-config"]

    # Realizando a coleta do running-config
    cisco = default.access_collect(host, device_info, commando) 
    
    # convertendo a coleta em uma lista
    lista_cisco = cisco.split("\n")
    
    # Extraindo o hostname da coleta com compreensão de listas
    hostname = next(name.split()[1] for name in lista_cisco if name.startswith("hostname"))

    # Criando o arquivo de coleta com o nome do hostname e data/hora
    with open(f'Data\{hostname}_{now}.txt', 'w') as arq:
        arq.write(cisco)
        arq.close()