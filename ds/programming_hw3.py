
# coding: utf-8

# In[ ]:


############################################
#   107-1 Data Structure and Programming
#   Programming Assignment #3
#   Instructor: Pei-Yuan Wu
############################################

# Do not import any other library
import sys

# **********************************
# *  TODO                          *
# **********************************

'''
# You may need this node class for implementation of tree.
class Node:
    def __init__(self, data,left=None,right=None):
        self.left = left
        self.right = right
        self.data = data
'''

# This function is for checking if a sequence can be a preorder of BST or not.
# if yes, return the postorder traversal of the BST.
# if not, return '-'.
class node:
    def __init__(self, data,left=None,right=None):
        self.left = left
        self.right = right
        self.data = data






def preorder_check(st):
    lst = [int(i) for i in st.split(',')]
    ans1 = []
    
    def insert(root, num):
        if num < root.data:
            if root.left == None:
                root.left = node(num)                
            else:
                insert(root.left, num)
        elif num > root.data:
            if root.right == None:
                root.right = node(num)
            else:
                insert(root.right, num)
                
    def pre_order_lstgner(root):
        if not root:
            return        
        ans1.append (root.data)
        pre_order_lstgner(root.left)
        pre_order_lstgner(root.right)
        
    r = node(lst[0])
    for j in range(1, len(lst)):
        insert(r, lst[j])
        
    pre_order_lstgner(r)
    
    wr = []

    def postOrder(root):
        if root:
            postOrder(root.left)
            postOrder(root.right)
            wr.append (root.data)
#     print(ans)
#     print(lst)
    
    if ans1 != lst:
        return '-'
    
    else:
        postOrder(r)
        return ",".join([str(k) for k in wr])



# This function is for checking if a sequence can be a postorder of BST or not.
# if yes, return the preorder traversal of the BST.
# if not, return '-'.
                
def postorder_check(st):
    lst = [int(i) for i in st.split(',')]
    ans1 = []
 
    
    def insert(root, num):
        if num < root.data:
            if root.left == None:
                root.left = node(num)                
            else:
                insert(root.left, num)
        elif num > root.data:
            if root.right == None:
                root.right = node(num)
            else:
                insert(root.right, num)
                
    def post_order_lstgner(root):
        if not root:
            return        
        post_order_lstgner(root.left)
        post_order_lstgner(root.right)
        ans1.append (root.data)

    r = node(lst[-1])
    for j in range(len(lst)-2, -1, -1):
        insert(r, lst[j])
        
    post_order_lstgner(r)
    
    wr = []

    def preOrder(root):
        if root:
            wr.append (root.data)
            preOrder(root.left)
            preOrder(root.right)
        
    
#     print(ans)
#     print(lst)
    
    if ans1 != lst:
        return '-'
    
    else:
        preOrder(r)
        return ",".join([str(k) for k in wr])

'''
Feel free to add more functions here
'''

# **********************************
# *  Do NOT modify the code below  *
# **********************************
if __name__ == '__main__':
    # 1. Check the command line arguments
    if len(sys.argv) != 4:
        sys.exit("Usage: python3 programming_hw3.py <-pre | -post> <input> <output>")
    
    # 2. Read the input file
    inFile = open(sys.argv[2], 'r')
    input_list = list(inFile.read().splitlines())
    inFile.close()
    # print(input_list)

    # 3. Solve
    if sys.argv[1] == '-pre':
        answer_list = [ preorder_check(s) for s in input_list ]
    elif sys.argv[1] == '-post':
        answer_list = [ postorder_check(s) for s in input_list ] 
    # print(answer_list)

    # 4. Output answers
    outFile = open(sys.argv[3], 'w')
    for ans in answer_list:
        outFile.write('{}\n'.format(ans))
    outFile.close()

