#! /bin/bash

read -p "Enter filename:" file

if [ -f "$file" ]
then
	tail 10 $file
else
	echo "File is not found"
fi

