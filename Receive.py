import socket
from Functions import divide_counter_packet, add_data_in_order, create_empty_array
UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

size_of_file=10
file_array=create_empty_array(size_of_file)

counter = 0

while True:

    data_and_counter, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    data_and_counter_array = divide_counter_packet(data_and_counter)
    file_array = add_data_in_order(file_array, data_and_counter_array[0], data_and_counter_array[1])
    counter = +1
