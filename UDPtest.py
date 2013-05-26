import socket
from time import sleep

UDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    data = raw_input("Data to send via UDP: ")
    UDP.sendto(data, ("192.168.1.3", 5005))
