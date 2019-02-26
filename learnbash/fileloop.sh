#!/bin/bash
while [ ! -e myfile ]
do
    sleep 1
done
echo "myfile is created."
