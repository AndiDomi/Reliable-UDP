import socket
import time

UDP_IP = "192.168.11.47"
UDP_PORT = 5005

print( "UDP target IP:", UDP_IP)
print("UDP target port:", UDP_PORT)

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
num = 'a'.encode()
while True:
    sock.sendto(num, (UDP_IP, UDP_PORT))
    print ("Message sent: " + str(num))
    time.sleep(1)