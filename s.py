#!/usr/bin/env/ python
#__*__ coding: utf8 _*_

import sys
from shodan import Shodan


reload(sys)
sys.setdefaultencoding('UTF8')
key = "ZDyQupa9DlQ0AI3o6AyicRDfz0c8BisZ"

motor = Shodan(key)
try:
    query = motor.search("struts")
    print("Total de resultados: {}".format(['total']))
    for host in query ['matches']:
        print("IP : {}".format(host['ip_str']))
        print("Puerto: {}".format(host['port']))
        print("ORG: {}".format(host['org']))
        try:
            print("ASN: {}".format(host['asn']))
        except:
            pass
        for l in host['location']:
            print(l + ": " +str(host['location'][l]))
except:
    print("Ocurrio un error")

