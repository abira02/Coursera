#!/bin/bash
> oldFiles.txt
files=$(grep " jane " ../data/list.txt | cut -d' ' -f3)
for f in $files; do
   if test -e $HOME$f; then echo $HOME$f>>oldFiles.txt; else echo $HOME$f' : this file does not exist';fi
done
