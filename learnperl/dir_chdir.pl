#!/usr/bin/perl

$dir = "/d";

# This changes perl directory and moves you inside /home directory.
chdir( $dir ) or die "Couldn't go inside $dir directory, $!";
print "Your new location is $dir\n";
