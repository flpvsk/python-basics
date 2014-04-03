from socket import socket

def main():
    server_sock = socket()
    server_sock.bind(('', 8001))
    server_sock.listen(1)

    try:
        conn, addr = server_sock.accept()
        print('Client connected from {}'.format(addr))

        try:
            data = ''
            while True:
                data += conn.recv(1024)
                if not data:
                    break

                if '\n' not in data:
                    continue

                print('Got data from {}'.format(addr))
                conn.send('Got: {}'.format(data))
                data = ''

        finally:
            print('Connection from {} closed'.format(addr))
            conn.close()

    finally:
        server_sock.close()

if __name__ == '__main__':
    main()

