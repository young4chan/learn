#!/usr/bin/perl

use lib "/d/learn/learnperl";
use Employee;

$object = new Employee( "Mohammad", "Saleem", 23234345 );
# Get first name which is set using constructor.
$firstName = $object->getFirstName();

print "Before Setting First name is : $firstName\n";

# Now Set first name using helper function.
$object->setFirstName( "Mohd. " );

# Now get first name using helper function.
$firstName = $object->getFirstName();
print "After Setting First name is : $firstName\n";
