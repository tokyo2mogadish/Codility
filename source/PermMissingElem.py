import simplegui

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
print '->FASTER sum of numbers till n is:', countTilNFaster(4), '<-\n'

print '----PermMissingElem----'
test_array =[ 2, 3, 1, 5, 4, 6, 8]
print 'dati niz: ', test_array
print 'njegova duzina: ', len(test_array)

def PermMissingElem(A):
    for i in range(1,len(A)+1):
        if (i not in A):
            return i
print 'in array: ', test_array, ' number ', PermMissingElem(test_array), ' is missing \n'

#NAJBRZE RESENJE ZA PermMissingElem
A =[ 2, 3, 1, 5]
print ((len(A)+1) * (len(A)+2) //2) - sum(A), '\n'

#CSharp resenje
#public static int PermMissingElem (int[] A) 
#        {
#           return (((A.Length + 1) * (A.Length + 2)) / 2 - A.Sum()); 
#       }
