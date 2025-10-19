from netmiko import ConnectHandler

def umdevice (ip):
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

    interface = ssh.send_config_set(confLoop)
    showl = ssh.send_command(f'show ip interface brief | include Loopback{loopback[0]}')

    print(f'{nome[1]} - {showl}')

    ssh.disconnect()

def lista (arquivo):
    addr = arquivo.readlines()
    for linha in range(len(addr)):
        ip = addr[linha]
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
 
        n = linha+1                         
        iplsplit = loopback[2].split('.')   
        iplsplit[3] = str(n)                
        ipljoin = '.'.join(iplsplit)        

        confLoop = (f'interface loopback {loopback[0]}',
                    f'description {loopback[1]}',
                    f'ip add {ipljoin} {loopback[3]}')

        interface = ssh.send_config_set(confLoop)
        showl = ssh.send_command(f'show ip interface brief | include Loopback{loopback[0]}')

        print(f'{n}º: {nome[1]} - {showl}')

        ssh.exit_enable_mode()

user = 'cisco'
userpass = 'cisco'
verificar = int(input('Você deseja Criar Loopback: \n\t1) Um Device \n\t2) Usar uma Lista de Ips \nR:'))
print('\n')

if verificar == 1:
    ip = input('Inserir IP de acesso: ') 
    loopback = [int(input('Numero da Loopback: ')),
                input('Description: '),
                input('Endereço IP: '),
                input('Mascara de SubRede: ')]
    print('\n')
    umdevice(ip)

elif verificar == 2:
    arquivo = open("lista\ip.txt") 
    loopback = [int(input('Numero da Loopback: ')),
                input('Description: '),
                input('IP de Rede: '),
                input('Mascara de SubRede: ')]
    print('\n')
    lista(arquivo)

print('Concluido!')
