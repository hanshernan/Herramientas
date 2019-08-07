#!/usr/bin/env python
#_*_ coding: utf8 _*_

import os

print("Ruta actual:" + os.getcwd())
os.chdir("/root/Control/")
print("Ruta actual:" + os.getcwd())
print(os.listdir(os.getcwd()))
#os.mkdir("pruebacurso")
#print(os.listdir(os.getcwd()))
#os.rmdir("pruebacurso")
print(os.listdir(os.getcwd()))
#os.rename('test.txt','prueba.txt')
#print(os.listdir(os.getcwd()))
print(os.stat("prueba.txt"))
os.system("ping -c 3 www.google.com")