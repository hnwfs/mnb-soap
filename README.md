# MNB SOAP client module

## Background

MNB exposes a publicly available exchange rate API as a SOAP service where they publish their official daily rate between Hungarian Forint (HUF) and most other currencies.

The official documentation of their API is available here [in hungarian](https://www.mnb.hu/letoltes/aktualis-es-a-regebbi-arfolyamok-webszolgaltatasanak-dokumentacioja-1.pdf) or [in english](https://www.mnb.hu/letoltes/documentation-on-the-mnb-s-web-service-on-current-and-historic-exchange-rates.pdf)

## Installation

  python setup.py install

  or you can install it with any PyPI-compatible package manager

  pip install mnb-soap

## Sample:

```python

from mnb import getCurrencyRate

a = getCurrencyRate()

print (a.getCurrencies())
print ('1 japán yen = {} hungarian forint', a.getActual('JPY'))
print (a.getHistoricalData('2023-03-01','2023-03-20','JPY'))
end
```
# Python version:

    Programming Language :: Python :: 2.7
    Programming Language :: Python :: 3
    Programming Language :: Python :: 3.5
    Programming Language :: Python :: 3.6
    Programming Language :: Python :: 3.7
    Programming Language :: Python :: 3.8
    Programming Language :: Python :: 3.9

# History:

  **2023-03-21** ver 0.1
             rewrited to module
             old branch moved to: 0.0.1 alpha

  **2023-02-24** actualisation

  **2017-02-06** rewrited test.py scrapper
