from netmiko import ConnectHandler
from datetime import datetime

now = datetime.today().strftime('%d-%m-%Y_%Hh%Mm')

n = 0
user = 'cisco'
userpass = 'cisco'
arquivo = open("lista\ip.txt")

addr = arquivo.readlines()
for linha in addr:
    ip = linha 
    cisco_router = {
        'device_type': 'cisco_ios',
        'host': ip, 
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
