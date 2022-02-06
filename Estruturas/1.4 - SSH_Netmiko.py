'''NETMIKO
Site para informação:
    https://pypi.org/project/netmiko/
    https://pythonacademy.com.br/blog/tipos-de-variaveis-no-python#dicionários-dict

Uma Biblioteca para o Python é uma valioza caixa de ferramenta que 
tem muitas funções internas.

Podemos utilizar as bibliotecas para serem Importadas no programa 
de forma geral (Com todas as suas ferramentas) ou escolher de dentro 
da Caixa apenas a ferramenta necessária para a atividade.

A sintaxe para se utilizar uma biblioteca é simple:

- Para importar toda a Biblioteca:
import biblioteca

- Para importa somente uma ferramenta da biblioteca:
from biblioteca import ferramenta

O Netmiko é uma Biblioteca totalmente focada para Network no Geral, 
ela não é funcional só para Cisco, pois é uma Ferramenta Multi-Vendor, 
sendo assim ela trabalha com muitas marcas, e até mesmo pode-se ser 
utilizada em Sistemas como Linux.

'''
from netmiko import ConnectHandler

'''
Variaveis de String

Existem algumas formas de Variaves de String, mas a que iremos trabalhar são:

String(str) - É um conjunto de caracteres posto em uma determinada ordem, 
geralmente para representar Palavras, Frases ou Texto

Lista(list) - Lista agrupam um conjunto de elementos variados, sendo eles: 
Inteiros, Floats, Strings.

Dicionario(dict) - São utilizado para agrupar elementos atráves da estrutura 
Chave e Valor, onde a chave é o primeiro elemento seguido por dois pontos e pelo valor.

Exemplo!

string = 'Isso é um exemplo de string'

lista = ['essa', 'variavel', 'e', 1, 'lista']

dicionario = { 
    'chave': 'Valor',
    'usuario': 'cisco',
    'senha': 123    
}


'''

#Dicionario contendo as informações de acesso ao equipamento, desde tipo 
#de IOS (Sistema Operacional do Equipamento CISCO), IP, Usuario, Senha, 
#Senha Secreta do Enable e a Porta 22 que nesse caso é o do Protocolo SSH.
cisco_router = {
    'device_type': 'cisco_ios',
    'host': '192.168.10.192',  #IP do equipamento que será acessado
    'username': 'cisco',
    'password': 'cisco',
    'secret': 'cisco',
    'port': 22,
}

#A Variavel ssh ao receber a Função ConnectHandler da biblioteca, ira 
#utilizar as informações do Dicionario para realizar o acesso ao equipamento 
#até que seja encerrado o acesso.
ssh = ConnectHandler(**cisco_router)

#A Função .enable ira entrar em modo Enable, sendo que na Variavel contendo 
#as informações da Lista, ele tem a Chave 'Secret' que nesse caso é a senha do Modo Enable
ssh.enable()


#A Variavel Result, utilizando a variavel SSH com uma função de Enviar um 
#Comando ao equipamento '.send_command()' e dentro da função o comando e modo 
#String para que o equipamento entenda a solicitação.
result = ssh.send_command('show ip interface brief')
ssh.exit_enable_mode()


#A Função Print ira Mostrar no terminal o Resultado que foi obtido ao enviar o 
#comando e ser armazenado na Variavel.
print (result)
