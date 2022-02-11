#Criação de Arquivo
nome = 'new'
texto = 'To Infinity and Beyond!'

arq = open(f'coleta\ {nome}.txt', 'w')
arq.write(texto)
arq.close()

#Leitura de Arquivo 
arq = open("lista\ip.txt")
leitura = arq.readlines()
for linha in range(len(leitura)):
    print(leitura[linha])