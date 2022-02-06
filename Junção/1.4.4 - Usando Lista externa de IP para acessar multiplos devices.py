#Usando arquivo de texto com Lista de IP para acessar maiores quantidades de Devices

from netmiko import ConnectHandler
from datetime import datetime

now = datetime.today().strftime('%d-%m-%Y_%Hh%Mm')
n = 0

user = 'cisco'
userpass = 'cisco'

#Adicionado a variavel 'arquivo' para abrir o arquivo de texto contendo lista de IP address.
arquivo = open("lista\ip.txt")

#A Lista 'addr' ira receber a informação do arquivo em forma de Lista, separando informação por indices.
addr = arquivo.readlines()

#O FOR tem a Variavel contadora 'linha' para ser o conteudo de cada Indice (Ao em vez de ser o Indice).
for linha in addr:
    ip = linha # A variavel 'ip' receberá o conteudo da variavel 'linha' a cada volta no loop, receberá uma nova informação.
    cisco_router = {
        'device_type': 'cisco_ios',
        'host': ip, #Chave 'host' tem a variavel 'ip' como Valor para acessar cada elemento em cada volta do loop FOR.
        'username': user,
        'password': userpass,
        'secret': userpass,
        'port': 22,
    }

    ssh = ConnectHandler(**cisco_router)
    ssh.enable()

    config = ssh.send_command('show running')

    running = config.split()

    for x in range(len(running)):
        if 'hostname' == running[x]:
            hostname = running[x+1]

    arq = open(f'coleta\ {hostname} - {now}.txt', 'w')
    arq.write(config)
    arq.close()

    n = n+1
    ssh.exit_enable_mode()

    print(f'O {n}º Device é: {hostname}')

print('='*20)
print('Concluido!')