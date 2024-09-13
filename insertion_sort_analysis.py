import random

#smaller function
def smaller(A,j,i):

    global COMPCOUNT
    COMPCOUNT+=1
    return bool(A[i] < A[j])
    
#initialize global counter
COMPCOUNT = 0

#function to sort
def insertion(A):
    #insertion sort   
    for i in range(1, len(A)):
        curr = A[i]
        j=i-1
#call smaller for comparison
        while smaller(A,j,j+1)==True and j>=0:
            A[j+1] = A[j]
            j-=1
            A[j+1] = curr


#best case
def best():
    n = 32
    A=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32]
    #print n
    print("n:",n)
#print input list
    print("Input list: ")
    for x in range(len(A)):
        print (A[x], end=', ')
#call insertion
    insertion(A)
#print sorted list
    print(end='\n')        
    print("Sorted List: ")
    for x in range(len(A)):
        print(A[x], end=', ')
#print COMPCOUNT
    print(end='\n')
    print("number of comparisons: ",COMPCOUNT,end='\n\n')

#worst case
def worst():
    n = 32
    A=[32,31,30,29,28,27,26,25,24,23,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]
    #print n
    print("n:",n)
#print input list
    print("Input list: ")
    for x in range(len(A)):
        print (A[x], end=', ')
#call insertion
    insertion(A)
#print sorted list
    print(end='\n')        
    print("Sorted List: ")
    for x in range(len(A)):
        print(A[x], end=', ')
#print COMPCOUNT
    print(end='\n')
    print("number of comparisons: ",COMPCOUNT,end='\n\n')

#average case
def avg():
    n = 32
    index = 0
    A =[]
    for index in range(0,n):
        num = random.randint(0,100)
        A.append(num)
        index+=1
#print n
    print("n:",n)
#print input list
    print("Input list: ")
    for x in range(len(A)):
        print (A[x], end=', ')
#call insertion 
    insertion(A)
#print sorted list
    print(end='\n')        
    print("Sorted List: ")
    for x in range(len(A)):
        print(A[x], end=', ')
#print COMPCOUNT
    print(end='\n')
    print("number of comparisons: ",COMPCOUNT,end='\n\n')
    
#increasing array size 100
def inc_100():
    n =100
    index = 0
    A =[]
    for index in range(0,n):
        num = random.randint(0,100)
        A.append(num)
        index+=1
#print n
    print("n:",n)
    insertion(A)
#print COMPCOUNT
    print("number of comparisons: ",COMPCOUNT,end='\n')

#increasing array size 1000
def inc_1000():
    n = 1000
    index = 0
    A =[]
    for index in range(0,n):
        num = random.randint(0,100)
        A.append(num)
        index+=1
#print n
    print(end='\n')
    print("n:",n)
    insertion(A)
#print COMPCOUNT
    print("number of comparisons: ",COMPCOUNT,end='\n')

#increasing array size 10000
def inc_10000():
    n = 10000
    index = 0
    A =[]
    for index in range(0,n):
        num = random.randint(0,100)
        A.append(num)
        index+=1
#print n
    print(end='\n')
    print("n:",n)
    insertion(A)
#print COMPCOUNT
    print("number of comparisons: ",COMPCOUNT,end='\n')
#test
best()
COMPCOUNT = 0
worst()
COMPCOUNT = 0
avg()
COMPCOUNT = 0
inc_100()
COMPCOUNT = 0
inc_1000()
COMPCOUNT = 0
inc_10000()
