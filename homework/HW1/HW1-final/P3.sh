#!/bin/bash
grep -c '[0-9]' apollo13.txt > apollo_out.txt
grep --help | grep -e '--count'
ls -lR *.py | wc -l
find . -maxdepth 2  -type f \! -perm -o+rw | wc -l
find -maxdepth 1 -type f,d \! -perm -o+rw | wc -l
