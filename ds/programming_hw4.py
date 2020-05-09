
# coding: utf-8

# In[1]:


import sys

def Parent(i):
    return int(i/2)
def Left(i):
    return(2*i)
def Right(i):
    return 2*i+1

def MinHeapify(A, i): #輸入是list 跟 index
    #確認
    smallest = 0
    l = Left(i)
    r = Right(i)
    
    if l < len(A) and A[l] < A[i]:
        smallest = l
    else:
        smallest = i
    if r < len(A) and A[r] < A[smallest]:
        smallest = r
        
    if smallest != i:
        temp = A[i]
        A[i] = A[smallest]
        A[smallest] = temp
        MinHeapify(A, smallest)
        
class MinBinaryHeap():
    def __init__(self):
        self.heap = [0] # with a dummy node
        
#     def decreasekey(self, i, key):
#         A[i] = key
#         while i > 1 and self.heap[Parent(i)] > self.heap[i]:
#             temp = self.heap[i]
#             self.heap[i] = A[Parent(i)]
#             A[Parent(i)] = temp
#             i = Parent(i)
            
    def insert(self, item):
        # TODO #
        i = len(self.heap)
        self.heap.append(item)
        while i > 1 and self.heap[Parent(i)] > self.heap[i]:
            temp = self.heap[i]
            self.heap[i] = self.heap[Parent(i)]
            self.heap[Parent(i)] = temp
            i = Parent(i)
        
    def deleteMin(self):
        # TODO #
        self.heap[1] = self.heap[len(self.heap) - 1]
        self.heap.pop()
        MinHeapify(self.heap, 1)

    def findMin(self):
        # TODO #
        return self.heap[1]

    def size(self):
        # TODO #
        return len(self.heap) - 1
    
    def string(self):
        # Convert self.heap into a string
        return list2String(self.heap[1:])
    
def list2String(l):
    formatted_list = ['{}' for item in l ] 
    s = ','.join(formatted_list)
    return s.format(*l)

if __name__ == '__main__':
    # 1. Check the command-line arguments
    if len(sys.argv) != 3:
        sys.exit("Usage: python3 programming_hw4.py <input> <output>")
    
    # 2. Read the input file
    inFile = open(sys.argv[1], 'r')
    input_line_list = list(inFile.read().splitlines())
    input_cmd_list = [ line.split(' ') for line in input_line_list ]
    inFile.close()

    # 3. Solve
    minPQ = MinBinaryHeap()
    findMin_list = []
    for cmd in input_cmd_list:
        if cmd[0] == 'insert':
            # print('insert {}'.format(cmd[1]))
            minPQ.insert(int(cmd[1]))
        elif cmd[0] == 'deleteMin':
            # print('deleteMin')
            if minPQ.size() > 0:
                minPQ.deleteMin()
        elif cmd[0] == 'findMin':
            # print('findMin')
            if minPQ.size() > 0:
                findMin_list.append(minPQ.findMin())
            else:
                findMin_list.append('-')
        else: # Unknown command
            assert False
        # print(minPQ.string())
    
    # 4. Output answers
    outFile = open(sys.argv[2], 'w')
    # 4.1 Output FindMin string
    outFile.write('{}\n'.format(list2String(findMin_list)))
    # 4.2 Output minPQ string
    outFile.write('{}'.format(minPQ.string()))
    outFile.close()

