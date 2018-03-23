#!/bin/bash

classe=$1
project=$2

cd classes/$1

for eleve in *\.*
do
    mkdir $eleve/$project
done

