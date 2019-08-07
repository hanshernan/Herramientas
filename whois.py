#!/usr/bin/env/ python
#__*__ coding: utf8 _*

import requests
from bs4 import BeautifulSoup


def main():
    a = requests.get("http://whois.domaintools.com/lacuarta.com")
    soup = BeautifulSoup(a.text,'html5lib')
    for l in soup.find_all("row-label"):
        print(l.get_text())

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
