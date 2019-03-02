#!/usr/bin/perl

$PATH = "I am Perl Variable";

system('echo $PATH');    # Treats $PATH as shell variable
system("echo $PATH");    # Treats $PATH as Perl variable
system("echo \$PATH");   # Escaping $ works.

0;
