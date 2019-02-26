#!/usr/bin/perl

$a = 20;
# check the boolean condition using unless statement
unless ( $a == 20 ) {
	# if condition is false then print the following
	printf "a has a value which is not 20\n";
} elsif ( $a == 30 ) {
	# if condition is true then print the following
	printf "a has a value which is 30\n";
} else {
	# if none of the above conditions is met
	printf "a has a value which is $a\n";
}
