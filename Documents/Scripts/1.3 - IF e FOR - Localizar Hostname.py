host = ''
texto = '''
!
version 15.4
service timestamps debug datetime msec
service timestamps log datetime msec
no service password-encryption
!
hostname R1
!
boot-start-marker
boot-end-marker
!
'''

text = (texto).split()

for x in range(len(text)):
    if 'hostname' == text[x]:
        host = text[x+1]
        print (host)
