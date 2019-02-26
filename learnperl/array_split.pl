#!/usr/bin/perl

# define Strings
$var_string = "Rain-Drops-On-Roses-And-Whisker-On-Kittens";
$var_names = "Larry,David,Roger,Ken,Michael,Tom";

# transform above strings into arrays.
@string = split('-', $var_string);
@names = split(',', $var_names);

print "$string[3]\n";    # This will print Roses
print "$names[4]\n";     # This will print Michael

$string1 = join('-', @string);
$string2 = join('-', @names);

print "$string1\n";
print "$string2\n";
