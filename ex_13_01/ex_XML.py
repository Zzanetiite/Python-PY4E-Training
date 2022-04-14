import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
import collections
collections.Callable = collections.abc.Callable

import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')

print('Retrieving', url)
html = urllib.request.urlopen(url, context=ctx).read().decode()
print('Retrieved', len(html), 'characters')
tree = ET.fromstring(html)

comments = tree.findall('comments')
counts = list()

amount = 0

for comment in comments[0] :
    count = comment.find('count').text
    amount = amount + 1
    counts.append(int(count))

print('Count:',amount)
print('Sum:',sum(counts))
