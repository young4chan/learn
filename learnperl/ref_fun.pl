#!/usr/bin/perl

# Function definition
sub PrintHash {
	my (%hash) = @_;
	foreach $item ( keys %hash ) {
		print "Value of $item is : $hash{$item};\n"
	}
}

%hash = ('name' => 'Tom', 'age' => 19);

# Create a reference to above function.
$cref = \&PrintHash;

# Function call using reference.
&$cref(%hash);
