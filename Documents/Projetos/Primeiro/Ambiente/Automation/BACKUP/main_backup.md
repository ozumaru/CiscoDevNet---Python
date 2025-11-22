<p align="center">
  <h1><p align="center">Rotina de Backup</p></h1>
</p>

Abaixo iniciamos importa a instancia criada para algoritimos repetitivos, conforme no arquivo [instances](https://github.com/ozumaru/CiscoDevNet---Python/blob/master/Documents/Projetos/Primeiro/Ambiente/Automation/Instance/instances.md), abaixo está a forma de se invocar a classe **function_default**, e está nesse formato pois **Automation.Instance.** é o Caminho do diretorio onde essa classe se encontra, juntamente sendo invocando também informações de [instances](https://github.com/ozumaru/CiscoDevNet---Python/blob/master/Documents/Projetos/Primeiro/Ambiente/Automation/Instance/credentials.py) de acesso em formato de Tupla.

Também importando a biblioteca **datetime** para se criar uma parametro de tempo ao criar o arquivo de backup.
```Python
from Automation.Instance.instances import function_default
from Automation.Instance.credentials import device_info
from datetime import datetime
```
---
```Python
# Instanciando a classe
default = function_default()

# Coletando data e hora para nome do arquivo
now = datetime.today().strftime('%d-%m-%Y_%Hh%Mm')
```
---
O Arquivo [hosts](https://github.com/ozumaru/CiscoDevNet---Python/blob/master/Documents/Projetos/Primeiro/Ambiente/Automation/hosts) possui a lista de acesso aos devices, no caso de um ambiente com multiplos devices, é nesse arquivo que será armazenado os endereço de acesso, sempre linha por linha.

```Python
# Abrindo o arquivo com a lista de hosts
list_host = open("..\hosts")
```
---
<!-- Iniciando Loop na lista de devices para que seja executado device por device.

Parametros que vão abranger a parte inicial do Loop:
list_host: Lista de Hosts para acesso
commando: Lista de Comandos a ser enviados ao device, como trata-se de um backup: show running-config
- OBS: O porque de estar sendo enviado uma LISTA, é porque outros scrips podem usar a mesma função de coleta e enviar mais de 1 comando, então já se é tratado como LISTA
default.access_collect(host, device_info, commando): Com base na Instanciando a Classe **function_default**, invocando a Função **access_collect** e passando os parametrôs: host, device_info, commando
lista_cisco: Quebrando o retorno do Running-config em uma Lista para posterior tratativa
hostname: Usando Compreesão de Lista para localizar o hostname do device. -->

Este trecho inicia um loop para percorrer cada device da lista e executar o procedimento de coleta individualmente.
Abaixo, a função de cada parâmetro e etapa:

 - list_host → lista contendo todos os dispositivos que serão acessados.
 - commando → lista de comandos enviados ao device.
    - Mesmo sendo apenas um comando nesse caso (show running-config), ele é enviado como lista porque a mesma função também é usada por outros scripts que podem precisar de vários comandos.
 - default.access_collect(host, device_info, commando) → utilizando a classe function_default, chamamos a função access_collect, responsável por acessar o dispositivo e executar os comandos.
 - lista_cisco → convertemos o retorno do running-config em lista, para facilitar buscas e processamento posterior.
 - hostname → usando compreensão de lista para localizar a linha que começa com hostname e extrair somente o valor do hostname do equipamento.

```Python
# Loop para cada host na lista
for host in list_host: 
    # Definindo lista de comando
    commando = ["show running-config"]

    # Realizando a coleta do running-config
    cisco = default.access_collect(host, device_info, commando) 
    
    # convertendo a coleta em uma lista
    lista_cisco = cisco.split("\n")
    
    # Extraindo o hostname da coleta com compreensão de listas
    hostname = next(name.split()[1] for name in lista_cisco if name.startswith("hostname"))
```

```Python
    # Criando o arquivo de coleta com o nome do hostname e data/hora
    with open(f'Data\{hostname}_{now}.txt', 'w') as arq:
        arq.write(cisco)
        arq.close()
```