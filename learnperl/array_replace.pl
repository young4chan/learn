#!/usr/bin/perl

@nums = (1..20);
print "Before - @nums\n";
splice(@nums, 5, 5, 16..20);
print "After - @nums\n";
