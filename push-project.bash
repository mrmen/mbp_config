#!/bin/bash

classe=$1
file=$2

mkdir ~/mpoint

mount -t smbfs //tho.etchever:271828@admin_groupes/$classe ~/mpoint

sleep 1s

cd ~/mpoint

for eleve in *\.*
do
    cp $file $eleve
done
    
cd ~
umount ~/mpoint



