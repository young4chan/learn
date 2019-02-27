#!/usr/bin/perl

$a = 10;

LOOP: do {
	if ( $a == 15 ) {
		# skip the iteration.
		$a = $a + 1;
		# use goto LABEL from
		goto LOOP;
	}
	print "value of a = $a\n";
	$a = $a + 1;
} while ( $a < 20 );
