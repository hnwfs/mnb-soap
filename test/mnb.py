#!/usr/bin/env python
# -*- coding: utf-8 -*-

import lxml.html, sys

supported = ['AUD', 'CAD', 'CHF', 'CNY', 'CZK', 'DKK', 'EUR', 'GBP',
             'HRK', 'ISK', 'JPY', 'KRW', 'NOK', 'NZD', 'PLN', 'RUB',
             'SEK', 'SGD', 'TRY', 'USD']

if len(sys.argv) <> 2:
    print sys.argv[0], '<valuta kód>'
elif sys.argv[1].upper() not in supported:
    print '\n\tnem érvényes valuta kód:', sys.argv[1].upper()
else:
    val = 'td[3]/text()'
    cur = 'td[4]/text()'
    txt = 'td[2]/text()'
    cod = sys.argv[1].upper()

    url = 'http://www.mnb.hu/arfolyamok'
    table = lxml.html.parse(url)
    for trs in table.xpath('//table[@class="datatable"]/tbody'):
        for i in trs.xpath('tr'):
            if i.xpath('td[0]/text()')[0] == cod:
                print '\n\t', i.xpath(val)[0], (i.xpath(txt)[0]), i.xpath(cur)[0], 'forint'
