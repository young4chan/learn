#!/usr/bin/perl

# define an array
@foods = qw\pizza steak chicken burgers\;
print "Before: @foods\n";

# sort this array
@foods = sort(@foods);
print "After: @foods\n";

$[ = 1;

print "Food at \@foods[1]: $foods[1]\n";
print "Food at \@foods[2]: $foods[2]\n";
