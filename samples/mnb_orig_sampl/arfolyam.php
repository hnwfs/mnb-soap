<?php
require_once('lib/nusoap.php');
//$proxyhost = isset($_POST['proxyhost']) ? $_POST['proxyhost'] : '';
//$proxyport = isset($_POST['proxyport']) ? $_POST['proxyport'] : '';
//$proxyusername = isset($_POST['proxyusername']) ? $_POST['proxyusername'] : '';
//$proxypassword = isset($_POST['proxypassword']) ? $_POST['proxypassword'] : '';
//$client = new nusoap_client('http://www.mnb.hu/arfolyamok.asmx?WSDL', 'wsdl', $proxyhost, $proxyport, $proxyusername, $proxypassword);
$client = new nusoap_client('http://www.mnb.hu/arfolyamok.asmx?WSDL', 'wsdl', '', '', '', '');

$err = $client->getError();
if ($err) {
	echo '<h2>Constructor error</h2><pre>' . $err . '</pre>';
}
// Doc/lit parameters get wrapped
$param = array('startDate' => '2008-12-01', 'endDate' => '2008-12-30', 'currencyNames' => 'USD,EUR,AUD');
$result = $client->call('GetExchangeRates', array('parameters' => $param), '', '', false, true);
//$result = $client->call('GetInfo', '', '', '', false, true);
// Check for a fault
if ($client->fault) {
	echo '<h2>Fault</h2><pre>';
	print_r($result);
	echo '</pre>';
} else {
	// Check for errors
	$err = $client->getError();
	if ($err) {
		// Display the error
		echo '<h2>Error</h2><pre>' . $err . '</pre>';
	} else {
		// Display the result
//		echo '<h2>Result</h2><pre>';
//		print_r($result);
//		echo '</pre>';
	}
}
//echo '<h2>Request</h2><pre>' . htmlspecialchars($client->request, ENT_QUOTES) . '</pre>';
//echo '<h2>Response</h2><pre>' . htmlspecialchars($client->response, ENT_QUOTES) . '</pre>';
//echo '<h2>Debug</h2><pre>' . htmlspecialchars($client->debug_str, ENT_QUOTES) . '</pre>';
$tr = new nusoap_parser($result[GetExchangeRatesResult]);
$trr = $tr->message;
$elso = 1;
$ido = '';
$elso_tmp = '';
foreach ($trr as $tri) {
    if ($tri['name'] == 'Day') {
	$ido = $tri['attrs']['date'];
	if ($elso == 2) {
	    echo '</tr>';
	    $elso_tmp .= '</tr>';
	    echo $elso_tmp;
	    $elso = 3;
	}
	elseif ($elso == 4) {
	    echo '</tr>';
	    $elso = 3;
	}
    }
    elseif ($tri['name'] == 'Rate') {
	if ($elso == 1) {
	    echo '<table><tr>';
	    echo '<td>Date</td>';
	    echo '<td>' . $tri['attrs']['curr'] . '<br>';
	    echo $tri['attrs']['unit'] . '</td>';
	    $elso_tmp = '<tr><td>' . $ido . '</td><td>' . $tri['cdata'] . '</td>';
	    $elso = 2;
	}
	elseif ($elso == 2) {
	    echo '<td>' . $tri['attrs']['curr'] . '<br>';
	    echo $tri['attrs']['unit'] . '</td>';
	    $elso_tmp .= '<td>' . $tri['cdata'] . '</td>';
	}
	elseif ($elso == 3) {
	    echo '<tr><td>' . $ido . '</td><td>' . $tri['cdata'] . '</td>';
	    $elso = 4;
	}
	elseif ($elso == 4) {
	    echo '<td>' . $tri['cdata'] . '</td>';
	}
    }
}
echo '</tr></table>';