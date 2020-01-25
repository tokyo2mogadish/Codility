import simplegui

#####FrogRiverOne####

A=[1, 3, 1, 4, 2, 3, 5, 4]
N = len(A)
X = 5



print (list(range(0, X+1)))

bili = [0]*(X+1)


brojac =  0
if X not in A:
    print -1
for i in A:
    if (bili != list(range(0, X+1))):
        brojac+=1
        if (i in list(range(0, X+1))):
            bili[i]=i
                   
if bili != list(range (0, X+1)):
    print (-1)
else:
    print (brojac-1)


