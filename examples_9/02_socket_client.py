from socket import socket

def main():

    client_sock = socket()
    client_sock.connect(('localhost', 8001))

    try:
        client_sock.send('Hey you\n')
        data = client_sock.recv(1024)
        print('Server Response: "{}"'.format(data))
    finally:
        client_sock.close()


if __name__ == '__main__':
    main()

