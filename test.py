from scapy.layers.inet import IP, UDP
from scapy.layers.l2 import Ether
from scapy.packet import Raw
from scapy.sendrecv import sendp, send, sniff

pkts=sniff(count=10, iface="lo")

print(pkts)