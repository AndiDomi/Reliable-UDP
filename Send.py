import socket
from array import array
from random import randrange

from scapy.layers.inet import IP, UDP, TCP
from scapy.layers.l2 import Ether
from scapy.packet import Raw
from scapy.sendrecv import sendp, send
from Functions import add_counter_packet


counter = 1

with open('a.png', 'rb') as f:
    while True:
        chunk = f.read(1023)
        if not chunk:
            break
        data_and_counter = add_counter_packet(chunk, counter)
        print(data_and_counter)
        sendp(Ether() / IP(src="127.0.0.1", dst="127.0.0.1") / UDP(sport=randrange(65530), dport=5005) / Raw(
            load=data_and_counter), iface="lo")
        counter += 1




