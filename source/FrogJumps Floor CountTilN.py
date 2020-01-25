# CodeSkulptor runs Python programs in your browser.
# Click the upper left button to run this simple demo.

# CodeSkulptor runs in Chrome 18+, Firefox 11+, and Safari 6+.
# Some features may work in other browsers, but do not expect
# full functionality.  It does NOT run in Internet Explorer.

import simplegui
print '----FLOOR----'
def logaritmic(n):
    count = 0
    while n>1:
        n//=2
        count +=1
    return count
print '->Flor of a number 20 goes ', (logaritmic(20)), 'times<-\n'

print '----COUNT THE SUM OF NUMBERS TILL N----'
def countTilN(n):
    count = 0
    for i in range(1, n+1):
        #print i
        count += i
    return count
print '->sum of numbers till n is:', countTilN(20), '<-\n'

print '----FASTER COUNT THE SUM OF NUMBERS TILL N----'
def countTilNFaster(n):
    sum = n * (n + 1)//2    
    return sum
print '->FASTER sum of numbers till n is:', countTilNFaster(20), '<-\n'

print '****FROG****'
def frogJumps(x, y, d):
    
    return ((y-x)//d +1 if ((y-x)//d)*d<(y-x)  else (y-x)//d)

print '->From a X taking a D jumps to Y the frog will need ', frogJumps(75, 85, 30), ' jumps.<-'
#CSharp CODE
#public static double FrogJump(double X, double Y, double D)
        #{
        #    return ((Math.Floor((Y - X) / D)) * D < (Y - X) ? Math.Floor((Y - X) / D) + 1 : Math.Floor((Y - X) / D));
        #}


        