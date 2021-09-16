#! usr/bin/env bash
read -r -p "What file do you want to commit? " filename
git add $filename
git status
read -n1 -p "Do you want to continue? (Y or N) " continue
if [[ $continue == "Y" ]]
then 
	read -p "\nWhat is the commit message? " message
	git commit -m "$message"
	git status
	read -n1 -p "Do you want to continue? (Y or N) " continue2
	if [[ $continue2 == "Y" ]]
	then
		git push
	else
		exit 1
	fi
else
	exit 1
fi
done 
 
