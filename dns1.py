#!/usr/bin/env/ python
#__*__ coding: utf8 _*_

import dns.resolver

def main():
    consultas = ['A','AAAAA', 'NS', 'SOA', 'MX', 'MF','TXT']
    for c in consultas:
        try:
            a = dns.resolver.query("ciisa.cl",c)
            for q in a:
                print(q)

        except:
            print("No puede obtener la consulta")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()