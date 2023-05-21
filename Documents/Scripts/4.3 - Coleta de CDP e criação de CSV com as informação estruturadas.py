# -*- coding: iso-8859-1 -*-
# -*- coding: utf-8 -*-

from netmiko import ConnectHandler 
from netmiko.ssh_exception import NetMikoAuthenticationException, NetMikoTimeoutException 
from datetime import datetime 
from getpass import getpass 
import csv 

now = datetime.today().strftime('%d-%m-%Y_%Hh%Mm')

separador = ("="*63)
print(separador) 

ok = ""              
nok = ""             
arq = ""             
texto = ""           
hostname = ""        
hostname1 = ""       
discovery = ""     

address = []         
linhas = []          
device = []          
ip_device = []       
input_port = []      
outgoing_port = []   
cdp = []             

n = 0

user = input('Username: ')          
userpass = getpass('Password: ')    

arquivo = open("Local do Arquivo de IP_Address.txt") 
addr = arquivo.readlines()

for linha in addr:
    ip = linha
    cisco = {
        'device_type': 'cisco_ios',     
        'host': ip,                     
        'username': user,               
        'password': userpass,           
        'secret': userpass,             
        'port': 22,                     
        'fast_cli':False                
    } 

    try:
        with ConnectHandler(**cisco) as ssh:
            ssh.enable() 
            
            if not ssh.check_enable_mode(): 
                ssh.enable()
                
            comandos = ['show running | i hostname', 
                        'sh cdp neighbors detail | i Device ID|IP|Interface']

            for x in range(len(comandos)):
                config = ssh.send_command(comandos[x])
                linhas = config.split() 

                if x == 0:
                    for y in range(len(linhas)):      
                        if linhas[y] == "hostname":
                            hostname = linhas[y+1]
                            hostname1 = linhas[y+1]   

                elif x == 1: 
                    address = config.split()
                    for a in range(len(address)):
                       
                        if address[a] == 'Device':
                            device.append(str(address[a+2]))
                            if a > len(address):
                                continue

                    for b in range(len(address)):
                        if address[b] == 'ID:':
                            ip_device.append(str(address[b+4]))
                            if b > len(address):
                                continue
                              
                    for c in range(len(address)):
                        if address[c] == 'Interface:':
                            input_port.append(address[c+1].replace(",", ""))
                            if c > len(address):
                                continue
                                                        
                    for d in range(len(address)):
                        if address[d] == 'port):':
                            outgoing_port.append(address[d+1])
                            if d > len(address):
                                continue
                        
            for device, ip_device, input_port, outgoing_port in zip(device, ip_device, input_port, outgoing_port):
                coleta = {"hostname":hostname, "Device":device, "IP":ip_device, "Input_Port":input_port, "Outgoing_Port":outgoing_port}
                cdp.append(coleta)
                    
                with open(f"Local do diretorio de output do CSV/{hostname}_{now}.csv", mode="w", newline="", encoding="utf-8") as arquivo_csv:
                    colunas = csv.writer(arquivo_csv, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    colunas.writerow(
                                     ["hostname", 
                                      "Device", 
                                      "IP", 
                                      "Input_Port", 
                                      "Outgoing_Port"]
                                     )
                    
                    for equipamento in cdp:
                        colunas.writerow(
                                         [equipamento["hostname"],
                                          equipamento["Device"],
                                          equipamento["IP"],
                                          equipamento["Input_Port"],
                                          equipamento["Outgoing_Port"]]
                                         )

            ssh.disconnect()
            
            cdp = []
            device = []
            ip_device = []
            input_port = []
            outgoing_port = []
            
            n += 1
            print(f'{n} - Device: {hostname1}')
            ok += (f'{n} - Device: {hostname1}\n')
    
    except (NetMikoAuthenticationException, NetMikoTimeoutException):
        print('Falha de Conexao: {}'.format(cisco['host']),end="")
        nok += (f'Falha de Conexao: {ip}')
        
arq = (f"Equipamentos Acessados: \n{ok} \n{separador} \nEquipamentos sem acesso: \n{nok}")
texto = open(f'Local do diretorio de output/Conexoes_{now}.txt', 'w')
texto.write(arq)
texto.close()
   
print(separador)
print("Processo de Coleta Concluido!")
