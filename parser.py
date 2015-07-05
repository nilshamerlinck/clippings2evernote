#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Inspiré par https://github.com/albins/kindle-clippings-parser/
# Mais j'ai choisi une approche différente, basée sur une regex

import codecs, locale, os, sys
import traceback
if sys.stdout.encoding != 'UTF-8':
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout)

from datetime import datetime
import re

DEBUG = True

'''
Dans le cas d'un signet, pas de content.
'''
RE_CLIPPING = re.compile(ur'''
(?P<title>.+)\s\((?P<author>.+)\)
\s+
-\sVotre\s(?P<type>surlignement|note|signet)\s(?P<location>(?P<page>sur\sla\spage\s\d+\s\|\s)?Emplacement\s[\d-]+)\s\|\sAjouté\sle\s(?P<date>.+)
\s*
(?P<content>.*)
''', re.UNICODE | re.MULTILINE | re.VERBOSE)

# TODO
# DATEFORMAT = samedi 11 août 2012 à 22:27:39
# datetime.strptime(d, 

class MyClippingsParser(object):

    def __init__(self, f):
        self.fp = codecs.open(f, 'r', "utf-8-sig") # BOM

    def parse(self):
        clippings = [ n.strip() for n in (self.fp.read().split("\n==========")) ]

        return (self.parse_clipping(clipping) for clipping in clippings if clipping != '')

    def parse_clipping(self, clipping):
        m = RE_CLIPPING.match(clipping)
        if m:
            return { 'type': m.group('type'),
                     'title': m.group('title'),
                     'author': m.group('author'),
                     'content': m.group('content'),
                     }                     
        elif DEBUG:
            #print repr(clipping)
            return {}

if __name__ == '__main__':

    parser = MyClippingsParser(sys.argv[1])
    for c in parser.parse():
        if c and c['type'] == 'surlignement' and 'Boris' in c['title']:
            #print c['author'], c['title'], c['content']
            print c['content']
