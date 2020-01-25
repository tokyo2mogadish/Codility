# CodeSkulptor runs Python programs in your browser.
# Click the upper left button to run this simple demo.

# CodeSkulptor runs in Chrome 18+, Firefox 11+, and Safari 6+.
# Some features may work in other browsers, but do not expect
# full functionality.  It does NOT run in Internet Explorer.

import simplegui

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
    