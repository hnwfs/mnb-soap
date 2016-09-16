// 2016 Forstech
// http://prog.hu/azonosito/info/Frostech0
//
// Google Táblázatnál Eszközök -> Szkriptszerkesztő, majd oda ezt (GS kód):

function getCurrency( currency ) {
    // ha nincs currency megadva, akkor USD legyen a default
    currency = currency || "USD";

    // SOAP kérés törzsének összeállítása
    var payload = '<?xml version="1.0" encoding="utf-8"?>';
    payload += '<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">';
    payload += '<soap:Body>';
    payload += '<GetCurrentExchangeRates xmlns="http://www.mnb.hu/webservices/" />';
    payload += '</soap:Body>';
    payload += '</soap:Envelope>';

    // kérés opciói: legyen POST, a post adat legyen a fenti szöveg és 2 header beállítása a SOAP kéréshez...
    var options = { "method": "post",
                    "payload": payload,
                    "headers": {'SOAPAction': "http://www.mnb.hu/webservices/GetCurrentExchangeRates",
                                'Content-Type': 'text/xml; charset=utf-8'
                                }
                   };

    // SOAP kérés elküldése...
    var result = UrlFetchApp.fetch('http://www.mnb.hu/arfolyamok.asmx', options).getContentText();

    // Ha megjött a válasz, akkor kiszedjük belőle az eredményt...
    var str = result.match(/<GetCurrentExchangeRatesResult>(.+)<\/GetCurrentExchangeRatesResult>/)[1];

    // Mivel htmlentity-vel kódolva van, így azt visszaalakítjuk (&lt; helyett < legyen)
    var decode = Xml.parse('<d>' + str + '</d>');
    var strDecoded = decode.getElement().getText();

    // ezután a dekódolt xml-ből kinyerjük a szükséges sort ami egyébként pl. így néz ki: <Rate unit="1" curr="GBP">364,04</Rate>
    var regexp = new RegExp('<Rate unit="\\d+" curr="'+ currency +'">([^<]+)</Rate>');
    var rate = strDecoded.match(regexp);

    // ha nincs találat, akkor error
    if(!rate) {
        throw new Error("Ismeretlen currency: " + currency);
    }

    // egyébként visszaadjuk az értéket
    return rate[1];
}

// ezután kattints a futtatásra - engedélyt kér a távoli eléréshez.
// Ha ez ok, akkor a táblázatba a cellába pl:
//
// =getCurrency("GBP")
