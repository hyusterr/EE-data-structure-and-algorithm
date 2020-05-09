
# coding: utf-8

# In[7]:


inputpath, outputpath = input().split()

inp = open(inputpath, mode='r')
file = inp.read()
# print(file)

s = [float(i) for i in file.split("\n")]
# print(s)

s.append(float('inf'))
s = [float('inf')] + s
# print(s)

idxlist = []
for idx in range(1, len(s) - 1):
    if s[idx - 1] > s[idx] and s[idx + 1] > s[idx]:
        idxlist.append(idx)

# print(idxlist)
# print(idxlist[0] - 1)
ans = idxlist[0] - 1

outputfile = open(outputpath, mode='w')
outputfile.write(str(ans))

