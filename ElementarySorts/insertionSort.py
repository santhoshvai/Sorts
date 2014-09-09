# **************** INSERTION SORT **************************************
# Properties
# 
#     Stable
#     O(1) extra space
#     O(n2) comparisons and swaps
#     Adaptive: O(n) time when nearly sorted
#     Very low overhead
# 
# Discussion
# 
#     Although it is one of the elementary sorting algorithms with O(n2) 
#     worst-case time, insertion sort is the algorithm of choice either 
#     when the data is nearly sorted (because it is adaptive) or when 
#     the problem size is small (because it has low overhead).
#     
#     For these reasons, and because it is also stable, insertion sort 
#     is often used as the recursive base case (when the problem size 
#     is small) for higher overhead divide-and-conquer sorting 
#     algorithms, such as merge sort or quick sort. 
#======================================================================= 
def insertionSort( array ):
    n = len( array )    
    for i in range(1,n):
        key = array[i]
        #Insert A[i] into the sorted sequence A[1...i-1]
        j = i - 1
        while (j>=0) and (array[j]>key):
            array[j+1] = array[j]
            j = j-1
        array[j+1] = key

def main():
    import random
    seq = [random.randint(1, 10) for _ in range(4000)]
    sorted_seq = sorted(seq)
    insertionSort(seq)
    assert (seq == sorted_seq)
    print "assertion pass"

if __name__ == "__main__":
    main()  
