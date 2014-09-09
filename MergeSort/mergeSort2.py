"""
************************ MERGE SORT *********************************

Properties
    * Stable
    * O(n) extra space for arrays (as shown)
    * O(lg(n)) extra space for linked lists
    * O(n.lg(n)) time
    * Not adaptive
    * Does not require random access to data

Discussion

    Merge sort is very predictable. It makes between 0.5*lg(n) and lg(n) 
    comparisons per element, and between lg(n) and 1.5*lg(n) swaps per 
    element. The minima are achieved for already sorted data; the maxima
    are achieved, on average, for random data. If using O(n) extra space
    is of no concern, then merge sort is an excellent choice: It is simple
    to implement, and it is the only stable O(n.lg(n)) sorting algorithm. 
    Note that when sorting linked lists, merge sort requires only O(lg(n))
    extra space (for recursion).
    
    Merge sort is the algorithm of choice for a variety of situations: when 
    stability is required, when sorting linked lists, and when random access
    is much more expensive than sequential access (for example, external 
    sorting on tape).
    
    There do exist linear time in-place merge algorithms for the last step 
    of the algorithm, but they are both expensive and complex. The complexity
    is justified for applications such as external sorting when O(n) extra 
    space is not available. 
"""

def merge_sort_web(A,start,end):
    """
    Sort list A into order, and return result.
    """
    if start < end:
        mid = (start+end)//2
    if len(A[start:end])==1: 
        return A
    merge_sort_web(A, start, mid)
    merge_sort_web(A, mid, end)
    merge(A,start,mid,end)

def merge(a,start, mid, end):
    """
    Requires: the list with elements that need to be sorted
    Approach: http://www.sorting-algorithms.com/merge-sort  | only 1/2s length extra copy :) O(n/2) space
    """  
    b = a[start:mid]
    k = start
    i = 0
    j = mid
    thisMid = len(b)
    while (i<thisMid) and (j<end):
        if a[j] < b[i]:
            a[k] = a[j]
            k+=1;j+=1
        else:
            a[k] = b[i]
            k+=1;i+=1
    while i<thisMid:
        a[k] = b[i]
        k+=1;i+=1

def merge_sort_CLRS(A,start,end, checkedType = False):
    """
    Sort list A into order, and return result.
    Requires: the list to contain only integers
    """
    if not checkedType:#to avoid repeated checking | Done only once
        for n in A:
            if not isinstance(n, int): #list has to contain only integers
                raise TypeError
    if start < end:
        mid = (start+end)//2
    if len(A[start:end])==1: 
        return A
    merge_sort_CLRS(A, start, mid, True) #True since already type has been checked once
    merge_sort_CLRS(A, mid, end, True)
    mergeCLRS(A,start,mid,end)

def mergeCLRS(A,start, mid, end):
    """
    Requires: the list to contain only integers
    Approach: CLRS page 31 and 32 | two copies each => O(n) space!
    """
    L = A[start:mid]
    R = A[mid:end]
    k = start
    i = 0
    j = 0
    L.append(9223372036854775807) # sentinel  
    R.append(9223372036854775807) # sentinel
    # sys.maxint
    # >> 9223372036854775807
    while k<=(end-1):
        if L[i]<=R[j]:
            A[k] = L[i]
            i += 1; k += 1
        else:
            A[k] = R[j]
            j += 1; k += 1


def main():
    import random
    seq = [random.randint(1, 10) for _ in range(4000)]
    sorted_seq = sorted(seq)
    merge_sort_CLRS(seq, 0, len(seq))
    assert (seq == sorted_seq)
    print "assertion pass"

if __name__ == "__main__":
    main()    