#!/usr/bin/perl

$a = 0;
OUTER: while ( $a < 4 ) {
	$b = 0;
	print "value of a: $a\n";
	INNER: while ( $b < 4 ) {
		if ( $a == 2 ) {
			$a = $a + 1;
			# jump to outer loop
			next OUTER;
		}
		$b = $b + 1;
		print "value of b: $b\n";
	}
	print "\n";
	$a = $a + 1;
}
