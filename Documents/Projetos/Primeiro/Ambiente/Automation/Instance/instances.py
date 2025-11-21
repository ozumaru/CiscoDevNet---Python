# Importando biblioteca Netmiko
from netmiko import ConnectHandler

# Funções Padrões de Acesso e Coleta instanciadas em outros scripts
class function_default():

    # Função de Acesso e Coleta
    def access_collect(self, host, device_info, commando):
        
        # Desempacotando device_info tupla
        device_type, username, password = device_info
        
        # Inicializando variável de resultado
        result = ""
        
        # Definindo o dicionário de conexão
        device = {
            'device_type': device_type,
            'host': host,
            'username': username,
            'password': password,
            'secret': password, 
            'port': 22
        }

        # Estabelecendo conexão SSH
        ssh = ConnectHandler(**device)
        
        # Entrando no modo enable
        ssh.enable()

        # Loop para enviar comandos e coletar resultados
        for comm in commando:
            result += f"{ssh.send_command(comm)}\n" 

        # Encerrando a conexão SSH
        ssh.disconnect()

        # Retornando o resultado da coleta
        return result
    
    # Função de Envio de Configuração
    def send_config_default(self, host, device_info, commando):

        # Desempacotando device_info tupla
        device_type, username, password = device_info
        
        # Inicializando variável de resultado
        result = ""
        
        # Definindo o dicionário de conexão
        device = {
            'device_type': device_type,
            'host': host,
            'username': username,
            'password': password,
            'secret': password,
            'port': 22
        }

        # Estabelecendo conexão SSH
        ssh = ConnectHandler(**device)
        
        # Entrando no modo enable
        ssh.enable()

        # Enviando comandos de configuração
        result = f"{ssh.send_config_set(commando, read_timeout=120)}\n" 

        # Encerrando a conexão SSH
        ssh.disconnect()

        # Retornando o resultado da configuração
        return result

    # Tratando coleta de status de interface
    def get_interface_function(self, get_interface, interface):
        
        # Dividindo a linha da interface em uma lista
        list_int = interface.split()

        # Interface em Admin Down
        # Exemplo: GigabitEthernet0/1  unassigned  administratively down down
        if len(list_int) == 7:
            get_interface[list_int[0]] = {
                "address": list_int[1],
                "status": f"{list_int[-3]}_{list_int[-2]}",
                "protocol": list_int[-1]
                } 
        
        # Status Normal
        # Exemplo: GigabitEthernet0/0 up up
        elif len(list_int) == 6:
            get_interface[list_int[0]] = {
                "address": list_int[1],
                "status": list_int[-2],
                "protocol": list_int[-1]
                }
        
        # Retornando o dicionário atualizado
        return get_interface

# Fim do Script