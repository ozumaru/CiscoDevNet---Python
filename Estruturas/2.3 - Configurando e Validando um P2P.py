from netmiko import ConnectHandler
from time import sleep

'''
O Intuito do programa é Configurar um Ponto-a-Ponto em duas Caixas com Gerencias 
já existentes.

E Realizar Ping do Segundo para o Primeiro Device, pois ao entrar no Loop For.
    - Ira acessar o Primeiro Device, Acessar a Interface (Já tento as devidas 
    informações previamente fornecidas)
    - Configurar: Description > IP Address > Subnet-Mask e No Shutdown
'''

print('\n\tConfiguração de Ponto-a-Ponto entre Devices\n')
sleep(2)
user = 'cisco'
userpass = 'cisco'

print('Endereços de acessos dos Devices')
ip = [input('\tInserir Primeiro IP: '), input('\tInserir Segundo IP: ')]

#Lista 'p2p' ira solicitar um IP de REDE para ser configurado, tendo em vista que 
#a mesma já tem a Mascara /30 no indice 1, então será um Ponto a Ponto /30 de qualquer forma
print('\nEndereço de Rede do Ponto a Ponto')
p2p = [input('\tInsira IP de Rede para Ponto-a-Ponto: '), '255.255.255.252']

#Variaveis  'ether1 / ether2' ira solicitar a interface de Ponto-a-Ponto entre os dois Devices.
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

    #Ação ira Quebrar o IP com base nos Pontos, criando uma Lista com 4 Indices, 
    #iniciando no 0 e terminando no 3,
    ipp2psplit = p2p[0].split('.') #Variavel 'ipp2psplit' = IP P2P Split

    #Variavel 'qo' ira receber o Quarto Octeto como Numero Interiro
    qo = int(ipp2psplit[3]) #Variavel 'qo' = Quarto Octeto

    #Variavel 'ipp2psplit' ira receber no Quarto Octeto o valor de 'qo' + 1
    ipp2psplit[3] = str(qo+1)

    #Variavel 'p2p' ira receber a lista 'ipp2psplit' contatenando por Ponto, 
    #formando novamente o IP e uma Unica String
    p2p[0] = '.'.join(ipp2psplit)

    n = x+1
    nome = ssh.send_command('show running | include hostname')
    nome = nome.split()

    #Conficional IF e ELIF iram validar se o acesso está acontecendo no Primeiro ou Pegundo IP
    if x == 0:
        confP2P = (f'interface Ethernet {ether1}', f'description P2P', f'ip add {p2p[0]} {p2p[1]}', 'no shutdown')
    elif x == 1:
        confP2P = (f'interface Ethernet {ether2}', f'description P2P', f'ip add {p2p[0]} {p2p[1]}', 'no shutdown')


    #Variavel 'interface' ira enviar para ambos os Devices o comando da variavel 'confP2P', 
    #o que ira diferenciar uma da outra é o em que momendo o Loop estará acontecendo
    interface = ssh.send_config_set(confP2P)

    print(f'{n}º: {nome[1]}', end = ' ')
    sleep(2)
    print('Pronto!')

    #Condicional IF validando que o Loop está na ultima volta, ira fazer o processo 
    #inverso ao de adicionar +1 ao Quarto Octeto, para assim que o segundo Device 
    #realize um Ping para o Decice Anterior para Validade Config de ponto a ponto.
    if x == 1:
        print(f'\n\tIniciando Validação de Ping')
        ipp2psplit = p2p[0].split('.')  # Variavel 'ipp2psplit' = IP P2P Split
        qo = int(ipp2psplit[3])  # Variavel 'qo' = Quarto Octeto
        ipp2psplit[3] = str(qo - 1)
        p2p[0] = '.'.join(ipp2psplit)
        ping = ssh.send_command(f'ping {p2p[0]}')
        print(f'\n{ping}')

    ssh.exit_enable_mode()

print('Concluido!')
