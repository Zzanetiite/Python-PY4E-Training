import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import collections
collections.Callable = collections.abc.Callable

import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def lookinguppage():
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    return soup

#Asking the user for input
theposition = int(input('Which position is the name at? '))
thetimes = int(input('How many times shall I do this? '))

countingthetimes = 0

url = 'http://py4e-data.dr-chuck.net/known_by_Lily.html'

#Making a function because I don't want to write a lot of code today!
def functiony():

    tags = soup('a')
    counter = 0
    for tag in tags:
        y = tag.get('href', None)
        name = tag.contents[0]
        counter = counter + 1
        if counter == theposition :
            url = y
            break
    return url, name

while countingthetimes != thetimes :
    countingthetimes = countingthetimes + 1
    soup = lookinguppage()
    url, name = functiony()

print(name)
