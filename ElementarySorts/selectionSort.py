# **************** SELECTION SORT **************************************
# Properties
#
#    Not stable
#    O(1) extra space
#    O(n2) comparisons
#    O(n) swaps
#    Not adaptive
#
# Discussion
#
#    From the comparisons presented here, one might conclude that selection sort
#    should never be used. It does not adapt to the data in any way (notice that
#    the four animations above run in lock step), so its runtime is always quadratic.
#  
#    However, selection sort has the property of minimizing the number of swaps. In 
#    applications where the cost of swapping items is high, selection sort very 
#    well may be the algorithm of choice. 
#
# Approach:
#    Selection sort is a step up from insertion sort from a memory
#    viewpoint. It only swaps elements that need to be swapped. In terms
#    of time complexity, however, insertion sort is better.
# ======================================================================= 
def selectionSort( array ):
    """
    First find the smallest element of A and exchange it with A[1]
    Then find the second smallest element of A, exchange with A[2]
    Continue in this manner for the first n-1 elements of A
    """
    n = len( array )    
    for i in range( n-1 ):
        minimum = i 
        # find min
        for j in range( i + 1 , n ):
            if array[j] < array[minimum]:
                minimum = j # update the min index
        # swap the min and the current element
        array[minimum], array[i] = array[i], array[minimum]

def main():
    array = [54,26,93,17,77,31,44,55,20]
    print;print "inputArray: " + str(array)
    selectionSort( array )
    print;print "sortedArray: " + str(array)

if __name__ == "__main__":
    main()  
