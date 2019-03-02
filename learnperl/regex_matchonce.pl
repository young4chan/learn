#!/usr/bin/perl

@list = qw/food foosball subeo footnote terfoot canic footbrdige/;

foreach (@list) {
	$first = $1 if m/(foo.*?)/;
	$last = $1 if m/(foo.*)/;
}
print "First: $first, Last: $last\n";
