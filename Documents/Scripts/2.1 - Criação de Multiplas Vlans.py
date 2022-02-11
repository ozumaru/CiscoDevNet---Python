from netmiko import ConnectHandler

print('VLAN: Virtual Local Area Network')
user = 'cisco'
userpass = 'cisco'
ip = '192.168.10.10' 

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

opcoes = 'S'
while opcoes == 'S':
    if opcoes == 'S':
        opcao = int(input('\nO que precisa fazer? \n\t(1) Criar Vlans \n\t(2) Deletar Vlans  \n\t(3) Nomear Vlan \n\t(4) Verificar Vlan no Equipamento \n\t(5) Sair\nR: '))
        if opcao == 1:
            print('\nModo de Criação de Vlan')
            q = int(input('\nQuantidade de Vlans criadas: ')) 
            if q == 1:
                n = int(input('\tNúmero da Vlan: ')) 
                config = ssh.send_config_set(f'vlan {n}')
                bvlan = ssh.send_command(f'show vlan brief | include {n}') 
                print(f'\n{bvlan}')
            elif q > 1:
                p = int(input('\tPrimeria de Vlan: ')) 
                u = int(input('\tAté Vlan: ')) 
                sn = input('\nA Criação de Vlans terá Variação? (S/N) \n\t(Exemplo (5)5x5 (10)10x10) \nR: ').upper() 
                if sn == 'N':
                    config = ssh.send_config_set(f'vlan {p}-{u}')
                    for x in range(p, u+1):
                        bvlan = ssh.send_command(f'show vlan brief | include {x}')
                        print(f'{bvlan}')
                elif sn == 'S':
                    v = int(input('\tIrá variar de quanto em quanto?  \nR: ')) 
                    for x in range(p, u+1, v):
                        config = ssh.send_config_set(f'vlan {x}')
                        bvlan = ssh.send_command(f'show vlan brief | include {x}')
                        print(bvlan)
        
        elif opcao == 2:
            print('\nModo de Execlusão de Vlans')
            q = int(input('\nQuantidade de Vlans Deletadas: '))
            if q == 1:
                n = int(input('\nNúmero da Vlan: '))
                config = ssh.send_config_set(f'no vlan {n}')
            elif q > 1:
                p = int(input('\tPrimeria de Vlan: '))
                u = int(input('\tAté Vlan: '))
                sn = input('\nA Exclusão de Vlans terá Variação? (S/N) \n\t(Exemplo (5)5x5 (10)10x10) \nR: ').upper()
                if sn == 'N':
                    config = ssh.send_config_set(f'no vlan {p}-{u}')
                elif sn == 'S':
                    v = int(input('\tIrá variar de quanto em quanto? \nR: '))
                    for x in range(p, u+1, v):
                        config = ssh.send_config_set(f'no vlan {x}')
        
        elif opcao == 3:
            print('\nModo de Nomear Vlan')
            vlan = [int(input('\tDigite a vlan: ')), input('\tDigite o nome: ')]
            nomear = [f'vlan {vlan[0]}', f'name {vlan[1]}']
            result = ssh.send_config_set(nomear)
            result = ssh.send_command(f'show vlan brief | include {vlan[0]}')
            print(f'\nResultado: {result}')
        elif opcao == 4:
            print('\nModo para Verificar Vlans')
            bvlan = ssh.send_command('show vlan brief')
            print(bvlan)
        elif opcao == 5:
            opcoes = ''
            break
        elif opcao < 1 or opcao > 5:
            print('Opção Invalida!')
    opcoes = input('\nContinuar: (S/N) \nR: ').upper()

print('\nFim da Operação: Vlans')
ssh.exit_enable_mode()
