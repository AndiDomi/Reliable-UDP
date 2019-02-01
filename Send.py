import socket
from array import array
from random import randrange

from scapy.layers.inet import IP, UDP, TCP
from scapy.layers.l2 import Ether
from scapy.packet import Raw
from scapy.sendrecv import sendp, send

def add_counter_packet(data, counter):
    print(counter)
    print(chr(counter))
    counter = chr(counter).encode('ascii')
    data = data + counter
    return data

number=0



with open('a.png', 'rb') as f:
    while True:
        chunk = f.read(1400)
        if not chunk:
            break
        data= add_counter_packet(chunk, number)
        sendp(Ether() / IP(src="127.0.0.1", dst="192.168.11.47") / UDP(sport=randrange(65530), dport=5005) / Raw(
            load=data), iface="wlp3s0")
        number=number+1




