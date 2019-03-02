#!/usr/bin/perl

$dir = "/d/learn/learnperl/perl";

# This removes perl directory from /d/learn/learnperl/perl directory.
mkdir( $dir ) or die "Couldn't create $dir directory, $!";
print "Directory created successfully\n";
