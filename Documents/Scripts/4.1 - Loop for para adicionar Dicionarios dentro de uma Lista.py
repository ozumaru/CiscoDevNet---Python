# -*- coding: iso-8859-1 -*-
# -*- coding: utf-8 -*-

device = "SWA-"
ip_device = "Ip-"
input_port = "In-port-"
outgoing_port = "Out-port-"
n = 0

cdp = []

for x in range(1, 6):
    coleta = {"Device":device+str(n), "IP":ip_device+str(n), "Input_Port":input_port+str(n), "Outgoing_Port":outgoing_port+str(n)}
    cdp.append(coleta)
    
    n += 1

print(cdp) 