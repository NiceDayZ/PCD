import socket
import datetime
import sys


def print_stats(protocol, number_of_packets, number_of_bytes):
    print("---Session stats " + str(datetime.datetime.now()).split('.')[0] + "---")
    print("Protocol:" + protocol)
    print("Number of Packets: " + str(number_of_packets))
    print("Number of bytes: " + str(number_of_bytes))
    print(" ")


def open_tcp_socket(bufferSize, ack=False):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("127.0.0.1", 3000))
    print("TCP server started")

    while True:
        server_socket.listen(5)
        client_socket, addr = server_socket.accept()
        print("Client connected to TCP socket")
        client_socket.settimeout(5)

        buffer_len = 0
        number_of_buffers = 0

        while True:
            try:
                message = client_socket.recv(bufferSize)

                if len(message) == 0:
                    print_stats("TCP", number_of_buffers, buffer_len)
                    client_socket.close()
                    buffer_len = 0
                    number_of_buffers = 0
                    break

                number_of_buffers += 1
                buffer_len += len(message)

                if ack:
                    client_socket.send(b'0')
            except ConnectionResetError:
                print(number_of_buffers)
                break

def open_udp_socket(bufferSize, ack=False):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.settimeout(3)
    server_socket.bind(("127.0.0.1", 3001))
    print("UDP server started")
    number_of_buffers = 0

    bufferLen = 0
    while True:
        try:
            message, addr = server_socket.recvfrom(bufferSize)
            bufferLen += len(message)
            number_of_buffers += 1

            if ack:
                server_socket.sendto(b'0', addr)

        except socket.timeout:
            if number_of_buffers > 0:
                print_stats("UDP", number_of_buffers, bufferLen)
                number_of_buffers = 0
                bufferLen = 0



if __name__ == '__main__':
    argv = sys.argv[1:]
    if len(argv) < 2:
        sys.exit(-1)

    if (argv[0].lower() == 'udp'):
        open_udp_socket(int(argv[1]), bool(argv[2]))
    elif (argv[0].lower() == 'tcp'):
        open_tcp_socket(int(argv[1]), bool(argv[2]))

