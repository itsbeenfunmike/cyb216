#!/bin/usr/python

import pprint
import requests
MAC_URL = 'http://macvendors.co/api/%s'
r = requests.get(MAC_URL % 'BC:92:6B:A0:00:01')
pprint.pprint(r.json())
{'result': {'address': '1 Infinite Loop Cupertino CA US 95014 ',
            'company': 'Apple, Inc.',
'mac_prefix': 'BC:92:6B'}}
