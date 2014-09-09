def merge_sort_MIT(A):
    """
    Sort list A into order, and return result.
    """
    n = len(A)
    if n==1: 
        return A
    mid = n//2     # floor division
    L = merge_sort_MIT(A[:mid])
    R = merge_sort_MIT(A[mid:])
    return merge(L,R)

def merge(L,R):
    """
    Given two sorted sequences L and R, return their merge.
    """
    i = 0
    j = 0
    answer = []
    while i<len(L) and j<len(R):
        if L[i]<R[j]:
            answer.append(L[i])
            i += 1
        else:
            answer.append(R[j])
            j += 1
    if i<len(L):
        answer.extend(L[i:])
    if j<len(R):
        answer.extend(R[j:])
    return answer

def main():
    array = [54,26,93,17,77,31,44,55,20]
    print;print "inputArray: " + str(array)
    answer = merge_sort_MIT( array )
    print;print "sortedArray: " + str(answer)

if __name__ == "__main__":
    main()    