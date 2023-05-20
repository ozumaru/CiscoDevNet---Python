# -*- coding: iso-8859-1 -*-
# -*- coding: utf-8 -*-

import csv

device = []
ip_device = []
input_port = []
outgoing_port = []

cdp = []

for a in range(1, 6):
    device.append(f"Sw-{a}")
for b in range(1, 6):
    ip_device.append(f"{b}.{b}.{b}.{b}")
for c in range(1, 6):
    input_port.append(f"Gi1/{c}")
for d in range(1, 6):
    outgoing_port.append(f"Gi1/{d}")

for device, ip_device, input_port, outgoing_port in zip(device, ip_device, input_port, outgoing_port):
    coleta = {"Device":device, "IP":ip_device, "Input_Port":input_port, "Outgoing_Port":outgoing_port}
    cdp.append(coleta)
    
    with open("Export_CDP.csv", mode="w", newline="", encoding="utf-8") as arquivo_csv:
        colunas = csv.writer(arquivo_csv, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        colunas.writerow(
                         ["Device", 
                          "IP", 
                          "Input_Port", 
                          "Outgoing_Port"]
                         )
        
        for equipamento in cdp:
            colunas.writerow(
                             [equipamento["Device"],
                              equipamento["IP"],
                              equipamento["Input_Port"],
                              equipamento["Outgoing_Port"]]
                             )
