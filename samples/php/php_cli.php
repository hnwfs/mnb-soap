<?php

# coded by: Világi Norbert
# (c) 2015 Lineo       <szegeny_legeny@yahoo.hu>

$dat = new SoapClient('http://www.mnb.hu/arfolyamok.asmx?wsdl');;
$dat = $dat->GetCurrentExchangeRates()->GetCurrentExchangeRatesResult;
$xml = simplexml_load_string($dat);

$supported = array('AUD', 'BGN', 'BRL', 'CAD', 'CHF', 'CNY', 'CZK', 'DKK',
             'EUR', 'GBP', 'HKD', 'IDR', 'ISK', 'JPY', 'KRW', 'MXN',
             'MYR', 'NOK', 'NZD', 'PHO', 'PLN', 'RON', 'RSD', 'RUB',
             'SEK', 'SGD', 'THB', 'TRY', 'USD', 'ZAR');


$dictionar = array('AUD'=>'ausztrál dollár',   'BGN'=>'bolgár leva',
                   'BRL'=>'brazil reál',       'CAD'=>'kanadai dollár',
                   'CHF'=>'svájci frank',      'CNY'=>'kínai jüan',
                   'CZK'=>'cseh korona',       'DKK'=>'dán korona',
                   'EUR'=>'euro',              'GBP'=>'brit font',
                   'HKD'=>'homgkongi dollár',  'IDR'=>'indonéz rúpia',
                   'ISK'=>'izlandi korona',    'JPY'=>'japán jen',
                   'KRW'=>'dél-kóreai won',    'MXN'=>'mexikói peso',
                   'MYR'=> 'maláj ringgit',    'NOK'=>'norvég korona',
                   'NZD'=>'új-zélandi dollár', 'PHP'=>'fülöp-szigeteki peso',
                   'PLN'=>'lengyel zlotyi',    'RON'=>'román lej',
                   'RSD'=>'szerb dinár',       'RUB'=>'orosz rubel',
                   'SEK'=>'svéd korona',       'SGD'=>'szingapúri dollár',
                   'THB'=>'thai bát',          'TRY'=>'török líra',
                   'USD'=>'USA dollár',        'ZAR'=>'dél-afrikai rand');

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
