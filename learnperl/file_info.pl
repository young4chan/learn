#!/usr/bin/perl

my $file = "/d/learn/learnperl/file2.txt";
my (@description, $size);
if (-e $file) {
	push @description, 'binary' if (-B _);
	push @description, 'a socket' if (-S _);
	push @description, 'a text file' if (-T _);
	push @description, 'a block special file' if (-b _);
	push @description, 'a directory' if (-d _);
	push @description, 'executable' if (-x _);
	push @description, (($Size = -s _)) ? "$Size bytes" : 'empty';
	print "$file is ", join(', ', @description), "\n";
}
