# CS2223 Project 2 Nikolas Gamarra B17

#import libraries
import time
from memory_profiler import memory_usage
from memory_profiler import profile
import sys
import math
import copy
#print intro for program




def dist(a,b):
    return math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)

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
    return r[0]

def closestPairRec(P,Q):

    if len(P)<=3:

        result=closestPairBF(P)
    else:
        x=0
        PL=[]
        QL=[]
        PR=[]
        QR=[]
        while x <len(P)/2:
            PL.append(P[x])
            QL.append(Q[x])
            x=x+1

        while x<len(P):
            PR.append(P[x])
            QR.append(Q[x])
            x=x+1

        DL=closestPairRec(PL,QL)
        DR=closestPairRec(PR,QR)
        d=min(DL,DR)
        n=int(len(P))

        m=P[(n/2)-1][0]
        S=[]
        num=len(Q)
        #copy all the points of Q for which |x-m|<d into array S[0...num-1
        for element in Q:
            if math.fabs(element[0]-m)<d:
                S.append(element)
        dminsq=d**2
        i=0
        k=0
        while i < num-2:
            k = i + 1
            while (k<= num-1 )and(((S[k][1]-S[i][1])**2) < dminsq):
                k=k+1
                print(((S[k][0]-S[i][0])**2))
                print((S[k][1]-S[i][1])**2)
                var=(((S[k][0]-S[i][0])**2)+((S[k][1]-S[i][1])**2))
                dminsq=min(var,dminsq)
                #k=k+1
            #i = i + 1
        result=math.sqrt(dminsq)

    return result

def effREC(points):#function to test the recursive function
    print('\nTesting Recursive\n')
    P=copy.copy(points)
    Q=copy.copy(points)
    P.sort(key=lambda tup: tup[0])
    Q.sort(key=lambda tup: tup[1])
    t0=time.time()
    result=closestPairRec(P,Q)
    t1=time.time()
    T=t1-t0
    print('The distance of the closest pair: '+str(result)+' Was calculated in time: '+str(T)+' seconds.\nMemory used displayed above.\n')
    return

def effBF(points):#function to test the brute force function
    print('\nTesting Brute Force\n')
    t0=time.time()
    result=closestPairBF(points)
    t1=time.time()
    T=t1-t0
    print('The distance of theclosest pair: '+str(result)+' Was calculated in time: '+str(T)+' seconds.\nMemory used displayed above.\n')
    return


if __name__ == '__main__':
    print('\nCS2223 Project2 Nikolas Gamarra')
    print('This program finds two closest points in a set of n points\n')

    if len(sys.argv)>1:
        filename=str(sys.argv[1])
    else:
        filename="input.txt"
    try:  # check of invalid inputs
        f = open(filename, "r")
        array = f.read()
        # print 't1'
        # print f.read()
        for char in "][":
            array = array.replace(char, '')

        array.split("),(")
        for char in ")(":
            array = array.replace(char, '')

            # print 't2'
        array.split(",")
        # print array
        # print len(array)
        array = array.split(',')
        # print 't3'
        # print array
        # print len(array)
        if len(array) % 2 != 0:
            raise ValueError
        i = 0
        newArray = []
        while i < len(array):
            x = int(array[i])
            y = int(array[i + 1])
            point = (x, y)
            newArray.append(point)
            i = i + 2


            #  if not isinstance(n,int):
            #     raise ValueError
        #break
    except IOError:
        print'Could no read file:', filename  # Primpt user to correct their input
        sys.exit()
    except ValueError:
        print "Value Error: make sure input is valid"
        sys.exit()
    else:
        #break
        print '\nThe input is:\n'
        print newArray
        effBF(newArray)
        effREC(newArray)