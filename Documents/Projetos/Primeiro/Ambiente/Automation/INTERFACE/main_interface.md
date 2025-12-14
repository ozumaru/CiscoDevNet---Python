<p align="center">
  <h1><p align="center">Criando relatório de Status das Interaces</p></h1>
</p>

Abaixo importamos a instancia criada para algoritimos repetitivos, conforme no arquivo [instances](https://github.com/ozumaru/CiscoDevNet---Python/blob/master/Documents/Projetos/Primeiro/Ambiente/Automation/Instance/instances.md), abaixo está a forma de se invocar a classe **function_default**, e está nesse formato pois **Automation.Instance.** é o Caminho do diretorio onde essa classe se encontra, juntamente sendo invocando também informações de [credentials](https://github.com/ozumaru/CiscoDevNet---Python/blob/master/Documents/Projetos/Primeiro/Ambiente/Automation/Instance/credentials.py) de acesso em formato de Tupla.

Também importando a biblioteca **datetime** para se criar uma parametro de tempo ao criar o arquivo de backup.
```Python
# Importando as bibliotecas necessárias
from Automation.Instance.instances import function_default
from Automation.Instance.credentials import device_info
from datetime import datetime
import csv, os
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

# Inicializando dicionários para tratativa de dados
get_interface = {}
hostname_interface = {}
```
---
Este trecho inicia um loop para percorrer cada device da lista e executar o procedimento de coleta individualmente.
Abaixo, a função de cada parâmetro e etapa:

 - **list_host**: lista contendo todos os dispositivos que serão acessados.
 - **commando**: lista de comandos enviados ao device, e temos agora 2 comandos:
    - **show running-config | include hostname** - Para retornar exatamente a linha do hostname.
    - **show ip interface brief** - Retornar o output dos status das interfaces existentes no device.
 - **default.access_collect(host, device_info, commando)**: utilizando a classe function_default, chamamos a função access_collect, responsável por acessar o dispositivo e executar os comandos.
 - **lista_cisco**: convertemos o retorno do running-config em lista, para facilitar buscas e processamento posterior.
 - **hostname**: Nesse formado, sendo que o comando que está na variavel nesse momento é output dos 2 comandos, e nesse caso o hostname está na primeira linha, pois foi o primeiro comando a ser enviado.
 - **default.get_interface_function(get_interface, interface)**: É enviado 2 parametros para a funação:
    - **get_interface** - Dicionario vazio que vai armazenar linha por linha, e transformar em um JSON.
    - **interface** - Variavel de contagem do loop que vai enviar linha a linha para a função para tratamento.
 - **hostname_interface** - Dicionario vazio que vai ter como Chave/Key o hostname do device, e como Valor/Value o Json criado na função anterior **get_interface**.
 - **try**: é exatamente o que a própria palavra diz: Tentar, pois caso de algum erro, ele vai para Except.

```Python
# Loop para cada host na lista
for host in list_host:

    # Definindo lista de comandos
    commando = ["show running-config | include hostname", "show ip interface brief"]
    
    try:
        cisco = default.access_collect(host, device_info, commando)
        # print(cisco)
        
        # Convertendo a coleta em uma lista
        lista_cisco = cisco.split("\n") 

        # Extraindo o hostname da coleta
        hostname = lista_cisco[0].split()[1]

        # Tratando coleta de status de interface
        for interface in lista_cisco:
            # Tratando linhas de interfaces: GigabitEthernet, FastEthernet, etc
            get_interface = default.get_interface_function(get_interface, interface) 

        # Criando dicionário com hostname e suas interfaces
        hostname_interface[hostname] = get_interface 
```
---
Este trecho prepara toda a estrutura necessária para criar e manter o arquivo interfaces.csv, garantindo que novas coletas possam ser adicionadas sem duplicar registros já existentes.

Abaixo está a função de cada etapa e variável:

**output_file** - Nome do arquivo CSV que armazenará todas as interfaces coletadas.

**header** - Lista com os nomes das colunas do CSV:
 - Hostname – Nome do device.
 - Interface – Interface coletada.
 - IP-Address – Endereço IP da interface.
 - Status – Status administrativo (up/down).
 - Protocol – Status do protocolo (up/down).

Esses campos serão utilizados como cabeçalho caso o arquivo ainda não exista.

**file_exists** - Verifica se o arquivo interfaces.csv já foi criado anteriormente.
Serve para saber se precisamos criar o arquivo do zero ou apenas complementar.

**existing_rows** - Lista que armazenará todas as linhas já existentes no CSV.
Isso evita que o script grave duplicatas quando o mesmo device for coletado mais de uma vez.

Bloco **if file_exists**: - Caso o arquivo já exista:
 - Ele é aberto em modo leitura.
 - O cabeçalho é ignorado com next(reader, None)
 - Todo o conteúdo é convertido em uma lista (existing_rows) para posterior comparação.

Isso prepara o script para:
 - Validar se a interface já foi registrada
 - Complementar novas informações sem sobrescrever
 - Garantir que o CSV mantenha integridade e consistência
```Python
        # Criando o Arquivo de coleta
        output_file = "interfaces.csv"
        header = ["Hostname", "Interface", "IP-Address", "Status", "Protocol"]

        # Verifica se o arquivo já existe
        file_exists = os.path.exists(output_file)

        # Se existir, carrega conteúdo pra evitar duplicatas
        existing_rows = []
        if file_exists:
            with open(output_file, newline="") as csvfile:
                reader = csv.reader(csvfile)
                next(reader, None)  # Pula o cabeçalho (se houver)
                existing_rows = [row for row in reader]
```
---
Este trecho é responsável por gravar os dados coletados no arquivo interfaces.csv, garantindo que nenhuma linha seja duplicada e que o cabeçalho seja criado apenas quando necessário.

Abaixo está o papel de cada etapa:

### Abertura do arquivo em modo append ("a")
O arquivo é aberto no modo append, o que significa:
 - Nada é apagado.
 - Novas linhas são adicionadas ao final.
 - É a forma mais segura para atualizar coletas sem perder dados antigos.


**writer = csv.writer(csvfile)**
Cria o objeto responsável por escrever linhas no formato CSV.


**Escrita do cabeçalho (somente se o arquivo for novo)** - if not file_exists:
O cabeçalho só é adicionado se o arquivo ainda não existia, evitando duplicação de títulos.

**Loop pelos devices e suas interfaces**
Aqui percorremos cada device coletado e seu respectivo dicionário de interfaces.

**new_row**

Para cada interface, montamos uma linha com:
 - Hostname
 - Interface
 - IP
 - Status
 - Protocol

Essa linha será comparada antes de ser escrita.

**Verificação de duplicatas**
O script verifica se já existe uma linha com o mesmo:
 - Hostname
 - Interface

Se sim, pulamos essa entrada.
Se não, escrevemos no CSV.

Essa lógica garante que o arquivo:
 - Não cresça desnecessariamente
 - Não crie entradas repetidas quando o script rodar várias vezes
 - Mantenha uma coleta limpa e organizada
```Python
        # Abre o arquivo para append (sem apagar conteúdo existente)
        with open(output_file, mode="a", newline="") as csvfile:
            writer = csv.writer(csvfile)

            # Escreve o cabeçalho apenas se o arquivo for novo
            if not file_exists:
                writer.writerow(header)

            # Percorre cada hostname e suas interfaces
            for hostname, interfaces in hostname_interface.items():
                for intf, info in interfaces.items():
                    new_row = [
                        hostname,
                        intf,
                        info["address"],
                        info["status"],
                        info["protocol"],
                    ]

                    # Evita duplicar linha já existente (hostname + interface)
                    duplicate_found = False
                    for row in existing_rows:
                        if row[0] == hostname and row[1] == intf:
                            duplicate_found = True
                            break

                    # Escreve a nova linha se não for duplicata
                    if not duplicate_found:
                        writer.writerow(new_row)
```
O Except serve para caso o trecho de acesso ao device por algum motivo: 
  - O Device não está acessivel
  - Usuario e senha Errado

Vai retornar qual foi o erro, pois tratar o erro dessa forma é uma forma mais Limpa, e não trava o programa, e assim se tiver outros devices o script segue normal.

```Python
    except Exception as e:
        print(f"Não foi possível conectar ao host {host.strip()}. Erro: {e}")
```

Links essenciais:
\
Script Limpo: [main_interface](https://github.com/ozumaru/CiscoDevNet---Python/blob/master/Documents/Projetos/Primeiro/Ambiente/Automation/INTERFACE/main_interface.py)
\
Inicio do Projeto: [Inicio](https://github.com/ozumaru/CiscoDevNet---Python/blob/master/Documents/Projetos/Primeiro)
\
Video de Exeplicação: [Parte 1](https://www.youtube.com/watch?v=NHoNt21UnJs) \ [Parte 2](https://www.youtube.com/watch?v=d-3HldELBnM) \ [Parte 3](https://www.youtube.com/watch?v=Hl1G6pDfuDA) \ [Parte 4](https://www.youtube.com/watch?v=kl-Lj_iU0VY)