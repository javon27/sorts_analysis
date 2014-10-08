#!/usr/bin/env python
#Jayson Gallardo: jayson.gallardo
#Zack Flowers: zackary.flowers
#Josh Allen: josh.allen

from random import random
from time import time
import sys

sys.setrecursionlimit(1500)  # try to get around quickSort recursion depth problem

count = 0
x = 100
arrayType = 'random'
printArray = False
Array = []

###################################### INSERTION SORT ####################################
def insertionSort(A):
    global count
    if len(A) < 2:
        return A
    for i in range(1, len(A)):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            count += 1  # count comparisons
            A[j+1] = A[j]
            j -= 1
        count += 1  # count failed comparison
        A[j+1] = key
    return A

####################################### MERGE SORT ########################################
def mergeSort(A):
    p = 0
    r = len(A)
    return MergeSort(A, p, r)


def MergeSort(A, p, r):
    if 1 != r - p:
        q = p + (r - p)//2
        A = MergeSort(A, p, q)
        A = MergeSort(A, q, r)
        A = merge(A, p, q, r)
    return A


def merge(array, start, middle, end):
    global count
    leftHalf = array[start:middle]
    rightPointer = middle
    b = 0
    while b < len(leftHalf) and rightPointer < end:  # both halves are not empty
        if leftHalf[b] < array[rightPointer]:
            count += 1
            array[start] = leftHalf[b]
            b += 1
        else:
            count += 1
            array[start] = array[rightPointer]
            rightPointer += 1
        start += 1

    while b < len(leftHalf):
        array[start] = leftHalf[b]
        b += 1
        start += 1
    while rightPointer < end:
        array[start] = array[rightPointer]
        rightPointer += 1
        start += 1
    return array

############################################## QUICK SORT #############################################
def quickSort(array):
    global count
    less = []
    pivotList = []
    more = []
    if len(array) <= 1:
        return array
    else:
        pivot = array[-1]
        for i in array:
            if i < pivot:
                count += 1
                less.append(i)
            elif i > pivot:
                count += 2  # takes into account (if < pivot) == False
                more.append(i)
            else:
                count += 2
                pivotList.append(i)
        less = quickSort(less)
        more = quickSort(more)
        return less + pivotList + more

############################################## HEAP SORT ####################################################
def heapSort(array):
    array = heapify(array)
    for start in range((len(array)-2)//2, -1, -1):
        siftdown(array, start, len(array)-1)

    for end in range(len(array)-1, 0, -1):
        array[end], array[0] = array[0], array[end]
        siftdown(array, 0, end - 1)
    return array

def siftdown(array, start, end):
    global count
    root = start
    while True:
        child = root * 2 + 1
        if child > end:
            count += 1
            break
        count += 1
        if child + 1 <= end and array[child] < array[child + 1]:
            child += 1
        count += 1
        if array[root] < array[child]:
            array[root], array[child] = array[child], array[root]
            root = child
            count += 1
        else:
            count += 1
            break

def heapify(array):
    global count
    size=len(array)
    for root in range((size//2)-1,-1,-1):
        root_val = array[root]
        child = 2*root+1
        while(child<size):
            if child<size-1 and array[child]>array[child+1]:
                child+=1
            if root_val<=array[child]:     # compare against saved root value
                break
            array[(child-1)//2]=array[child]   # find child's parent's index correctly
            child=2*child+1
        array[(child-1)//2]=root_val       # here too, and assign saved root value
    return array

############################################ BUBBLE SORT ###########################################
def bubbleSort(A):
    global count
    top = len(A)
    swap = True
    while swap:
        swap = False
        for i in range(1,top):
            if A[i-1] > A[i]:
                swap = True
                temp = A[i-1]
                A[i-1] = A[i]
                A[i] = temp
            count += 1
        top -= 1
    return A


############################################## HELPER FUNCTIONS ##########################################
def randomList(size):
    A = [int(size*random()) for i in range(size)]
    return A

def increasingList(size):
    A = [i for i in range(size)]
    return A

def decreasingList(size):
    A = increasingList(size)
    A = A[::-1]
    return A

def timeIt(func, array):
    global count
    count = 0
    print('\n')
    print(func.__name__ + '():')
    try:
        start = time()
        array = func(array)
        end = time()
        delta = end-start
        print('runtime: ' + str(delta) + ' seconds\n')
        print('comparisons: ' + str(count) + '\n')
        if printArray:
            print(array)
            print('\n')
    except RuntimeError as e:
        print('Error running ' + func.__name__ + '(): ' + e.args[0])

def checkArgs(argv):
    global printArray
    global x
    try:
        opts, args = getopt.getopt(argv, "hn:p:")
    except getopt.GetoptError:
        print('sorts.py -n <integer> -p <true || false>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('sorts.py -n <integer> -p <true || false>')
            sys.exit()
        elif opt == '-n':
            try:
                x = int(arg)
            except:
                pass
        elif opt == '-p':
            if arg.lower() == 'true':
                printArray = True
            else:
                printArray = False

def updateSize():
    global x
    global Array
    while True:
        try:
            x = int(input('Array size: '))
            break
        except ValueError:
            print('Not an integer!')
    if arrayType == 'random':
        Array = randomList(x)
    elif arrayType == 'increasing':
        Array = increasingList(x)
    else:
        Array = decreasingList(x)


def toggleType():
    global arrayType
    global Array
    while True:
        print('(r)andom')
        print('(i)ncreasing')
        print('(d)ecreasing')
        userInput = input()
        if userInput[0].lower() == 'r':
            Array = randomList(x)
            arrayType = 'random'
            break
        elif userInput[0].lower() == 'i':
            Array = increasingList(x)
            arrayType = 'increasing'
            break
        elif userInput[0].lower() == 'd':
            Array = decreasingList(x)
            arrayType = 'decreasing'
            break
        else:
            print('Invalid selection')

def togglePrint():
    global printArray
    printArray = not printArray


def printMenu():
    print('\n')
    if printArray:
        print('Starting Array: '+str(Array))
        print('\n')
    print('Make your selection:')
    print('1: Insertion Sort')
    print('2: Merge Sort')
    print('3: Quick Sort')
    print('4: Heap Sort')
    print('5: Bubble Sort')
    print('6: Set array size (currently: '+str(x)+')')
    print('7: Toggle array type (currently: '+arrayType+')')
    print('8: Toggle print array (currently: '+str(printArray)+')')
    print('0: Quit')

############################################### MAIN ############################################
def main(argv):
    global Array
    checkArgs(argv)

    Array = randomList(x)


    userInput = None
    while True:
        printMenu()
        try:
            userInput = int(input())
        except ValueError:
            print("\nInvalid selection")
        else:
            if userInput > 8 or userInput < 0:
                print("\nInvalid selection")
            elif userInput == 0:
                print("Have a nice day!")
                return
            elif userInput == 1:
                timeIt(insertionSort, Array[:])
            elif userInput == 2:
                timeIt(mergeSort, Array[:])
            elif userInput == 3:
                timeIt(quickSort, Array[:])
            elif userInput == 4:
                timeIt(heapSort, Array[:])
            elif userInput == 5:
                timeIt(bubbleSort, Array[:])
            elif userInput == 6:
                updateSize()
            elif userInput == 7:
                toggleType()
            else:  # == 8
                togglePrint()


if __name__ == "__main__":
    import getopt
    import sys
    main(sys.argv[1:])
