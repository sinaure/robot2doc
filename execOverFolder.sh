#!/bin/bash
EXCLUDE=""
SOL="SOL00Y"
COMMIT=""
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
	if [ "$4" != "" ]; then
		SOL=$4
	else
		echo "No configured commit id"
	fi

	API=$(basename $DIR)
	echo "api: $API"
	for file in $DIR/*.robot; do
		filename=$(basename "$file")
		if [[ $filename != *"$EXCLUDE"* ]]; then
			python robot2doc/main.py $file "${filename%.*}.docx" "${filename%.*}" $COMMIT $SOL $API
		else
			echo "excluded file: $filename"	
		fi
	done
else
    echo "Enter a directory"
fi

