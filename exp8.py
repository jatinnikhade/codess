import os.path
import sys

fname= input("enter the filename")
if not os .path.isfile (fname):
    print("file", fname,"dose not exists")
    sys.exit(0)

infile = open(fname,"r")
linelist =infile.readlines()

for i in range(0):
      print(i+1, ":", linelist[i])
word =input("enter a word")
cnt=0
for line in linelist:
     cnt+= line.count(word)
     print("the word",word,"appears",cnt,"tmes in the file")
           
               


