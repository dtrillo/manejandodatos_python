#-------------------------------------------------------------------------------
# Name:        Probando BeautifulSoap en Python
#
# Copyright:   (c) David Trillo Montero 2014 - Manejandodatos.es
#-------------------------------------------------------------------------------
import time, urllib2
from cookielib import CookieJar
from urllib2 import urlopen
from bs4 import BeautifulSoup as bs

cj = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
miVersion = "Probando BeautifulSoap - version 1.0.0 http://www.manejandodatos.es"

def probandoBS():
    codigoHTML = gethtml(url) # Recupero el código HTML
    soap = bs(codigoHTML)       # Paso el código HTML a BeautifulSoap
    #print soap.title
    #print soap.title.string # findAll('title')
    tabla = soap.find('table')
    trs = tabla.findAll('tr')
    for tr in trs:
        tds = tr.findAll('td')
        #print tds
#        for td in tds: # Imprime cada TD por separado
#            print td.string
    lista = soap.findAll("ul", { "class" : "nav nav-pills" })
    print len(lista)
    for li in lista[0]: # Seleccionamos el primer elemento
        print li.string

def gethtml(url):
    """ Recupera codigo HTML a partir de URL """
    try:
        texto = opener.open (url).read()
        return texto
    except Exception, e:
        print "Error: ", str(e)
        time.sleep(2)
        return ''

url = "http://manejandodatos.es/codigo/twitterbootstrap_table.html"
if __name__ == '__main__':
    print miVersion
    probandoBS()
