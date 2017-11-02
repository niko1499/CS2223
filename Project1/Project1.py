# CS2223 Project 1 Nikolas Gamarra B17

#import libraries
import time
from memory_profiler import memory_usage
from memory_profiler import profile
from termcolor import colored

#print intro for program
print('\nCS2223 Project1 Nikolas Gamarra')
print('This program finds the greatest common devisor(GCD) of two posivive intiger numbers\n')

#gather user inputs
while True:
    try:#check of invalid inputs
        m=(input('Enter the  first number(m): '))
        n=(input('Enter the second number(n): '))
        if n<=0:#make sure input is positive
            raise ValueError
        if m<=0:
            raise ValueError
        if not isinstance(m,int):#make sure input is integer
            raise ValueError
        if not isinstance(n,int):
            raise ValueError
        break
    except ValueError:
        print('\nINPUT ERROR: Enter two positiver intigers\n')#Primpt user to correct their input
        continue
    else:
        break


def findPrimeFactors(n):#helper function to return all the prime factors of a number
    primeFactors=[]
    i=2
    while i*i<=n:
        while n%i==0:
            primeFactors.append(i)
            n//=i
        i+=1
    if n>1:
        primeFactors.append(n)
    return primeFactors

@profile
def alg1(m,n):#Euclids - function to determin GCD using Euclids method
    while n != 0:
        r=m%n
        m=n
        n=r
    return m

@profile
def alg2(m,n):#Consecutive int - function to determin GCD using consucitive integer method
    t=min(m,n)#step1
    done=0
    state=2
    while done==0:
        if state==2:#step2
            if m%t==0:
                state=3#go to step3
            else:
                state=4#go to step4
        if state==3:#step3
            if n%t==0:
                state=5#go to step5
            else:
                state=4#go to step4
        if state==4:#step4
            t=t-1
            state=2#go to step2
        if state==5:
            done=1
            result=t

    return result

@profile
def alg3(m,n):#Middle School - function to determine GCD using middle school method
    result=1
    primeFactorsOfM=findPrimeFactors(m)
    primeFactorsOfN=findPrimeFactors(n)
    primeFactorsOfBoth=[]
    for i in primeFactorsOfM:
        if i in (primeFactorsOfM and primeFactorsOfN):
            primeFactorsOfBoth.append(i)
    for f in primeFactorsOfBoth:
        result=f*result
    return result

def effGDC(s1,s2):#function to test all three algs for time and space efficiency and print the results
    print colored('\nTesting Algorythem1-Euclids Algorithm','red')#test the first alg
    t0=time.time()
    GCD=alg1(s1,s2)
    t1=time.time()
    T=t1-t0
    print colored('The GCD: '+str(GCD)+' Was calculated in time: '+str(T)+' seconds memory used displayed above','red')

    print colored('\nTesting Algorythem2-Consecutive Integer Checking Algorithm','green')#test the second alg
    t0=time.time()
    alg2(s1,s2)
    t1=time.time()
    T=t1-t0
    print colored('The GCD: '+str(GCD)+' Was calculated in time: '+str(T)+' seconds; memory used displayed above','green')

    print colored('\nTesting Algorythem3-Middle School Procedure','blue')#test the third alg
    t0=time.time()
    alg3(s1,s2)
    t1=time.time()
    T=t1-t0
    print colored('The GCD: '+str(GCD)+' Was calculated in time: '+str(T)+' seconds; memory used displayed above','blue')

    return

effGDC(m,n)#call the function to do all the things

