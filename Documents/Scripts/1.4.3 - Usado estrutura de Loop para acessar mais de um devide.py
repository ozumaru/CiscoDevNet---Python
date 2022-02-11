from netmiko import ConnectHandler
from datetime import datetime

now = datetime.today().strftime('%d-%m-%Y_%Hh%Mm')

n = 0
user = 'cisco'
userpass = 'cisco'
hosts = ['192.168.10.192', '192.168.10.80']

for y in range(len(hosts)):
    cisco_router = {
        'device_type': 'cisco_ios',
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

    n = n+1 #Contagem de devices
    print(f'O {n}º Device é: {hostname}')

print('='*20)
print('Concluido!')
