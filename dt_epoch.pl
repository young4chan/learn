#!/usr/bin/perl

$epoc = time();

print "Number of seconds since Jan 1, 1970 - $epoc\n";

$datestring = localtime();
print "Current date and time $datestring\n";

$epoc = time();
$epoc -= 24 * 60 * 60;	# one day before current date

$datestring = localtime($epoc);
print "Yesterday's date and time $datestring\n";
