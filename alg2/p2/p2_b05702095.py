
# coding: utf-8

# In[7]:


import sys

inFile = open(sys.argv[1], 'r')
# inFile = open('inputp2.txt', 'r')
input_list = list(inFile.read().splitlines())
inFile.close()

hw_list = [int(hws) for hws in input_list[0].split()]
dl_list = [int(dls) for dls in input_list[1].split()]
pn_list = [int(pns) for pns in input_list[2].split()]

info_list = []
for i in range(len(hw_list)):
    info_list.append((hw_list[i], dl_list[i], pn_list[i]))

def penalsort(tupl):
    return tupl[2]

penalty_sortlist = sorted(info_list, key=penalsort, reverse=True)
# print(penalty_sortlist)        

ans = [0] * len(info_list)
wait = []

for info in penalty_sortlist:
    if ans[info[1] - 1] == 0:
        ans[info[1] - 1] = info
    else:
        k = 2
        while ans[info[1] - k] != 0 and info[1] - k >= 0:
            k += 1
        if info[1] - k >= 0:
            ans[info[1] - k] = info
        else:
            wait.append(info)
            
# print(wait)
# print(ans)

penalty = 0
for dehw in wait: 
    penalty += dehw[2]
    
for l in range(len(ans)):
    if ans[l] == 0:
        ans[l] = wait.pop()

# print(ans)
# print(wait)

writeorder = []
for item in ans:
    writeorder.append(item[0])

# print(writeorder)        
# print(penalty)

outFile = open(sys.argv[2], 'w')
# outFile = open('outputp2.txt', 'w')
for wro in writeorder:
    outFile.write('{} '.format(wro))
outFile.write('\n')
outFile.write(str(penalty))
outFile.close()

