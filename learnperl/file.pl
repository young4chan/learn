#!/usr/bin/perl

open (DATA, "<file.txt") or die "Couldn't open file file.txt, $!";

while (<DATA>) {
	print "$_";
}

$pd = close(DATA) || die "Couldn't close file properly";
if ( $pd )
{
	print "file's closed properly\n";
} else {
	print "file's not closed yet\n";
}
