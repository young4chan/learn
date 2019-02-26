#!/bin/bash
args=("$@")
for a in `seq 0 $#`
do
    echo ${args[a]}
done
