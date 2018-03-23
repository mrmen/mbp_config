input=$1

cat $input | sed '/Élèves/d' | sed 's/\"//g' | sed 's/Évaluation : Maîtrise insuffisante/0/g' | sed 's/Évaluation : Maîtrise fragile/1/g' | sed 's/Évaluation : Maîtrise satisfaisante/2/g'| sed 's/Évaluation : Très bonne maîtrise/3/g' | sed 's/	/,/g' | sed 's/Évaluation : Absent/a/g' | sed 's/Évaluation : Non évalué/N.E./g' | sed 's/,/;/g'
