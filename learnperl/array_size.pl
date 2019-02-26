#!/usr/bin/perl

@array = (1, 2, 3);
print "Size: ", scalar @array, "\n";

$array[50] = 4;
$size = @array;
$max_index = $#array;

print "Size: $size\n";
print "Max index: $max_index\n";
