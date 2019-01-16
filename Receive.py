import socket
from array import array
from random import randrange

from scapy.layers.inet import IP, UDP, TCP
from scapy.layers.l2 import Ether
from scapy.packet import Raw
from scapy.sendrecv import sendp, send





greeting='Hello Andi this is the number you wanted:'

number=1000000



with open('a.png', 'rb') as f:
    while True:
        chunk = f.read(1400)
        if not chunk:
            break

        number_to_send = str(number).encode('ascii')
        number_to_send_byte = bytes(number_to_send)
        data=chunk+number_to_send
        sendp(Ether() / IP(src="127.0.0.1", dst="192.168.11.47") / UDP(sport=randrange(65530), dport=5005) / Raw(
            load=data), iface="wlp3s0")
        number=number+1
        print(number)
        print(data)



