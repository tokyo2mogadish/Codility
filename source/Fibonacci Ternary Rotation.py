# CodeSkulptor runs Python programs in your browser.
# Click the upper left button to run this simple demo.

# CodeSkulptor runs in Chrome 18+, Firefox 11+, and Safari 6+.
# Some features may work in other browsers, but do not expect
# full functionality.  It does NOT run in Internet Explorer.

import simplegui
print '-----TERNARY-------------------'

a=2
b=3
print(1 if a<b else 2)

print '-------------------------------'
n=15

for i in range(n, 0, -1):
    for j in range(n-i):
        print '',
    for j in range (2*i -1):
        print '*'*j,
    print
        
        
print '--------------------'
print '*'
print '* *'
print '* * *'
print '* * * *'
print '* * * * *'
print '--------------------'
print 'Fibonacci'

a = 0
b = 1
while a<=n:
    print a
    c = a + b
    a = b
    b = c
print '---------MODULO %-------'
print '6 modulo 5: ',6%5
print '9 modulo 5: ', 9%5
print '---------ROTATION-------'    
test_array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def solution(A, K):
    N =len(A)
    new_array = [0]* N
    for i in range(0, N):
        if(K > N):
            if((i + (K % N)) > (N - 1)):
                new_array[ i + (K%N)-N] = test_array[i]
            else:
                new_array[i + (K%N)]= test_array[i]
        else:
            if((i+K)>(N-1)):
                new_array[(i+K)-N] = test_array[i]
            else:
                new_array[i+K] = test_array[i]
    return new_array
                               

print solution(test_array, 15)
    















