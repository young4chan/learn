#!/usr/bin/perl

format EMPLOYEE = 
==================================
@<<<<<<<<<<<<<<<< @<<
$name $age
@#####.##
$salary
==================================
.

format EMPLOYEE_TOP =
==================================
Name              Age
==================================
.

format EMPLOYEE_BOTTOM =
End of Page @<
            $%
.

select(STDOUT);
$~ = EMPLOYEE;
$^ = EMPLOYEE_TOP;
$- = EMPLOYEE_BOTTOM;

@n = ("Ali", "Raza", "Jaffer");
@a = (20, 30, 40);
@s = (2000.00, 2500.00, 4000.000);

$i = 0;
foreach (@n) {
	$name = $_;
	$age = $a[$i];
	$salary = $s[$i++];
	write;
}
