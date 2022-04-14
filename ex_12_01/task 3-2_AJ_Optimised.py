import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import collections
collections.Callable = collections.abc.Callable
import re

def lookinguppage(ctx, url):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    return soup

#Making a function because I don't want to write a lot of code today!
def functiony(soup, theposition):
    tags = soup('a')
    url = tags[theposition].get('href', None)
    name = tags[theposition].contents[0]
    return url, name

def main():
    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    #Asking the user for input
    theposition = int(input('Which position is the name at? '))
    thetimes = int(input('How many times shall I do this? '))

    countingthetimes = 0
    name = ''

    url = 'http://py4e-data.dr-chuck.net/known_by_Lily.html'
    while countingthetimes != thetimes :
        countingthetimes = countingthetimes + 1
        soup = lookinguppage(ctx, url)
        url, name = functiony(soup, theposition-1)
    print(name)

main()
