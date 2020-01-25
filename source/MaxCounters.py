# CodeSkulptor runs Python programs in your browser.
# Click the upper left button to run this simple demo.

# CodeSkulptor is tested to run in recent versions of
# Chrome, Firefox, and Safari.

import simplegui

def solution(N, A):
    test_array =[0]*len(range(1, max(A)))
    for i in A:
        if(i<=N):
            test_array[i-1] +=1
        else:
            test_array = [max(test_array)]*len(range(1, max(A)))
    
    return test_array