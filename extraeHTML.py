#-------------------------------------------------------------------------------
# Name:        Extraer código HTML en Python
#
# Copyright:   (c) David Trillo Montero 2014 - Manejandodatos.es
#-------------------------------------------------------------------------------
import time, cookielib, urllib2, difflib
from cookielib import CookieJar
from urllib2 import urlopen

cj = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent', 'Mozilla/5.0')]

def gethtml(url):
    try:
        return opener.open (url).read()
    except Exception, e:
        print str(e)
        time.sleep(5)
    return ''

url = 'http://www.manejandodatos.es'
print gethtml(url)
