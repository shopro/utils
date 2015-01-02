#! /usr/bin/env python


# part of "newstuff" fork

import os
import array as array

import string

print( "hello" + " STRANGER")

#mypath = '/store/20136_ROCKDOG/assets/development/FxDev/fx/waterFloat/gravity_field/v0019'
mypath = os.getcwd()

'''
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
for (dirpath,dirnames,filenames) in os.walk(mypath):
        #print filenames
        f.extend(filenames)
        break
        
print len(f)

num = []
#narray = array("i")
for x in f:
    y = x.split(".")
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




count = 0






#x = os.walk(mypath)
#for y in x:
#    print y
