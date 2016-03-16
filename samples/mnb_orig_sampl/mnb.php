<?php

$bdy = "<?xml version=\"1.0\" encoding=\"utf-8\"?>";
$bdy.= "<soap:Envelope xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:soap=\"http://schemas.xmlsoap.org/soap/envelope/\">";
$bdy.= "<soap:Body>";
$bdy.= "<GetCurrentExchangeRates xmlns=\"http://www.mnb.hu/webservices/\" />";
$bdy.= "</soap:Body>";
$bdy.= "</soap:Envelope>\r\n";

$req = "POST /arfolyamok.asmx HTTP/1.1\r\n";
$req.= "Host: www.mnb.hu\r\n";
$req.= "Connection: Close\r\n";
$req.= "Content-Type: text/xml; charset=utf-8\r\n";
$req.= "Content-Length: ".strlen($bdy)."\r\n";
$req.= "SOAPAction: \"http://www.mnb.hu/webservices/GetCurrentExchangeRates\"\r\n\r\n";

$fs = fsockopen("www.mnb.hu", 80);
fwrite($fs, $req.$bdy);
while (!feof($fs)) {
    $s = fgets($fs);
    echo $s."<BR/>";
}
fclose($fs);
?>
