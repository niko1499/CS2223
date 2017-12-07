# CS2223 Project 3 Nikolas Gamarra B17

#import libraries
import time
import sys
import math
import itertools
from itertools import combinations
from itertools import permutations

def ES(carryCapacity,array,n):#Exhaustive Search Implementation
    itemResult = []
    perm=list(permutations(array))#make all the permutations and put them in a list
    highestValue=0
    highestWeight=0
    x=0
    while x< len(perm):    #for the possible configurations in all permutations
        attempt=perm[x]
        x=x+1
        itemIndex=0
        runningWeight=0
        runningValue=0
        while itemIndex<n:#for the items in this attempt
            if(((attempt[itemIndex][0])+runningWeight)<=(carryCapacity)):
                runningWeight=runningWeight+(attempt[itemIndex][0])#add the weight
                runningValue=runningValue+(attempt[itemIndex][1])#add the value
                if(runningValue>=highestValue):#if we find a better value
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
    return K[n][carryCapacity]

def MY(carryCapacity,weights,values,n):#Alternative Function
    #check for no input
    if n == 0 or carryCapacity == 0:
        return 0

    #check if weight past capacity if so can not be included in optimal
    if ((weights[n - 1]) > carryCapacity):
        return MY(carryCapacity, weights, values, n - 1)

    # return max of item included and item not included
    else:
        return max(values[n - 1] + MY(carryCapacity - weights[n - 1], weights, values, n - 1),MY(carryCapacity, weights, values, n - 1))

def testAll(carryCapacity,weights,values):#function to test all 3 functions
    #Test First Alg
    print('\n------------------------------------------------------------------------')
    print('\nTesting Exhaustive Search\n')
    n = len(weights)
    x = 0
    array = []
    while x < n:#Pre-arrange data into tuples
        w = (weights[x])
        v = (values[x])
        tup = (w, v)
        array.append(tup)
        x = x + 1
    t0=time.time()#start time
    resultES=ES(carryCapacity,array,n)
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
    print('Max Value: ' + str(resultDP))
    print('The answer was calculated in time: ' + str(T) + ' seconds.\n')
    print(str(T))

    #Test Thrid Alg
    print('\n------------------------------------------------------------------------')
    print('\nTesting My Function\n')
    t0=time.time()
    resultMY=MY(carryCapacity,weights,values,int(len(values)))
    t1=time.time()
    T=t1-t0
    print('Max Value: ' + str(resultMY))
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
