#!/usr/bin/perl

@list = (1, 2, 3, 4, 5);
foreach $a ( @list ) {
	print "value of a = $a\n";
} continue {
	last if $a == 4;
}
