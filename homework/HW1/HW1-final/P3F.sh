#! usr/bin/env bash
for FILE in *
do 
echo -n $FILE
cat $FILE | wc -l
done
