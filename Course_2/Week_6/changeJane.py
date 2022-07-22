#!/usr/bin/env python3
import sys
import subprocess

myfile = open("oldFiles.txt","r")
for file in myfile.readlines():
  old_name = file.strip()
  new_name = old_name.replace('jane','jdoe')
  print(new_name)
  subprocess.run(["mv", '/home/<username>'+old_name, '/home/<username>'+new_name])
myfile.close()
