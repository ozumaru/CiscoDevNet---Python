<p align="center">
  <h1><p align="center">Criando a Instancia</p></h1>
  <h2><p align="center">Classes e Funções</p></h2>
</p>

```Python
# Importando biblioteca Netmiko
from netmiko import ConnectHandler
```

Aqui trata-se de um Agrupamento de Funções, e para isso utilizamos a **Classe** para realizar esse agrupamento
\
Conforme abaixo fora criado a classe **function_default** que todos os demais scripts desse projeto iram importar para realizar determinadas funções.
\
Dentro dessa Classe, temos a principio 3 Funções
 - **ACCESS_COLLECT**: Função inicial que vai Acessar o Device e vai enviar uma Lista de comando, pode ser 1 ou mais comandos
 - **SEND_CONFIG_DEFAULT**: Função que ira enviar para o device um conjunto de Configuração para ser aplicados, no caso do Cisco como exemplo da tarefa, em modo **configure terminal**
 - **GET_INTERFACE_FUNCTION**: Função ira tratar a coleta de interfaces, retornando no final um JSON contendo o padrão:

Exemplo do Retorno do Json:
```Json
    {
        "Nome_da_Interface": {
            "Endereço_IP": "Retorno do IP",
            "status": "UP/ DOWN/ ADMIN DOWN",
            "protocol": "UP/DOWN"
        }
    }
```

Inicio da Classe:
```Python
# Funções Padrões de Acesso e Coleta instanciadas em outros scripts
class function_default():
```
---
Parâmetros da Função: **"access_collect"**

**host**: Endereço de acesso do Device
\
**device_info**: Tupla - Conteudo: (device_type, Usuario, Senha)
\
**commando**: Lista de Comandos a serem enviados ao device para coleta

OBS: A forma a baixo de se **"Desempacotar"** só é possivel realizar no tipo Tupla, não é possivel fazer o mesmo com Lista

```Python
    # Função de Acesso e Coleta
    def access_collect(self, host, device_info, commando):

        # Desempacotando device_info tupla
        device_type, username, password = device_info
        
        # Inicializando variável de resultado para Armazenar multiplos resultados
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
```
---
Parâmetros da Função: **"send_config_default"**

**host**: Endereço de acesso do Device
\
**device_info**: Tupla - Conteudo: (device_type, Usuario, Senha)
\
**commando**: Lista de Comandos a serem enviados ao device para coleta

OBS: A forma a baixo de se "Desempacotar" só é possivel realizar no tipo Tupla, não é possivel fazer o mesmo com Lista

```Python
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
```
---
Parâmetros da Função: **"get_interface_function"**

**get_interface**: Dicionario Vazio para armazenar informação que será tratado durante ação da Função.
\
**interface**: Output do comando - show ip interface brief

OBS: Como se trata de um retorno de um comando Especifico, então é uma função especifica que se repete muitas vezes dependendo da quantidade de interfaces o device tiver

```Python
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
```