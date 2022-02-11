from netmiko import ConnectHandler
from time import sleep

print('\n\tConfiguração de Ponto-a-Ponto entre Devices\n')
sleep(2)
user = 'cisco'
userpass = 'cisco'

print('Endereços de acessos dos Devices')
ip = [input('\tInserir Primeiro IP: '), input('\tInserir Segundo IP: ')]

print('\nEndereço de Rede do Ponto a Ponto')
p2p = [input('\tInsira IP de Rede para Ponto-a-Ponto: '), '255.255.255.252']

print('\nInterface dos Devices que serão Configuradas')
ether1 = input('\tQual é a interface 1º Device: ')
ether2 = input('\tQual é a interface 2º Device: ')
print(' ')

for x in range(len(ip)):
    cisco_router = {
        'device_type': 'cisco_ios',
        'host': ip[x],
        'username': user,
        'password': userpass,
        'secret': userpass,
        'port': 22,
    }

    ssh = ConnectHandler(**cisco_router)
    ssh.enable()
    
    ipp2psplit = p2p[0].split('.') 
    qo = int(ipp2psplit[3]) 
    ipp2psplit[3] = str(qo+1)
    p2p[0] = '.'.join(ipp2psplit)

    n = x+1
    nome = ssh.send_command('show running | include hostname')
    nome = nome.split()

    if x == 0:
        confP2P = (f'interface Ethernet {ether1}', f'description P2P', f'ip add {p2p[0]} {p2p[1]}', 'no shutdown')
    elif x == 1:
        confP2P = (f'interface Ethernet {ether2}', f'description P2P', f'ip add {p2p[0]} {p2p[1]}', 'no shutdown')

    interface = ssh.send_config_set(confP2P)

    print(f'{n}º: {nome[1]}', end = ' ')
    sleep(2)
    print('Pronto!')

    if x == 1:
        print(f'\n\tIniciando Validação de Ping')
        ipp2psplit = p2p[0].split('.')  
        qo = int(ipp2psplit[3])  
        ipp2psplit[3] = str(qo - 1)
        p2p[0] = '.'.join(ipp2psplit)
        ping = ssh.send_command(f'ping {p2p[0]}')
        print(f'\n{ping}')

    ssh.exit_enable_mode()

print('Concluido!')
