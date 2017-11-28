# CS2223 Project 3 Nikolas Gamarra B17

#import libraries
import time
import sys
import math
from memory_profiler import memory_usage
from memory_profiler import profile

global carryCapacity = 6
@profile
def ES(weights,values,array):# Exhaustive Search
    global carryCapacity
    i=1
    n=len(weights)
    while i < 2**n:
        j=n
        tempWeight=0
        tempValue=0
        while(array[j]!=0 and j>0):
            array[j]=0
            j=j-1
        array[j]=1
        for k range(1 to n):
            if(array[k]==1:
                    tempWeight=tempWeight+weights[k]
                    temValue=tempValue+values[k]
        if(tempValue>bestValue and tempWeight <= carryCapacity):
            bestValue=tempValue
            bestWeight=tempWeight

        result=array
    return result

@profile
def DP(items):#Dynamic Programming
    global carryCapacity
    return

@profile
def MY(items):#Alternative Function
    global carryCapacity
    return

def testAll(data):#function to test all 3 functions
    print('\nTesting Exhaustive Search\n')
    t0=time.time()
    result=ES(data)
    t1=time.time()
    T=t1-t0
    print('The following items were selected: '+str(result)+' Answer was calculated in time: '+str(T)+' seconds.\n')

    print('\nTesting Dynamic Programming\n')
    t0=time.time()
    result=DP(data)
    t1=time.time()
    T=t1-t0
    print('The following items were selected: '+str(result)+' Answer was calculated in time: '+str(T)+' seconds.\n')

    print('\nTesting My Function\n')
    t0=time.time()
    result=MY(data)
    t1=time.time()
    T=t1-t0
    print('The following items were selected: '+str(result)+' Answer was calculated in time: '+str(T)+' seconds.\n')

    return


if __name__ == '__main__':
    print('\nCS2223 Project3 Nikolas Gamarra')
    print('This program finds the optimal solution to the knapsack problem and tests 3 ways of doing it\n')
    if len(sys.argv)>2:
        raise ValueError
    if len(sys.argv)>1:
        filename=str(sys.argv[1])
    else:
        filename="input.txt"
    try:  # check of invalid inputs
        f = open(filename, "r")
        array = f.read()
        for char in "][":
            array = array.replace(char, '')
        array.split("),(")
        for char in ")(":
            array = array.replace(char, '')
        array.split(",")
        array = array.split(',')
        if len(array) % 2 != 0:#check that there is an even nuber of numbers in the array
            raise ValueError
        i = 0
        newArray = []
        while i < len(array):#run through the array
            x = int(array[i])#extract x as an int
            y = int(array[i + 1])#extract y as an int
            point = (x, y)# put into tupl
            newArray.append(point)#add tupl to array 
            i = i + 2
    except IOError:
        print'Could no read file:', filename  # Primpt user to correct their input
        sys.exit()
    except ValueError:
        print "Value Error: make sure input is valid"
        sys.exit()
    except UserError:
        print "invalid number of inputs"
        sys.exit()
    else:
        #break
        print '\nThe input from ' +filename+' is: \n'
        print newArray
        print '\nLength: '+str(len(newArray))
        testAll(newArray)
'''
class MyException(Exception):
    pass
raise MyException
