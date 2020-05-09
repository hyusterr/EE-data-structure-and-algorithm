
# coding: utf-8

# In[2]:


def val(string):
    codelist = []
    
    for letter in string:
        codelist.append(ord(letter))
        
    return codelist

def merge2(A, B):
    C = []
    while len(A) != 0 and len(B) != 0:
        if val(A[0]) <= val(B[0]):
            C.append(A[0])
            A.pop(0)
        else:
            C.append(B[0])
            B.pop(0)
            
    if len(A) == 0:
        C += B
    
    else:
        C += A
    
    return C

def merge3(L, M, R):
    
    A = []
    
    while len(L) != 0 and len(M) != 0 and len(R) != 0:
        if val(L[0]) <= val(R[0]) and val(L[0]) <= val(M[0]):
            A.append(L[0])
            L.pop(0)
            
        elif val(R[0]) <= val(L[0]) and val(R[0]) <= val(M[0]):
            A.append(R[0])
            R.pop(0)
            
        elif val(M[0]) <= val(R[0]) and val(M[0]) <= val(L[0]):
            A.append(M[0])
            M.pop(0)
            
    if len(L) == 0:
        if len(M) == 0:
            if len(R) == 0:
                return A
            else:
                return A + R
        else:
            if len(R) == 0:
                return A + M
            else:
                return A + merge2(M, R)
    else:
        if len(M) == 0:
            if len(R) == 0:
                return A + L
            else:
                return A + merge2(L, R)
        else:
            if len(R) == 0:
                return A + merge2(L, M)
            else:
                return A

def mergesort(Arr):
    if len(Arr) <= 1:
        return Arr
    else:
        length = len(Arr)
        a1 = length // 3 + 1 
        a2 = (length * 2) // 3 + 1
        
        left = mergesort(Arr[:a1])
        mid = mergesort(Arr[a1:a2])
        right = mergesort(Arr[a2:])
        
        return merge3(left, mid, right)

inputpath, outputpath = input().split()

from tools import Parser

myParser = Parser(inputpath)        
    
ans = mergesort(list(myParser.queryList()))

outputfile = open(outputpath, mode='w')
wr = "\n".join(ans)
outputfile.write(wr)  
        
    
    
        
    

