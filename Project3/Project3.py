# CS2223 Project 3 Nikolas Gamarra B17

#import libraries
import time
import sys
import math
import itertools
from itertools import combinations
from itertools import permutations

def ES(carryCapacity,weights,values):#Exhaustive Search Implementation
    n=len(weights)
    itemResult=[]
    x=0
    array=[]
    lastAttempt=[]
    while x < n:
        w=(weights[x])
        v=(values[x])
        tup=(w,v)
        array.append(tup)
        x=x+1
    perm=list(permutations(array))
    highestValue=0

    highestWeight=0
    x=0
    #for attempt in list(perm):#for the possible configurations in all permutations
    while x< len(perm):
        attempt=perm[x]
        x=x+1
       # print(attempt)
        itemIndex=0
        runningWeight=0
        runningValue=0
        while itemIndex<n:#for the items in this attempt
            if(((attempt[itemIndex][0])+runningWeight)<=(carryCapacity)):
                runningWeight=runningWeight+(attempt[itemIndex][0])#add the weight
                runningValue=runningValue+(attempt[itemIndex][1])#add the value
                if(runningValue>=highestValue):
                    itemResult=attempt
                    highestValue=runningValue
                    highestWeight=runningWeight
                    itemResult=attempt[0:itemIndex+1]
            itemIndex=itemIndex+1
    result=(itemResult,highestValue,highestWeight)
    return result

def DP(carryCapacity,weights,values):#dynamic programming implementation
    n=len(weights)
    K = [[0 for x in range((carryCapacity) + 1)] for x in range(n + 1)]
    # Build table K[][] in bottom up manner
    items=[]
    for i in range(n + 1):
        for w in range(carryCapacity + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif (weights[i - 1]) <= w:
                K[i][w] = max((values[i - 1]) + K[i - 1][w - ( weights[i - 1])], K[i - 1][w])

            else:
                K[i][w] = K[i - 1][w]

    return values,K[n][carryCapacity],values

def MY(carryCapacity,weights,values,n):#Alternative Function
    # Returns the maximum value that can be put in a knapsack of
    # capacity W
#def knapSack(W, wt, val, n):
    # Base Case

    if n == 0 or carryCapacity == 0:
        return 0

    # If weight of the nth item is more than Knapsack of capacity
    # W, then this item cannot be included in the optimal solution
    if ((weights[n - 1]) > carryCapacity):
        return MY(carryCapacity, weights, values, n - 1)

    # return the maximum of two cases:
    # (1) nth item included
    # (2) not included
    else:
        return max(values[n - 1] + MY(carryCapacity - weights[n - 1], weights, values, n - 1),MY(carryCapacity, weights, values, n - 1))
    return result

def testAll(carryCapacity,weights,values):#function to test all 3 functions
    #Test First Alg
    print('\n------------------------------------------------------------------------')
    print('\nTesting Exhaustive Search\n')
    t0=time.time()#start time
    resultES=ES(carryCapacity,weights,values)
    t1=time.time()#end time
    T=t1-t0#find difference
    print('Selected Items: '+str(resultES[0]))
    print('Max Value: '+str(resultES[1]))
    print('Max Weight: '+str(resultES[2]))
    print('The answer was calculated in time: '+str(T)+' seconds.\n')
    print(str(T))#print again for easy copy paste

    #Test Second Alg
    print('\n------------------------------------------------------------------------')
    print('\nTesting Dynamic Programming\n')
    t0=time.time()
    resultDP=DP(carryCapacity,weights,values)
    t1=time.time()
    T=t1-t0
    #print('Selected Items:' + str(resultDP[0]))
    print('Max Value: ' + str(resultDP[1]))
    #print('Max Weight: ' + str(resultDP[2]))
    print('The answer was calculated in time: ' + str(T) + ' seconds.\n')
    print(str(T))

    #Test Thrid Alg
    print('\n------------------------------------------------------------------------')
    print('\nTesting My Function\n')
    t0=time.time()
    resultMY=MY(carryCapacity,weights,values,int(len(values)))
    t1=time.time()
    T=t1-t0
    #print('Selected Items: ' + str(result[0]))
    print('Max Value: ' + str(resultMY))
    #print('Max Weight: ' + str(resultMY))
    print('The answer was calculated in time: ' + str(T) + ' seconds.\n')
    print(str(T))
    print('\n------------------------------------------------------------------------')
    return


if __name__ == '__main__':#main function starts program, interprets user input, reads and formats input
    print('\nCS2223 Project3 Nikolas Gamarra')
    print('This program finds the optimal solution to the knapsack problem and tests 3 ways of doing it\n')
    if len(sys.argv)>2:
        raise ValueError
    if len(sys.argv)>1:
        filename=str(sys.argv[1])#select a specific input
    else:
        filename="input-1.txt"#default file
    try:  # check of invalid inputs
        f = open(filename, "r")
        array = f.read()
        weights=[]
        values=[]
        tempArray=[]
        carryCapacitiy=0

        tempArray=array.splitlines(0)
        carryCapacity=tempArray[0]
        weights=tempArray[1]
        values=tempArray[2]

        weights = weights.split(',')# split by specified character
        values = values.split(',')

        Ivalues = [int(v) for v in values]#correct strings to int
        Iweights = [int(w) for w in weights]

        if len(weights) != len(values):
            raise ValueError

    except IOError:
        print ("Could not read file:"+str(filename))# Primpt user to correct their command line input
        sys.exit()
    except ValueError:
        print ("Value Error: make sure input format is valid")# Prompt user to check their input file structure
        sys.exit()
    else:#no errors
        carryCapacity = int(carryCapacity)#correct strings to int
        print ('\nThe input from ' +filename+' is: ')
        print ('   Carry Capacity: ' +str(carryCapacity))
        print ('   Weights: ' +str(weights))
        print ('   Values:  ' +str(values))
        print ('   Number of items: '+str(len(weights)))
        testAll(carryCapacity,Iweights,Ivalues)# make the call to the main tester function
