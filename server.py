import socket
import argparse
from threading import *
from random import randint


def get_window_size():
    return randint(3,10)


def main():

    parser = argparse.ArgumentParser(description='Get server info.')
    parser.add_argument('-p', help='port to listen on', type=int)
    parser.add_argument('-a', help='hostname or ip', type=str)

    args = vars(parser.parse_args())

    if args['p']:
        port = args['p']
    else:
        port = 5001

    if args['a']:
        hostName = args['a']
    else:
        hostName = '127.0.0.1'

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sAddr = (hostName, port)

    print('Starting server on: ' + hostName + ' on port: ' + str(port) + '.')

    sock.bind(sAddr)
    sock.listen(2)

    while True:
        #Do stuff
        connection, cAddr = sock.accept()
        try:
            #stuff

        finally:
            connection.close()