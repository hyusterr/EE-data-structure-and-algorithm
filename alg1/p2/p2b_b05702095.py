
# coding: utf-8

# In[2]:


inputpath, outputpath = input().split()

inp = open(inputpath, mode='r')
file = inp.read()

def findavalley(s):
    
    s = [float("inf")] + s + [float("inf")]
    m = int(len(s) / 2)
    if s[m] <= s[m + 1] and s[m] <= s[m - 1]:
        return m - 1
    else:
        if s[m - 1] <= s[m]:
            return findavalley(s[:m])
        elif s[m + 1] <= s[m]:
            return findavalley(s[m+1:])

string = [float(i) for i in file.split()]
ans = findavalley(string)

outputfile = open(outputpath, mode='w')
outputfile.write(str(ans))

