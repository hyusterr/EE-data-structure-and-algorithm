
# coding: utf-8

# In[2]:


import sys

def solution(n):
    num = int(n)

    remain = num
    cblist = []

    if num < 10:
        ans = "1" + str(n)

    else:
    
        while remain > 9:
         
            for i in range(9, 0, -1):
                if remain % i == 0:
                    cblist.append(str(i))
                    remain = remain // i
                    break

        cblist.append(str(remain))
        ans = "".join(sorted(cblist))

    return ans

inFile = open(sys.argv[1], 'r')
# inFile = open('inputp1.txt', 'r')
input_list = list(inFile.read().splitlines())
inFile.close()
    # print(input_list)

    # 3. Solve
answer_list = [ solution(s) for s in input_list ]
# print(answer_list)

    # 4. Output answers
outFile = open(sys.argv[2], 'w')
# outFile = open('outputp1.txt', 'w')
for ans in answer_list:
    outFile.write('{}\n'.format(ans))
outFile.close()

