############################################
#   107-1 Data Structure and Programming
#   Programming Assignment #2
#   Instructor: Pei-Yuan Wu
############################################

import sys

# **********************************
# *  TODO                          *
# **********************************
def solution(string):
    '''
    Modify this function
    1. Return the number (integer) of all possible ways 
       to divide input_string into n1, n2, ... , nk (0 <= ni <= 100).
    2. For example, given input_string '21005', you should return 4.
       '21005'  =>  '2,1,0,0,5'  => return 4
                    '21,0,0,5'
                    '2,10,0,5'
                    '2,100,5' 
    3. Feel free to add more functions.
    '''
    lst = []

    for i in range(len(string)):
        if i == 0:
            lst.append(1)
        else:
            lst.append(0)
        
            if string[i - 1] != '0':
                if i == 1:
                    lst[i] = 2
                else:
                    lst[i] = lst[i - 1] + lst[i - 2]
            elif string[i - 1] == '0':
                if i == 1:
                    if string[i - 1] == '0':
                        lst[i] = 1
                else:
                    if string[i - 2] == '1' and string[i] == '0':
                        lst[i] = lst[i - 1] + lst[i - 3]
                    else:
                        lst[i] = lst[i - 1] 

    return lst[-1]

# **********************************
# *  Do NOT modify the code below  *
# **********************************
if __name__ == '__main__':
    # 1. Check the command-line arguments
    if len(sys.argv) != 3:
        sys.exit("Usage: python3 programming_hw2.py <input> <output>")
    
    # 2. Read the input file
    inFile = open(sys.argv[1], 'r')
    input_list = list(inFile.read().splitlines())
    inFile.close()
    # print(input_list)

    # 3. Solve
    answer_list = [ solution(s) for s in input_list ]
    # print(answer_list)

    # 4. Output answers
    outFile = open(sys.argv[2], 'w')
    for ans in answer_list:
        outFile.write('{}\n'.format(ans))
    outFile.close()
