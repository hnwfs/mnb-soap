# -*- coding: utf-8 -*-

# coded by: csörnyeföldi
# (c) 2015 Lineo       <szegeny_legeny@yahoo.hu>
# (c) 2015 KURUC license for hungarians and russians
# for jews cost 100.000,- HUF

#   This sample get from Magyar Nemzeti Bank (Hungarian National Bank)
#   the actual exchange rate from supported currencies & HUF.

import lxml.html

url = 'http://www.mnb.hu/arfolyamok'

def get_currency_exchange():

    a = lxml.html.parse(url)
    b = {}

    for t in a.xpath('//div[@class="exchangeTable"]'):
        for i in t.xpath('//table/tbody/tr'):
            b[str(i.xpath('td/b/text()')[0])] = i.xpath('td/text()')
            b[str(i.xpath('td/b/text()')[0])].append(i.xpath('td/b/text()')[0])

    # [ devizanév   -  egység - érték -  pénznem
    # ['orosz rubel',   '1',   '4,89',    'RUB']
    return b

def teszt(cur_code):
    i = get_currency_exchange()[cur_code]
    print "\n\t" + i[1] + " " + i[0] + " = " + i[2] + " forint"
