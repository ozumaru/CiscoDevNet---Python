from Automation.Instance.instances import function_default
from Automation.Instance.credentials import device_info
from datetime import datetime
import csv, os

default = function_default()

now = datetime.today().strftime('%d-%m-%Y_%Hh%Mm')

list_host = open("..\hosts")

get_interface = {}
hostname_interface = {}

for host in list_host:

    commando = ["show running-config | include hostname", "show ip interface brief"]
    
    try:
        cisco = default.access_collect(host, device_info, commando)
        
        lista_cisco = cisco.split("\n") 

        hostname = lista_cisco[0].split()[1]

        for interface in lista_cisco:
            get_interface = default.get_interface_function(get_interface, interface) 

        hostname_interface[hostname] = get_interface 

        output_file = "interfaces.csv"
        header = ["Hostname", "Interface", "IP-Address", "Status", "Protocol"]

        file_exists = os.path.exists(output_file)

        existing_rows = []
        if file_exists:
            with open(output_file, newline="") as csvfile:
                reader = csv.reader(csvfile)
                existing_rows = [row for row in reader]
        
        with open(output_file, mode="a", newline="") as csvfile:
            writer = csv.writer(csvfile)

            if not file_exists:
                writer.writerow(header)

            for hostname, interfaces in hostname_interface.items():
                for intf, info in interfaces.items():
                    new_row = [
                        hostname,
                        intf,
                        info["address"],
                        info["status"],
                        info["protocol"],
                    ]

                    duplicate_found = False
                    for row in existing_rows:
                        if row[0] == hostname and row[1] == intf:
                            duplicate_found = True
                            break

                    if not duplicate_found:
                        writer.writerow(new_row)
                        
    except Exception as e:
        print(f"Não foi possível conectar ao host {host.strip()}. Erro: {e}")