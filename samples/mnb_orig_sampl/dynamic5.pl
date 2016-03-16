#!/usr/bin/env perl

use SOAP::Lite +trace => 'debug';
#use SOAP::Lite;

my $soap = SOAP::Lite
    -> uri('http://www.mnb.hu/webservices/')
    -> on_action( sub { join '/','http://www.mnb.hu/webservices',$_[1] } )
    -> proxy('http://www.mnb.hu/arfolyamok.asmx');

my $method = SOAP::Data->name('GetExchangeRates')
    ->attr({xmlns => 'http://www.mnb.hu/webservices/'});

my @params = ( SOAP::Data->name(startDate => '2015-04-13'),
               SOAP::Data->name(endDate => '2015-04-15'),
               SOAP::Data->name(currencyNames => 'RUB,SGD'));

print $soap->call($method => @params)->result;
