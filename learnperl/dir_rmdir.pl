#!/usr/bin/perl

$dir = "/d/learn/learnperl/perl";

# This removes perl directory form /tmp directory.
rmdir( $dir ) or die "Couldn't remove $dir directory, $!";
print "Directory removed successfully\n";
