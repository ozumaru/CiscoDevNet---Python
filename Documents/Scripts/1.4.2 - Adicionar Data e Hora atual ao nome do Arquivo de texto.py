from netmiko import ConnectHandler
from datetime import datetime

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

ssh.disconnect()

running = (config).split()

for x in range(len(running)):
    if 'hostname' == running[x]:
        hostname = running[x+1]
arq = open(f'coleta\ {hostname} - {now}.txt', 'w')
arq.write(config)
arq.close()

print (f'O nome do Device e: {hostname}')
print ('='*20)
print ('Concluido!')
