#!/bin/bash
> oldFiles.txt
files=$(grep " jane " ../data/list.txt | cut -d' ' -f3)
for f in $files; do
   if test -e '/home/<username>'$f; then echo $f>>oldFiles.txt; else echo'File does not exist';fi
done
