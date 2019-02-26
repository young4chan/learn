#!/bin/bash
# Declare array with 4 elements
ARRAY=('Debian Linux' 'Redhat linux' Ubuntu Linux)
# get number of elements in the array
ELEMENTS=${#ARRAY[@]}

# echo each element in array
# for loop
for i in `seq 0 $ELEMENTS`
do
    echo ${ARRAY[${i}]}
done
