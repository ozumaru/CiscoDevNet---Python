#Contexto de Biblioteca explicado no Arquivo: 2 - SSH_Netmiko

'''
A Biblioteca Datetime tem como função usar o sistema para trazer a informação atual de Data e Hora.

Conforme mostra na Variavel é aplicado o 'datetime' e trazendo a inforação .TODAY (HOJE), dentro dessa forma de trazer essa informação o .STRFTIME auxilia em como manipular essa informação para que a Variavel a Receba.

d - day
m - month
Y - Year (Ano completo: 2022) - y (Ultimos numero: 22)

H - Hour
M - Minute 

Print ira trazer a informação que a variavel 'agora' recebeu.
'''
from datetime import datetime

agora = datetime.today().strftime('%d-%m-%Y_%Hh%Mm')

print(agora) 