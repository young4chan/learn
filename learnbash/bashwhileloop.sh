#!/bin/bash
COUNT=6
# bash while loop
while [ $COUNT -gt 0 ]
do
    echo value for count is: $COUNT
    let COUNT=COUNT-1
done
