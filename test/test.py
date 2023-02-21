#!/usr/bin/env python
# -*- coding: utf-8 -*-

# coded by: Világi Norbert

from mnb import test
import sys

supported = ['AUD', 'BGN', 'BRL', 'CAD', 'CHF', 'CNY', 'CZK', 'DKK',
             'EUR', 'GBP', 'HKD', 'IDR', 'ISK', 'JPY', 'KRW', 'MXN',
             'MYR', 'NOK', 'NZD', 'PHO', 'PLN', 'RON', 'RSD', 'RUB',
             'SEK', 'SGD', 'THB', 'TRY', 'USD', 'ZAR']

if __name__ == '__main__':
    if len(sys.argv) <> 2:
        print sys.argv[0], '<currency_code>'
    elif sys.argv[1].upper() not in supported:
        print '\n\t invalid currency code:', sys.argv[1].upper()
    else:
        teszt(sys.argv[1].upper())
