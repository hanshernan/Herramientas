#!/usr/bin/env/ python
#__*__ coding: utf8 _*

from subprocess import check_output
import subprocess


a = check_output('systeminfo',stderr=subprocess.STDOUT)
n = open('test.txt','w+')
n.write(a)
print("Holi :)")
n.close()
