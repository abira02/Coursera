#!/usr/bin/env python3
import sys
import subprocess
input_file = sys.argv[1]
myfile = open(input_file,"r")
for file in myfile.readlines():
  old_name = file.strip()
  new_name = old_name.replace('jane','jdoe')
  print(new_name)
  subprocess.run(["mv", '/home/<username>'+old_name, '/home/<username>'+new_name])
myfile.close()
