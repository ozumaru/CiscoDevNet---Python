# Importando as bibliotecas necessárias
from Automation.Instance.instances import function_default
from Automation.Instance.credentials import device_info
from datetime import datetime
import csv, os

# Instanciando a classe
default = function_default()

# Coletando data e hora para nome do arquivo
now = datetime.today().strftime('%d-%m-%Y_%Hh%Mm')

# Abrindo o arquivo com a lista de hosts
list_host = open("..\hosts")

# Inicializando dicionários
get_interface = {}
hostname_interface = {}

# Loop para cada host na lista
for host in list_host:

    # Definindo lista de comandos
    commando = ["show running-config | include hostname", "show ip interface brief"]

    cisco = default.access_collect(host, device_info, commando)
    # print(cisco)
    
    # Convertendo a coleta em uma lista
    lista_cisco = cisco.split("\n") 

    # Extraindo o hostname da coleta
    hostname = lista_cisco[0].split()[1]

    # Tratando coleta de status de interface
    for interface in lista_cisco:
        # Tratando linhas de interfaces: GigabitEthernet, FastEthernet, etc
        get_interface = default.get_interface_function(get_interface, interface) 

    # Criando dicionário com hostname e suas interfaces
    hostname_interface[hostname] = get_interface 

    # Criando o Arquivo de coleta
    output_file = "interfaces.csv"
    header = ["Hostname", "Interface", "IP-Address", "Status", "Protocol"]

    # Verifica se o arquivo já existe
    file_exists = os.path.exists(output_file)

    # Se existir, carrega conteúdo pra evitar duplicatas
    existing_rows = []
    if file_exists:
        with open(output_file, newline="") as csvfile:
            reader = csv.reader(csvfile)
            next(reader, None)  # Pula o cabeçalho (se houver)
            existing_rows = [row for row in reader]
     
    # Abre o arquivo para append (sem apagar conteúdo existente)
    with open(output_file, mode="a", newline="") as csvfile:
        writer = csv.writer(csvfile)

        # Escreve o cabeçalho apenas se o arquivo for novo
        if not file_exists:
            writer.writerow(header)

        # Percorre cada hostname e suas interfaces
        for hostname, interfaces in hostname_interface.items():
            for intf, info in interfaces.items():
                new_row = [
                    hostname,
                    intf,
                    info["address"],
                    info["status"],
                    info["protocol"],
                ]

                # Evita duplicar linha já existente (hostname + interface)
                duplicate_found = False
                for row in existing_rows:
                    if row[0] == hostname and row[1] == intf:
                        duplicate_found = True
                        break

                # Escreve a nova linha se não for duplicata
                if not duplicate_found:
                    writer.writerow(new_row)
