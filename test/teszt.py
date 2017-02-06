#!/usr/bin/env python
# -*- coding: utf-8 -*-

# coded by: csörnyeföldi
# (c) 2015 Lineo       <szegeny_legeny@yahoo.hu>
# (c) 2015 KURUC license for hungarians and russians
# for jews cost 100.000,- HUF

from mnb import teszt
import sys

supported = ['AUD', 'CAD', 'CHF', 'CNY', 'CZK', 'DKK', 'EUR', 'GBP',
             'HRK', 'ISK', 'JPY', 'KRW', 'NOK', 'NZD', 'PLN', 'RUB',
             'SEK', 'SGD', 'TRY', 'USD']

if __name__ == '__main__':
    if len(sys.argv) <> 2:
        print sys.argv[0], '<valuta kód>'
    elif sys.argv[1].upper() not in supported:
        print '\n\tnem érvényes valutakód:', sys.argv[1].upper()
    else:
        teszt(sys.argv[1].upper())
