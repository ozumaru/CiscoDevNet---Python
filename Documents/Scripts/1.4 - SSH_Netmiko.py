from netmiko import ConnectHandler

cisco_router = {
    'device_type': 'cisco_ios',
    'host': '192.168.10.192',
    'username': 'cisco',
    'password': 'cisco',
    'secret': 'cisco',
    'port': 22
}

ssh = ConnectHandler(**cisco_router)
ssh.enable()

result = ssh.send_command('show ip interface brief')
ssh.disconnect()

print (result)
