#!/usr/bin/env python
#_*_ coding: utf8 _*_

import requests


def main():
    word = "cloudflare"
    url = requests.get("https://www.cloudflare.com/es-la/")
    cabeceras = dict(url.headers)
    verify = False
    for c in cabeceras:
        if word in cabeceras[c].lower():
            verify = True
            break

    
    if verify == True:
        print("cloudflare presente")
    else:
        print("El sitio no tiene cloudflare")

if __name__ == '__name__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
