#Criando um Loop usando dois IP em uma variavel Lista para acessar 2 equipamento

from netmiko import ConnectHandler
from datetime import datetime

now = datetime.today().strftime('%d-%m-%Y_%Hh%Mm')

#Variavel 'n' para fazer contagem de elementos a cada loop
n = 0

user = 'cisco'
userpass = 'cisco'

#Foi adicionado uma Lista contendo dois Indices e em cada Indice um IP Address.
hosts = ['192.168.10.192', '192.168.10.80']

#Identado todo o codigo colocado dentro de um Loop FOR.
#Criado a variavel contadora 'y' para que a cada volta no Loop seja a posição do Indice dentro da Lista 'hosts'
for y in range(len(hosts)):
    cisco_router = {
        'device_type': 'cisco_ios',
        #O Valor da Chave 'host' será a variavel 'hosts[na posição de 'y' dentro da lista 'hosts']
        'host': hosts[y],
        'username': user,
        'password': userpass,
        'secret': userpass,
        'port': 22,
    }

    ssh = ConnectHandler(**cisco_router)
    ssh.enable()

    config = ssh.send_command('show running')
    ssh.exit_enable_mode()
    running = (config).split()

    for x in range(len(running)):
        if 'hostname' == running[x]:
            hostname = running[x+1]

    arq = open(f'coleta\ {hostname} - {now}.txt', 'w')
    arq.write(config)
    arq.close()

    #Colocado o Print que mostra o nome dos hosts com base em cada volta da executção do programa.
    n = n+1 #Contagem de devices
    print(f'O {n}º Device é: {hostname}')

print('='*20)
print('Concluido!')





