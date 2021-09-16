#! usr/bin/env bash
read -r -p $'What file do you want to commit?\n' filename
git add $filename
git status
read -n1 -p $'Do you want to continue? (Y or N)\n' continue
if [[ $continue == "Y" ]]
then 
	read -p $'\nWhat is the commit message?\n' message
	git commit -m "$message"
	git status
	read -n1 -p $'\nDo you want to continue? (Y or N)\n' continue2
	if [[ $continue2 == "Y" ]]
	then
		git push
	else
		exit 1
	fi
else
	exit 1
fi 
