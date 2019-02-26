#!/bin/bash
trap bashtrap INT
clear
bashtrap(){
    echo "CTRL+C dectected"
}
for i in `seq 1 20`
do
    echo $i
    sleep 1
done
