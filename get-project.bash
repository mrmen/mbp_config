#!/bin/bash
classe=$1
project=$2

mount -t smbfs //tho.etchever:271828@admin_groupes/$classe ~/mpoint

sleep 1s

td=$(date +"%Y-%m-%d")
DEST="/Users/mrmen/"$td"_"$classe"_"$project
mkdir $DEST
cd ~/mpoint

for eleve in *\.*
do
    name=$(echo $eleve | sed 's/\./_/g')
    # Si plus d'un fichier création d'un dossier au nom de l'eleve
    shopt -s nullglob
    numfiles=($eleve/$project/*)
    numfiles=${#numfiles[@]}
    # dossier non vide
    if (($numfiles))
    then
	mkdir $DEST/$name
	cp $eleve/$project/* $DEST/$name/
    fi

done
    
cd ~
umount ~/mpoint



