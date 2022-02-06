#Criando Loopback em Um ou mais Devices

from netmiko import ConnectHandler

'''
Nessa atividade foi utilizar uma ação para declarar funções, com o 'def' definimos determinada 
função para algumas das nossas ações que pode se repetir muitas vezes, e a forma para otimizar 
essa ação, e ao em vez de Reescrever elas muitas vezes quando precisamos, definimos uma função, 
e a chamamos quantas vezes forem preciso.

O exemplo dessa atividade é para declarar interfaces Loopback usando somente Um IP de acesso,
assim acessando somente Um equipamento, ou utilizando uma Lista de IPs, e assim configurando 
uma só range em multiplos Equipamentos, só que sem fazer com que o IP Repita para outro 
dispositivo e evitando o Overlap (IP Duplicado na rede).

Quando se é declarado mais de uma função dentro de um script, elas não precisam ter uma terminara ordem
a ser seguida, a ordem só será valida no momento em que a Função for Necessária para a ação do scritp.
'''

#Função 'umdevice' ira utilizar o argumento 'ip' com a informação que será inserida pelo usuario,
#que será adicionado dentro de um Valor da Chave 'host' do dicionário 'cisco_router'.
#e assim seguindo o fluxo de criação da Loopback.
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

    #Lista 'confLoop' ira receber as 3 informações que serão pedidas ao usuario na Condição 'IF'.
    confLoop = (f'interface loopback {loopback[0]}', #O numero da Loopback
                f'description {loopback[1]}', #Uma descrição
                f'ip add {loopback[2]} {loopback[3]}') #E o Endereço IP

    #Variavel 'interface' tem com função enviar esses comandos para o device
    interface = ssh.send_config_set(confLoop)

    #Variavel 'showl = show Loopback' ira enviar o comando para verificar somente o status da 
    #interface que foi criada 
    showl = ssh.send_command(f'show ip interface brief | include Loopback{loopback[0]}')

    #Concluindo ação mostrando o hostname do Equipamento e o status da nova interface.
    print(f'{nome[1]} - {showl}')

    ssh.exit_enable_mode()


#A função 'lista' tem semelhanças a a função 'umdevice', porem, ao em vez do argumento ser 'ip'
#é 'arquivo', sendo que já na conficional 'elif' o arquivo de texto contendo os IPs de cada elemento
#que será acessado para criar uma loopback.
def lista (arquivo):
    #A Variavel 'addr' ao ler o todas as informações da variavel 'arquivo', ira ser verificado 
    #no loop 'FOR' quantos Indices tem na variavel, e a cada Indice, uma volta no loop tem que ser feito.
    addr = arquivo.readlines()

    #Utilizado a variavel contadora 'linha' verificando o indice de 'addr'
    for linha in range(len(addr)):
        #A Variavel 'ip' ira se tornar a informação de 'addr' na posição do indice adicionado em 'linha'
        ip = addr[linha]
        cisco_router = {
            'device_type': 'cisco_ios',
            'host': ip, #E adicionando a variavel 'ip' como o Valor da Chave 'host' do dicionario 'cisco_router'
            'username': user,
            'password': userpass,
            'secret': userpass,
            'port': 22,
        }
        ssh = ConnectHandler(**cisco_router)
        ssh.enable()

        nome = ssh.send_command('show running | include hostname')
        nome = nome.split()

        '''
        Essa é a etapa em que a Cada volta no loop 'FOR', será adicionado mais um numero ao Quarto Octeto
        do IP da Loopback.
        
        Sendo dividido em partes

        1 - Criado a variavel 'n' para receber o numero do volta do Loop + 1, pois o indice começa em 0
        2 - Localizar o IP no indice 2 da lista 'Loopback' e quebrar a Strig do IP com base nos Pontos, 
            e adicionar informação quebrada dentro da lista 'iplsplit'. 
            Exemplo: iplsplit = ['192','168','10','0']
        
        3 - Substituir a informação da Lista 'iplsplit' na posição do indice 3 (O Quarto Octeto) para o
            Numero da variavel 'n'.
            Exemplo: iplsplit = ['192','168','10','n']
        
        4 - Criado a variavel 'ipljoin' para juntar a lista 'iplsplit' e uma unica String
            Exemplo: ipljoin = ('192.168.10.n')
        '''
        n = linha+1                         #1
        iplsplit = loopback[2].split('.')   #2 iplsplit = IP Loopback Split
        iplsplit[3] = str(n)                #3
        ipljoin = '.'.join(iplsplit)        #4 ipljoin = IP Loopack Join

        #Lista 'confLoop' ira receber as informações fornecidas pelo usuario
        #Mais a variavel 'ipljoin' com o IP alterado condição 'ELIF'.
        confLoop = (f'interface loopback {loopback[0]}',
                    f'description {loopback[1]}',
                    f'ip add {ipljoin} {loopback[3]}')

        #Variavel 'interface' tem com função enviar esses comandos para o device
        interface = ssh.send_config_set(confLoop)

        #Variavel 'showl = show Loopback' ira enviar o comando para verificar somente o status da 
        #interface que foi criada 
        showl = ssh.send_command(f'show ip interface brief | include Loopback{loopback[0]}')

        #Concluindo ação mostrando a ordem de configuração e hostname do Equipamento 
        #e o status da nova interface.
        print(f'{n}º: {nome[1]} - {showl}')

        ssh.exit_enable_mode()

user = 'cisco'
userpass = 'cisco'

#A variavel 'verificar' vai questionar o Usuario o que será feito dado 2  opções.
verificar = int(input('Você deseja Criar Loopback: \n\t1) Um Device \n\t2) Usar uma Lista de Ips \nR:'))

print('\n')

#IF: na primeira opção, foi criado uma Variavel 'ip' e uma Lista 'Loopback'
if verificar == 1:
    ip = input('Inserir IP de acesso: ') #Na variavel 'ip' será solicitado o IP de acesso do dispositivo
    
    #Sendo somente Uma loopback criada e 1 dispositivo, será pedido o numero da loobpack, a descrição
    #o IP Address e a Mascara de Sub-rede.
    loopback = [int(input('Numero da Loopback: ')),
                input('Description: '),
                input('Endereço IP: '),
                input('Mascara de SubRede: ')]
    print('\n')

    #E assim chamando a função 'umdevice' com o variavel 'ip' como argumento e iniciando a ação da mesma.
    umdevice(ip)

#SENÃO_SE: Foi criado uma Variavel 'arquivo' e uma Lista 'Loopback'
elif verificar == 2:
    arquivo = open("lista\ip.txt") #Para Abrir o arquivo de TXT na sua devida Localização

    '''
    A diferenteça dessa Lista 'Loopback' para a anterior é que na posição do Indice 2 'IP de Rede'
    é solicitado o IP de REDE ao em vez do Endereço IP direto, para assim fazer internamente
    na função 'lista' a variação de IPs, mas é claro que você já deve ter em mente como funciona
    o Calculo de IPs, pois o Python não faz por nativo a Validação se é ou não um 
    IP Valido, IP de Rede ou Broadcast, é algo muito complexo, mas não imposivel de se criar.
    OBS: Futuramente quem sabe eu não publique aqui rs
    '''
    loopback = [int(input('Numero da Loopback: ')),
                input('Description: '),
                input('IP de Rede: '),
                input('Mascara de SubRede: ')]
    print('\n')

    #E assim chamando a função 'lista' com o variavel 'arquivo' como argumento e iniciando a ação da mesma.
    lista(arquivo)

print('Concluido!')