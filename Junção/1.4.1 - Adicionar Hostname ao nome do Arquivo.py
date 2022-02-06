#Junção: Localizando o Hostname para usar como Nome do Arquivo de texto

'''
Essa primeira parte será para juntar a Criação de Arquivo de Texto e Acesso ao Host

- Conforme explicado anteriormente, será acessado um Host Cisco e coletar a informação de configuração completa do equipamento, a qual será recebida pela variavel 'config'

- Após a variavel 'hostname' ser o nome do device, será criado um arquivo de texto puxando uma informação para ser o nome do arquivo, e é a informação dentro da variavel 'hostname'.
'''

from netmiko import ConnectHandler

#Variaveis com informações de usuario, senha e ip do device.
user = 'cisco'
userpass = 'cisco'
host = '192.168.10.192'

#Dicionário utilizando variaveis contendo dados de acesso e host que será acessado
cisco_router = {
    'device_type': 'cisco_ios',
    'host': host,
    'username': user,
    'password': userpass,
    'secret': userpass,
    'port': 22,
}
ssh = ConnectHandler(**cisco_router)
ssh.enable()

config = ssh.send_command('show running')
ssh.exit_enable_mode()

#Para conseguirmos localizar o Nome do host, foi criado a variavel 'running' que ira receber toda a informação da variavel 'config' utilizando a função .split() para quebrar todo o texto com base em cada Espaço, e separar cada informação por Indices.
running = (config).split()


#	- A estrutura FOR cria uma Variavel contadora 'x' para percorrer com base no Tamanho (quantidade de Indices) que a variavel 'running' possui.
#   	- A condição IF ira validar que SE 'hostname' for igual a Posição da variavel 'running'[na Posição do Indice 'x'] e essa condição for verdadeira, a variavel 'hostname' ira receber a variavel 'running'[na Posição do Indice 'x' + 1].
#		    - SE não for verdadeiro ele Ignora e o Loop se repede no proximo Salto até ser quem o IF diz que Tem que ser.


for x in range(len(running)):
    if 'hostname' == running[x]:
        hostname = running[x+1]

#- a Variavel 'arq' abrirá com OPEN (Na localização onde o arquivo estiver\ o arquivo vai recever a variavel 'hostnames'.txt) em modo de Escrita 'w')
#- A variavel 'arq.write()' em modo de escrita vai usar a informação armazenada na variavel 'config' para escrever no arquivo, log em seguida fechando o mesmo com 'arq.close()'.

arq = open(f'coleta\ {hostname}.txt', 'w')
arq.write(config)
arq.close()

#Print de texto trazendo informação da Variavel 'hostname'
print (f'O nome do Device e: {hostname}')

#Print com Caracter '=' sendo Multiplicado 20 Vezes formando uma Linha.
print ('='*20)

#Print da variavel 'config' mostrando o Show Running com conteúdo
print (config)





