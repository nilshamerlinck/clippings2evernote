#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from parser import RE_CLIPPING

class KnownValues(unittest.TestCase):                          
    knownValues = (
        ( u'--authors (Inconnu(e))\r\n- Votre surlignement Emplacement 307-307 | Ajout\xe9 le lundi 17 d\xe9cembre 2012 \xe0 08:27:45\r\n\r\nun portrait plut\xf4t vrai tellement il est g\xe9n\xe9raliste',
          { 'title': '--authors',
            'author': 'Inconnu(e)',
            'type': 'surlignement',
            },
          ),
        ( u'Freedom, Inc. (Brian M. Carney;Isaac Getz)\r\n- Votre surlignement sur la page 242 | Emplacement 3706-3708 | Ajout\xe9 le samedi 16 juin 2012 \xe0 22:40:52\r\n\r\nThe more people you have here, the more you have internal problems. They create their own work and they create bureaucracy. Then you need more personnel managers and you need more people just to look after your own people.\u201d',
          { 'title': 'Freedom, Inc.',
            'author': 'Brian M. Carney;Isaac Getz',
            'type': 'surlignement',
            },
          ),
        ( u'INTO THE RIVER: How Big Data, the Long Tail and Situated Cognition are Changing the World of Market Insights Forever (Cosentino, Tony)\r\n- Votre note Emplacement 1046 | Ajout\xe9 le samedi 11 ao\xfbt 2012 \xe0 22:27:39\r\n\r\ntaiste',
          { 'title': 'INTO THE RIVER: How Big Data, the Long Tail and Situated Cognition are Changing the World of Market Insights Forever',
            'author': 'Cosentino, Tony',
            'type': 'note',
            }
          ),
        ( u'INTO THE RIVER: How Big Data, the Long Tail and Situated Cognition are Changing the World of Market Insights Forever (Cosentino, Tony)\r\n- Votre signet Emplacement 1040 | Ajout\xe9 le samedi 11 ao\xfbt 2012 \xe0 22:21:55',
          { 'title': 'INTO THE RIVER: How Big Data, the Long Tail and Situated Cognition are Changing the World of Market Insights Forever',
            'author': 'Cosentino, Tony',
            'type': 'signet',
            }
          ),
        )

    def testRegex(self):
        for phrom, too in self.knownValues:
            m = RE_CLIPPING.match(phrom)
            self.assertNotEqual(m, None)
            for key in too.keys():
                self.assertEqual(m.group(key), too[key])

if __name__ == "__main__":
    unittest.main()
