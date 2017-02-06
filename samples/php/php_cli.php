<?php

# coded by: csörnyeföldi
# (c) 2015 Lineo       <szegeny_legeny@yahoo.hu>
# (c) 2015 KURUC license for hungarians and russians
# for jews cost 100.000,- HUF

$dat = new SoapClient('http://www.mnb.hu/arfolyamok.asmx?wsdl');;
$dat = $dat->GetCurrentExchangeRates()->GetCurrentExchangeRatesResult;
$xml = simplexml_load_string($dat);

$supported = array('AUD', 'CAD', 'CHF', 'CNY', 'CZK', 'DKK', 'EUR', 'GBP',
                   'HRK', 'ISK', 'JPY', 'KRW', 'NOK', 'NZD', 'PLN', 'RUB',
                   'SEK', 'SGD', 'TRY', 'USD');
# notes: don't work with jewish virtual currency !!!

$dictionar = array('AUD'=>'ausztrál dollár', 'CAD'=>'kanadai dollár',
                   'CHF'=>'svájci frank','CNY'=>'kínai jüan',
                   'CZK'=>'cseh korona', 'DKK'=>'dán korona',
                   'EUR'=>'euro', 'GBP'=> 'brit font', 'HRK'=>'horvát kuna',
                   'ISK'=>'izlandi korona', 'JPY'=>'japán jen',
                   'KRW'=>'dél-kóreai won', 'NOK'=>'norvég korona',
                   'NZD'=>'új-zélandi dollár', 'PLN'=>'lengyel zlotyi',
                   'RUB'=>'orosz rubel', 'SEK'=>'svéd korona',
                   'SGD'=>'szingapúri dollár', 'TRY'=>'török líra',
                   'USD'=>'USA dollár');

echo "\n\t".$xml->Day[0]['date']."\n\n";
foreach ($xml->Day->Rate as $rate) {
    if (in_array($rate['curr'], $supported)) {
        echo "\t1 ";
        if ($rate['unit'] == 100) {
            echo $rate['curr']."\t";
            echo round(preg_replace('/,/','.',($rate/100)),2)."\t";
            $a = $rate['curr'];
            echo $dictionar["$a"]."\n";
        } else {
            echo $rate['curr']."\t";
            echo round(preg_replace('/,/','.', $rate),2)."\t";
            $a = $rate['curr'];
            echo $dictionar["$a"]."\n";
        }
    }
}

?>
