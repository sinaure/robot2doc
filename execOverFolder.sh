#!/bin/bash
EXCLUDE=""
if [ "$1" != "" ]; then
	DIR=$1
	if [ "$2" != "" ]; then
		EXCLUDE=$2
	else
		echo "No configured exclusions"
	fi
	if [ "$3" != "" ]; then
		COMMIT=$3
	else
		echo "No configured commit id"
	fi
		
	for file in $DIR/*.robot; do
		filename=$(basename "$file")
		if [[ $filename != *"$EXCLUDE"* ]]; then
			python robot2doc/main.py $file "${filename%.*}.docx" "${filename%.*}" $COMMIT
		else
			echo "excluded file: $filename"	
		fi
	done
else
    echo "Enter a directory"
fi

