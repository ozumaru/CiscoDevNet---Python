#Criação de Arquivo

#Nome do Arquivo
nome = 'new'

#Texto dentro do arquivo
texto = 'To Infinity and Beyond!'

'''
1 - Primeiro é necessário criar um variavel que ira armazenar a informação de forma temporária.

- O 'OPEN' terá a função de Criar Ou Abrir um arquivo.

- O 'f' é um Método que  simboliza Format, ele auxilia na forma como Organizamos as nossas Variaveis dentro de uma string.

- A '\' auxilia na localização do diretório será criado ou aberto, seguido do Nome do Arquivo.

- As Chaves '{}' é onde iremos direcionar a Variavel, nesse exemplo está com a informação de NOME, que é a Variavel que tem uma string armazenada, que nesse caso fará a função de dar o nome ao arquivo, e o tipo do Arquivo (.txt).

- Dentro da Variavel ARQ que ira receber a informação, o 'W' é de Write (Escrita), ele tem a função de abrir o arquivo em forma de escrita.

2 - Nesse momento o Arquivo é a Variavel ARQ, e a função .WRITE ira escrever alguma informação dentro do Arquivo, nesse caso, a informação que será armazenada é a Variavel TEXTO, que contem uma String.

3 - Ao Fechar o Arquivo é o momento em que o programa para de armazenar a informação dentro do arquivo e o Encerra, dessa forma, salvando a informação dentro do mesmo.
'''
arq = open(f'coleta\ {nome}.txt', 'w')
arq.write(texto)
arq.close()

------------------

#Leitura de Arquivo 

'''
1 - Primeiro é necessário criar um variavel que ira armazenar a informação de forma temporária.
 
- A Variavel 'leitura' ira receber a informação da Variavel 'arq' (Nesse momento a função da variavel 'arq' é ser o arquivo aberto).

- O For ira criar a Variavel Contadora 'linha' que a cada "volta", será uma informação que ira receber da variavel 'leitura', nesse caso ira ler Linha por linha do arquivo 'ip.txt'

- e a cada "volta", a função Print irá mostrar a informação que a variavel contadora 'linha' é em cada volta.
'''

arq = open("lista\ip.txt")
leitura = arq.readlines()
for linha in range(len(leitura)):
    print(leitura[linha])