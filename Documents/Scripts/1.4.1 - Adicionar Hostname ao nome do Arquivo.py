from netmiko import ConnectHandler

user = 'cisco'
userpass = 'cisco'
host = '192.168.10.192'

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

running = (config).split()

for x in range(len(running)):
    if 'hostname' == running[x]:
        hostname = running[x+1]

arq = open(f'coleta\ {hostname}.txt', 'w')
arq.write(config)
arq.close()

print (f'O nome do Device e: {hostname}')
print ('='*20)
print (config)
