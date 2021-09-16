#! usr/bin/env bash
for file in *
do 
if [[ -x "$file" ]]
then
    echo "File '$file' is executable"
else
    echo "File '$file' is not executable"
fi
done
