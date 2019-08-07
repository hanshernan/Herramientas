#!/usr/bin/env/ python
#__*__ coding: utf8 _*_

import dns.renderer

def main():

    try: 
        a = dns.resolver.query("ciisa.cl","ANY")
        for q in a:
            print(q)

    except:
        print("No puede obtener la consulta")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
