#!/bin/bash

# Declare bash string variable
BASH_VAR="Bash Script"

# echo variable BASH_VAR
echo $BASH_VAR

# meta characters special meaning in bash is suppressed when using single quote
echo '$BASH_VAR "$BASH_VAR"'
