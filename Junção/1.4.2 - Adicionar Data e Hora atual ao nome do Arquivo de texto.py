#Junção: Usando data e hora atual para adicionar ao nome do Arquivo

from netmiko import ConnectHandler

#Utilizando da Biblioteca para trazer informação de Data e Hora do Sistema.
from datetime import datetime

#Variavel contendo a informação formatada de Dia-Mês-Ano_HoraMinuto.
now = datetime.today().strftime('%d-%m-%Y_%Hh%Mm')

user = 'cisco'
userpass = 'cisco'
host = '192.168.10.192'

cisco_router = {
    'device_type': 'cisco_ios',
    'host': host,
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

#Na hora da criação do Arquivo de Texto, foi adionado a variavel 'now' para complementar o nome do Arquivo e ter a informação de quando foi feito esse backup.
arq = open(f'coleta\ {hostname} - {now}.txt', 'w')
arq.write(config)
arq.close()

print (f'O nome do Device e: {hostname}')
print ('='*20)
print ('Concluido!')





