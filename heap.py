def heapsort(lst):

  for start in range((len(lst)-2)/2, -1, -1):
    siftdown(lst, start, len(lst)-1)

    for end in range(len(lst)-1, 0, -1):
        lst[end], lst[0] = lst[0], lst[end]
        siftdown(lst, 0, end - 1)
    return lst

def siftdown(lst, start, end):
    root = start
    while True:
        child = root * 2 + 1
        if child > end: break
        if child + 1 <= end and lst[child] < lst[child + 1]:
            child += 1
        if lst[root] < lst[child]:
            lst[root], lst[child] = lst[child], lst[root]
            root = child
        else:
            break

def heapify(array):
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
