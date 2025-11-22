<p align="center">
  <h1><p align="center">Rotina de Backup</p></h1>
</p>

Abaixo importamos a instancia criada para algoritimos repetitivos, conforme no arquivo [instances](https://github.com/ozumaru/CiscoDevNet---Python/blob/master/Documents/Projetos/Primeiro/Ambiente/Automation/Instance/instances.md), abaixo está a forma de se invocar a classe **function_default**, e está nesse formato pois **Automation.Instance.** é o Caminho do diretorio onde essa classe se encontra, juntamente sendo invocando também informações de [credentials](https://github.com/ozumaru/CiscoDevNet---Python/blob/master/Documents/Projetos/Primeiro/Ambiente/Automation/Instance/credentials.py) de acesso em formato de Tupla.

Também importando a biblioteca **datetime** para se criar uma parametro de tempo ao criar o arquivo de backup.
```Python
from Automation.Instance.instances import function_default
from Automation.Instance.credentials import device_info
from datetime import datetime
```
---
- **default**: O seguinte trecho faz a invocação das funções da Classe **function_default** na função nomeada como **default** podendo utilizar todas as funções que existem dentro da classe.

- **now**: A variavel **NOW** ira armazenar a data do sistema para ter como parametrô na criação do nome do arquivo de backup, dessa forma não sendo sobrescrito e de fato criar uma rotina de backup.

- **Hosts**: O Arquivo [hosts](https://github.com/ozumaru/CiscoDevNet---Python/blob/master/Documents/Projetos/Primeiro/Ambiente/Automation/hosts) possui a lista de acesso aos devices, no caso de um ambiente com multiplos devices, é nesse arquivo que será armazenado os endereço de acesso, sempre linha por linha.

```Python
# Instanciando a classe
default = function_default()

# Coletando data e hora para nome do arquivo
now = datetime.today().strftime('%d-%m-%Y_%Hh%Mm')

# Abrindo o arquivo com a lista de hosts
list_host = open("..\hosts")
```
---
Este trecho inicia um loop para percorrer cada device da lista e executar o procedimento de coleta individualmente.
Abaixo, a função de cada parâmetro e etapa:

 - **list_host**: lista contendo todos os dispositivos que serão acessados.
 - **commando**: lista de comandos enviados ao device.
    - Mesmo sendo apenas um comando nesse caso **(show running-config)**, ele é enviado como lista porque a mesma função também é usada por outros scripts que podem precisar de vários comandos.
 - **default.access_collect(host, device_info, commando)**: utilizando a classe function_default, chamamos a função access_collect, responsável por acessar o dispositivo e executar os comandos.
 - **lista_cisco**: convertemos o retorno do running-config em lista, para facilitar buscas e processamento posterior.
 - **hostname**: usando compreensão de lista para localizar a linha que começa com hostname e extrair somente o valor do hostname do equipamento.

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
---
O trecho abaixo cria o arquivo em formato **TXT**, utilizando o parametro "W" de Write, pois foi criado uma estratégia o arquivo não ser sobrescrito.
Parametros utilizados:
 - hostname: Contem o Hostname do Device
 - now: Contem - Dia_Mes_Ano-Hora_Minuto

```Python
    # Criando o arquivo de coleta com o nome do hostname e data/hora
    with open(f'Data\{hostname}_{now}.txt', 'w') as arq:
        arq.write(cisco)
        arq.close()
```

Links essenciais:
\
Script Limpo: [main_backup](https://github.com/ozumaru/CiscoDevNet---Python/blob/master/Documents/Projetos/Primeiro/Ambiente/Automation/BACKUP/main_backup.py)
\
Inicio do Projeto: [Inicio](https://github.com/ozumaru/CiscoDevNet---Python/blob/master/Documents/Projetos/Primeiro)
\
Video de Exeplicação: ⚠️ !!! EM PRODUÇÃO !!! ⚙️