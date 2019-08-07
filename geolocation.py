#!/usr/bin/env python
#_*_ coding: utf8 _*_

import urllib
import json


def main():
    url = "https://ipinfo.io/54.230.59.68/json"
    v = urllib.urlopen(url)
    j = json.loads(v.read())
    
    for dato in j:
        print(dato+ " : " + j [dato])
        


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()