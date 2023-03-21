# -*- coding: utf-8 -*-

from pysimplesoap.client import SoapClient
import xml.etree.ElementTree as ET

class getCurrencyRate(object):
    def __init__(self):
        url      = 'http://www.mnb.hu/arfolyamok.asmx?wsdl'
        self.client   = SoapClient(wsdl = url)

    def getActual(self, cur):
        client   = self.client
        respon   = client.GetCurrentExchangeRates()
        response = ET.fromstring(respon['GetCurrentExchangeRatesResult'])

        for child in response.iter('Rate'):
            unit, currency, rate = int(child.attrib['unit']), child.attrib['curr'], float(child.text.replace(',','.'))
            if currency == cur.upper():
                if unit == 100:
                    return "{0:.4f}".format(rate/100)
                else:
                    return rate

    def getCurrencies(self):
        client   = self.client
        respon   = client.GetCurrentExchangeRates()
        response = ET.fromstring(respon['GetCurrentExchangeRatesResult'])
        a        = []

        for child in response.iter('Rate'):
            a.append(child.attrib['curr'])
        return a

    def getHistoricalData(self, startdate, enddate, currency):
        client   = self.client
        respon   = client.GetExchangeRates(startdate, enddate, currency)
        response = ET.fromstring(respon['GetExchangeRatesResult'])
        a, b = ([] for _ in range(2))
        for child in response.iter('Day'):
            b.append(child.attrib['date'])
            for d in child.iter('Rate'):
                c = float(d.text.replace(',','.'))
                if int(d.attrib['unit']) == 100:
                    c = c/100
                b.append(c)
            a.append(b)
            b = []
        return a

