#!/usr/bin/perl

@names = ('John Paul', 'Lisa', 'Kumar', 1, (a, b, c));

@copy = @names;
$size = @names;

print "Given names are : @copy\n";
print "Number of names are : $size\n";
