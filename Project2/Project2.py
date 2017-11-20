# CS2223 Project 2 Nikolas Gamarra B17

#import libraries
import time
from memory_profiler import memory_usage
from memory_profiler import profile
import sys
import math

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
        f=open(filename,"r")
        array=f.read()
       # print 't1'
       # print f.read()
        for char in "][":
            array=array.replace(char,'')

        array.split("),(")
        for char in ")(":
            array=array.replace(char,'')

       # print 't2'
        array.split(",")
       # print array
       # print len(array)
        array=array.split(',')
       # print 't3'
       # print array
       # print len(array)
        if len(array)%2 !=0:
            raise ValueError
        i=0
        newArray=[]
        while i<len(array):
            x=int(array[i])
            y=int(array[i+1])
            point=(x,y)
            newArray.append(point)
            i=i+2


      #  if not isinstance(n,int):
       #     raise ValueError
        break
    except IOError:
        print'Could no read file:', filename #Primpt user to correct their input
        sys.exit()
    except ValueError:
        print "Value Error: make sure input is valid"
        sys.exit()
    else:
        break
print '\nThe input is:\n'
print newArray

def dist(a,b):
    return math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)

@profile
def closestPairBF(array):
    i=0
    result=[99999999,0,0]
    while i <len(array):
        j=i+1
        while j <len(array):
            d = dist(array[i],array[j])
            if d<result[0]:
                result=[d,i,j]
            j=j+1
        i=i+1
    r= [result[0],array[result[1]],array[result[2]]]
    return r

def oneToTwo(array):
    P=[]
    Q=[]
    for element in array:
        P.append(element[0])
        Q.append(element[1])
    result=[P,Q]
    return result

def twoToOne(P,Q):
    i=0
    result=[]
    while i < len(P):
        result.append((P[i],Q[i]))
    return result

@profile
def closestPairRec(P,Q):
    if len(P)<=3:
        array=twoToOne(P,Q)
        result=closestPairBF(array)
    else:
        i=0
        while i <len(P)/2:
            PL=P[i]
            QL=Q[i]
            i=i+1

        while i<len(P):
            PR=P[i]
            QR=Q[i]

        print 'helo'
        print PL
        print PR
        result=0


    return result

def effREC(points):#function to test the recursive function
    print('\nTesting Recursive\n')
    r=oneToTwo(points)
    t0=time.time()
    result=closestPairRec(r[0],r[1])
    t1=time.time()
    T=t1-t0
    print('The closest pair[dist,(x,y),(x,y)]: '+str(result)+' Was calculated in time: '+str(T)+' seconds.\nMemory used displayed above.\n')
    return

def effBF(points):#function to test the brute force function
    print('\nTesting Brute Force\n')
    t0=time.time()
    result=closestPairBF(points)
    t1=time.time()
    T=t1-t0
    print('The closest pair[dist,(x,y),(x,y)]: '+str(result)+' Was calculated in time: '+str(T)+' seconds.\nMemory used displayed above.\n')
    return
effREC(newArray)
effBF(newArray)
