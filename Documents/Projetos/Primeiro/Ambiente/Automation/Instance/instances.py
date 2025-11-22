from netmiko import ConnectHandler

class function_default():

    def access_collect(self, host, device_info, commando):
        device_type, username, password = device_info
        
        result = ""
        
        device = {
            'device_type': device_type,
            'host': host,
            'username': username,
            'password': password,
            'secret': password, 
            'port': 22
        }

        ssh = ConnectHandler(**device)
        ssh.enable()
        
        for comm in commando:
            result += f"{ssh.send_command(comm)}\n" 

        ssh.disconnect()
        return result
    
    def send_config_default(self, host, device_info, commando):
        device_type, username, password = device_info
        
        result = ""
        
        device = {
            'device_type': device_type,
            'host': host,
            'username': username,
            'password': password,
            'secret': password,
            'port': 22
        }

        ssh = ConnectHandler(**device)
        ssh.enable()

        result = f"{ssh.send_config_set(commando, read_timeout=120)}\n" 

        ssh.disconnect()
        return result

    def get_interface_function(self, get_interface, interface):
        
        list_int = interface.split()

        if len(list_int) == 7:
            get_interface[list_int[0]] = {
                "address": list_int[1],
                "status": f"{list_int[-3]}_{list_int[-2]}",
                "protocol": list_int[-1]
                } 
        
        elif len(list_int) == 6:
            get_interface[list_int[0]] = {
                "address": list_int[1],
                "status": list_int[-2],
                "protocol": list_int[-1]
                }
        
        return get_interface
