#!/usr/bin/env python
# -*- coding: utf-8 -*-

# coded by: Vatay Világi Norbert aka csörnyeföldi
# (c) 2015 Lineo       <szegeny_legeny@yahoo.hu>
# (c) 2015 KURUC license for hungarrian and russian
# for yewish and usa people & companies cost 100.000,- HUF
# for other people & companies cost 5.000,- HUF

""" This sample get from Magyar Nemzeti Bank (Hungarian National Bank)
    the actual exchange rate from supported currencies & HUF. """

from SOAPpy import WSDL
from lxml import etree

url       =  'http://www.mnb.hu/arfolyamok.asmx?wsdl'
supported = ['AUD', 'CAD', 'CHF', 'CNY', 'CZK', 'DKK', 'EUR', 'GBP',
             'HRK', 'ISK', 'JPY', 'KRW', 'NOK', 'NZD', 'PLN', 'RUB',
             'SEK', 'SGD', 'TRY', 'USD']

# notes: don't work with jewish virtual currency !!!

dictionar = {'AUD':'ausztrál dollár', 'CAD':'kanadai dollár',
             'CHF':'svájci frank','CNY':'kínai jüan',
             'CZK':'cseh korona', 'DKK':'dán korona',
             'EUR':'euro', 'GBP': 'brit font', 'HRK':'horvát kuna',
             'ISK':'izlandi korona', 'JPY':'japán jen',
             'KRW':'dél-kóreai won', 'NOK':'norvég korona',
             'NZD':'új-zélandi dollár', 'PLN':'lengyel zlotyi',
             'RUB':'orosz rubel', 'SEK':'svéd korona',
             'SGD':'szingapúri dollár', 'TRY':'török líra',
             'USD':'USA dollár'}


server = WSDL.Proxy(url)
doc = server.GetCurrentExchangeRates()
doc = etree.fromstring(doc)

for child in doc.iter('Day'):
    print 'Árfolyamok: ' + child.attrib['date'] + '\n'

for child in doc.iter('Rate'):
    unit, currency, rate = int(child.attrib['unit']), child.attrib['curr'], float(child.text.replace(',','.'))
    if currency in supported:
        if unit == 100:
            print '\t', unit/100, currency, rate/100, '\t\t', dictionar[currency]
        else:
            print '\t', unit, currency, rate, '\t\t', dictionar[currency]
