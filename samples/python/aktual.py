#!/usr/bin/env python
# -*- coding: utf-8 -*-

# code by: Világi Norbert
# (c) 2015 Lineo       <szegeny_legeny@yahoo.hu>

""" This sample get from Magyar Nemzeti Bank (Hungarian National Bank)
    the actual exchange rate from supported currencies & HUF. """

from SOAPpy import WSDL
from lxml import etree

url       =  'http://www.mnb.hu/arfolyamok.asmx?wsdl'
supported = ['AUD', 'BGN', 'BRL', 'CAD', 'CHF', 'CNY', 'CZK', 'DKK',
             'EUR', 'GBP', 'HKD', 'IDR', 'ISK', 'JPY', 'KRW', 'MXN',
             'MYR', 'NOK', 'NZD', 'PHO', 'PLN', 'RON', 'RSD', 'RUB',
             'SEK', 'SGD', 'THB', 'TRY', 'USD', 'ZAR']

dictionar = {'AUD':'ausztrál dollár',   'BGN':'bolgár leva',
             'BRL':'brazil reál',       'CAD':'kanadai dollár',
             'CHF':'svájci frank',      'CNY':'kínai jüan',
             'CZK':'cseh korona',       'DKK':'dán korona',
             'EUR':'euro',              'GBP':'brit font',
             'HKD':'homgkongi dollár',  'IDR':'indonéz rúpia',
             'ISK':'izlandi korona',    'JPY':'japán jen',
             'KRW':'dél-kóreai won',    'MXN':'mexikói peso',
             'MYR': 'maláj ringgit',    'NOK':'norvég korona',
             'NZD':'új-zélandi dollár', 'PHP':'fülöp-szigeteki peso',
             'PLN':'lengyel zlotyi',    'RON':'román lej',
             'RSD':'szerb dinár',       'RUB':'orosz rubel',
             'SEK':'svéd korona',       'SGD':'szingapúri dollár',
             'THB':'thai bát',          'TRY':'török líra',
             'USD':'USA dollár',        'ZAR':'dél-afrikai rand'}


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
