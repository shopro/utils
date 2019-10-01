#! /usr/bin/env python

import os
import array as array
import sys

if (len(sys.argv)==1):
    print("usage >>seqCheck.py [fileRootName, path ('.') for cwd]")
    sys.exit()
elif (len(sys.argv)==2):
    fileRootName = sys.argv[1]
    rootpath = os.getcwd()
elif (len(sys.argv)==3):
    fileRootName = sys.argv[1]
    rootpath = os.getcwd() + sys.argv[2]
    print rootpath
else:
    print("usage >>seqCheck.py [fileRootname, path ('.') for cwd]")
'''
mypath = os.getcwd()

print("Path at terminal when executing this file")
print(os.getcwd() + "\n")

print("This file path, relative to os.getcwd()")
print(__file__ + "\n")

print("This file full path (following symlinks)")
full_path = os.path.realpath(__file__)
print(full_path + "\n")

print("This file directory and name")
path, file = os.path.split(full_path)
print(path + ' --> ' + file + "\n")

print("This file directory only")
print(os.path.dirname(full_path))
'''
f = []

for (dirpath,dirnames,filenames) in os.walk(rootpath):
        #print filenames
        f.extend(filenames)
        break

print len(f)


num = []
#narray = array("i")
for x in f:
    y = x.split(".")
    if len(y) >1:
        try:
            z =int(y[1])
        except (SyntaxError, ValueError):
            pass
        num.append(z)
    #narray.append(z)

mylist = sorted(num)
end = len(mylist)
start = mylist[0]
print("start is " + str(start))
for x in mylist:
    #print(str(x) + "   "+ str(start))
    if x != start:
        print(str(start) + " is missing")
        break
    start += 1

print("There are "+ str(end) + " files")
