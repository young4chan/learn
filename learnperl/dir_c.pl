#!/usr/bin/perl

opendir(DIR, '.') or die "Couldn't open directory, $!";
foreach(sort grep(/^.*\.c$/, readdir(DIR))) {
	print "$_\n";
}
closedir DIR;
