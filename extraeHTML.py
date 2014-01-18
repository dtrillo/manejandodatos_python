#-------------------------------------------------------------------------------
# Name:        Extraer código HTML en Python
#
# Copyright:   (c) David Trillo Montero 2014 - Manejandodatos.es
#-------------------------------------------------------------------------------
import time, urllib2

def gethtml(url):
    try:
        req = urllib2.Request(url)
        return urllib2.urlopen(req).read()
    except Exception, e:
        time.sleep(2)
        return ''

url = 'http://www.manejandodatos.es'
print gethtml(url)
