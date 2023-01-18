<?php // php
print "hello". "\n";
$a = 10;
$b = 20;
$c = $a + $b;
$d = 2;
$c = $c / $d;
print "hello". " ". $c . "\n";
if($a > $b){
    print "The big number is " . $a. "\n";
}
else{
    print "The big number is " . $b. "\n";
}
$num = 1;
while($num <=100){
    if(($num % 2) != 0){
        $oddnum = $num;
        print "".$oddnum." ";
    }
    $num = $num + 1;
}
?>