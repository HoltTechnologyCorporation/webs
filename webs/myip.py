#!/usr/bin/env python
from six.moves.urllib.request import urlopen
import json

def detect_ip():
    data = urlopen('http://getip.io/?format=json').read()
    ip = json.loads(data)['ip']
    #country = g.doc.select('//b[contains(text(), "Your Country")]')\
    #           .text(default='').split(':')[-1].strip()
    #return '%s - %s' % (ip, country)
    return '%s' % ip


def main():
    print(detect_ip())
