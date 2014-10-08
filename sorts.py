#!/usr/bin/env python
from random import random
from time import time

def timing(f):
    def wrap(*args):
        time1 = time()
        ret = f(*args)
        time2 = time()
        print('{0} function took {1} ms'.format(f.__name__, (time2-time1)*1000.0))
        return ret
    return wrap

@timing
def insertionSort(A):
    if len(A) < 2:
        return A
    for i in range(1, len(A)):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key
    return A


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


def merge(A, p, q, r):
    B = A[p:q]
    a = q
    b = 0
    while b < len(B) and a < r:  # both halves are not empty
        if B[b] < A[a]:
            A[p] = B[b]
            b += 1
        else:
            A[p] = A[a]
            a += 1
        p += 1

    while b < len(B):
        A[p] = B[b]
        b += 1
        p += 1
    while a < r:
        A[p] = A[a]
        a += 1
        p += 1
    return A


def main(argv):
    x = 2000
    pp = False

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
                pp = True
            else:
                pp = False

    A = [int(x*random()) for i in range(x)]
    B = A[:]
    print('start')
    if pp:
        print(A)
    print('\n')

    start = time()
    A = insertionSort(A)
    end = time()
    delta = end-start
    print('insertionSort:', delta)
    if pp:
        print(A)
    print('\n')

    start = time()
    B = mergeSort(B)
    end = time()
    delta = end-start
    print('mergeSort:', delta)
    if pp:
        print(B)

if __name__ == "__main__":
    import getopt
    import sys
    main(sys.argv[1:])
