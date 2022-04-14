import urllib.request, urllib.parse, urllib.error
import ssl
import collections
collections.Callable = collections.abc.Callable

import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
#$input('Enter location: ')

print('Retrieving', url)
html = urllib.request.urlopen(url, context=ctx).read().decode()
print('Retrieved', len(html), 'characters')

# print(html)

js = json.loads(html)
#print('count:', len(js))

counter = 0
sum = 0
numbers = list()

for comment in js['comments']:
    counter = counter + 1
    number = comment['count']
    #print(number)
    sum = sum + number

print('Count:', counter)
print('Sum:', sum)
