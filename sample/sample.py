# -*- coding: utf-8 -*-

from mnb import getCurrencyRate

a = getCurrencyRate()

print (a.getCurrencies())
print ('1 japán yen = {} hungarian forint', a.getActual('JPY')))
print (a.getHistoricalData('2023-03-01','2023-03-20','JPY'))

