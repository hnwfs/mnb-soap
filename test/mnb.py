# -*- coding: utf-8 -*-

# coded by: Világi Norbert
# (c) 2015 Lineo <szegeny_legeny@yahoo.hu>

# 2023 02.21 revision - actualisation

from lxml import html
from urllib2 import urlopen

url = 'https://www.mnb.hu/arfolyamok'

def get_currency_exchange():
    d = urlopen(url)
    a = html.parse(d)
    b = {}

    for t in a.xpath('//div[@class="c-txt"]'):
        for i in t.xpath('//table/tbody/tr'):
            b[str(i.xpath('td/text()')[0])] = i.xpath('td/text()')
            b[str(i.xpath('td/text()')[0])].append(i.xpath('td/text()')[0])

    return b



def = test(cur_code):
    i = get_currency_exchange()[cur_code]
    print '\n\t' + i[2] + ' ' + i[1] + ' = ' +i[3] + ' forint'