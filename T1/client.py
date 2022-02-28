import socket
import time
import datetime
import math
import sys

def print_stats(transmission_time, number_of_packets, number_of_bytes):
    print("---Session stats " + str(datetime.datetime.now()).split('.')[0] + "---")
    print("Transmission Time:" + str(transmission_time) + " seconds")
    print("Number of Packets: " + str(number_of_packets))
    print("Number of bytes: " + str(number_of_bytes))
    print(" ")

def get_buffer_to_send(file='2.pbf'):
    with open(file, "rb") as file:
        buffer = file.read()
    return buffer

def send_via_tcp(buffer_size, msgFromClient, ack=False):
    serverAddressPort = ("127.0.0.1", 3000)

    number_of_blocks = len(msgFromClient) / buffer_size
    server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

    if ack:
        server_socket.settimeout(1)

    server_socket.connect(serverAddressPort)

    start_time = time.time()

    for i in range(int(number_of_blocks)):
        server_socket.send(msgFromClient[i*buffer_size:(i+1)*buffer_size])
        if ack:
            acknowledged = False

            while not acknowledged:
                try:
                    server_socket.recv(1)
                    acknowledged = True
                except socket.timeout:
                    server_socket.send(msgFromClient[i*buffer_size:(i+1)*buffer_size])

    if number_of_blocks > int(number_of_blocks):
        server_socket.send(msgFromClient[int(number_of_blocks)*buffer_size:])
        if ack:
            acknowledged = False

            while not acknowledged:
                try:
                    server_socket.recv(1)
                    acknowledged = True
                except socket.timeout:
                    server_socket.send(msgFromClient[int(number_of_blocks)*buffer_size:])
    print_stats(time.time() - start_time, math.ceil(number_of_blocks), len(msgFromClient))

    time.sleep(2)
    server_socket.close()

def send_via_udp(buffer_size, msgFromClient, ack=False):
    serverAddressPort = ("127.0.0.1", 3001)

    number_of_blocks = len(msgFromClient) / buffer_size
    server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    if ack:
        server_socket.settimeout(1)

    start_time = time.time()

    for i in range(int(number_of_blocks)):
        server_socket.sendto(msgFromClient[i*buffer_size:(i+1)*buffer_size], serverAddressPort)
        if ack:
            acknowledged = False

            while not acknowledged:
                try:
                    server_socket.recvfrom(1)
                    acknowledged = True
                except socket.timeout:
                    server_socket.sendto(msgFromClient[i*buffer_size:(i+1)*buffer_size], serverAddressPort)

    if number_of_blocks > int(number_of_blocks):
        server_socket.sendto(msgFromClient[int(number_of_blocks)*buffer_size:], serverAddressPort)
        if ack:
            acknowledged = False

            while not acknowledged:
                try:
                    server_socket.recvfrom(1)
                    acknowledged = True
                except socket.timeout:
                    server_socket.sendto(msgFromClient[int(number_of_blocks)*buffer_size:], serverAddressPort)

    print_stats(time.time() - start_time, math.ceil(number_of_blocks), len(msgFromClient))

if __name__ == '__main__':
    argv = sys.argv[1:]
    if len(argv) < 2:
        sys.exit(-1)


    if(argv[0].lower() == 'udp'):
        msgFromClient = get_buffer_to_send(argv[1])
        send_via_udp(int(argv[2]), msgFromClient, bool(argv[3]))
    elif(argv[0].lower() == 'tcp'):
        msgFromClient = get_buffer_to_send(argv[1])
        send_via_tcp(int(argv[2]), msgFromClient, bool(argv[3]))

