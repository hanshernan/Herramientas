#!/usr/bin/env/ python
#__*__ coding: utf8 _*_

import dns.resolver
from os import path

def main():
    if path.exists('worldlist_subdomain.txt'):
        worldlist = open('worldlist_subdomain.txt','r')
        worldlist = worldlist.read().split('\n')
        lista = []
        for s in worldlist:
            try:
                a = dns.resolver.query('{}.t13.cl'.format(s),'A')
                lista.append('{}.t13.cl'.format(s))
            except:
                pass
        if len(lista) > 0:
            print('Numero de subdominios posibles: {}'.format(len(lista)))
            for e in lista:
                print(e)
        else:
            print("No se encuentran subdominios")

    else:
        print("No existe el archivo")



if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()

