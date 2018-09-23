import time
import random
from random import randint
from sys import getsizeof
import numpy as np

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    if random.choice('+-') == '-':
        return randint(range_start, range_end) * -1
    else:
        return randint(range_start, range_end)   
		
def productofN(n):
   first = random_with_N_digits(n)
   second = random_with_N_digits(n)
   product = 0
   start = time.time()   
   product = first*second
   end = time.time()
   return getsizeof(first)+getsizeof(second)+getsizeof(product),end-start

def Multiply(size):
    timeArray=[]		
    for i in range(1000):
        timeArray.append(productofN(size));
	
    a = np.array(timeArray,dtype=float)
    print("------------------------------------------------")
    print("max time is %10.8f seconds"%a.max(axis=0)[1])
    print("min time is %10.8f seconds"%a.min(axis=0)[1])
    print("mean time is %10.8f seconds"%a.mean(axis=0)[1])
    print("------------------------------------------------")
    print("avg size is %d bytes"%a.mean(axis=0)[0])


Multiply(int(input("Enter the digit size: ")))