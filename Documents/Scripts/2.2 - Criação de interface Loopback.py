from netmiko import ConnectHandler

user = 'cisco'
userpass = 'cisco'
ip = '192.168.10.11'

loopback = [int(input('Numero da Loopback: ')),
            input('Description: '),
            input('IP Valido: '),
            input('Mascara de SubRede: ')]
print('\n')

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

nome = ssh.send_command('show running | include hostname')
nome = nome.split()


confLoop = (f'interface loopback {loopback[0]}',
            f'description {loopback[1]}',
            f'ip add {loopback[2]} {loopback[3]}')

show = (f'show running interface Loopback{loopback[0]} | i desc|ip')

interface = ssh.send_config_set(confLoop)
showl = ssh.send_command(show)

ssh.exit_enable_mode()

find = showl.split()
print(f'{nome[1]} - Interface: Loopback{loopback[0]} \tIP: {find[4]} \tDescription: {find[1]}')

print('\nConcluido!')
