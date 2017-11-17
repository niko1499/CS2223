# CS2223 Project 2 Nikolas Gamarra B17

#import libraries
import time
from memory_profiler import memory_usage
from memory_profiler import profile
import sys

#print intro for program
print('\nCS2223 Project2 Nikolas Gamarra')
print('This program finds two closest points in a set of n points\n')

#gather user inputs
while True:
    if len(sys.argv)>1:
        filename=str(sys.argv[1])
    else:
        filename="input.txt"

    try:#check of invalid inputs
        f=open("input.txt","r")
        array=f.read()
        print f.read()
      #  if not isinstance(n,int):
       #     raise ValueError
        break
    except IOError:
        print'Could no read file:', filename #Primpt user to correct their input
        sys.exit()
    except ValueError:
        print "shit is fucked"
        sys.exit()
    else:
        break

@profile
def closestPairBF(array):
    return result

@profile
def closestPairRec(array):
    return result

def effREC(points):#function to test the recursive function
    print('\nTesting Recursive\n')
    t0=time.time()
    result=closestPairRec(points)
    t1=time.time()
    T=t1-t0
    print('The closest pair: '+str(result)+' Was calculated in time: '+str(T)+' seconds. Memory used displayed above\n')
    return

def effBF(points):#function to test the brute force function
    print('\nTesting Brute Force\n')
    t0=time.time()
    result=closestPairBF(points)
    t1=time.time()
    T=t1-t0
    print('The closest pair: '+str(result)+' Was calculated in time: '+str(T)+' seconds. Memory used displayed above\n')
    return

effREC(array)
effBF(array)
