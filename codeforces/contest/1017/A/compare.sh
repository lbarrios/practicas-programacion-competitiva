#!/usr/bin/env bash

FILES_INPUT=input/*.txt
EXEC=A.py

for i in $FILES_INPUT; do
	name=$(echo $i | cut -d'/' -f2)

	echo "Testeando $name..."
	diff <(python3 $EXEC < "input/$name") "output/$name"

	if [ "$?" == "0" ]; then
		echo "Los output son iguales"
	else
		echo "Los output difieren"
	fi

	echo ""

done
