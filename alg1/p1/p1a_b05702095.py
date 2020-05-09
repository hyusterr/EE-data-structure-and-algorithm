
# coding: utf-8

# In[8]:


inputpath, outputpath = input().split()

from tools import Parser

myParser = Parser(inputpath)

def value(string):
    codelist = []
    
    for letter in string:
        codelist.append(ord(letter))
        
    return codelist

def insertionsort(lst):
    for i in range(len(lst)):
        door = lst[i]
        j = i - 1
        while j >= 0 and value(door) < value(lst[j]):
            lst[j + 1] = lst[j]
            lst[j] = door
            j = j - 1
        else:
            # setting j + 1 instead of i to let index go with "door" moves 
            lst[j + 1] = door 
    return lst

ans = insertionsort(list(myParser.queryList()))

outputfile = open(outputpath, mode='w')
wr = "\n".join(ans)
outputfile.write(wr)

