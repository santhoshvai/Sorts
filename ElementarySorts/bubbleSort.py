"""
************************ BUBBLE SORT *********************************

Properties

    Stable
    O(1) extra space
    O(n2) comparisons and swaps
    Adaptive: O(n) when nearly sorted

Discussion

  Bubble sort has many of the same properties as insertion sort, 
  but has slightly higher overhead. In the case of nearly sorted data,
  bubble sort takes O(n) time, but requires at least 2 passes through
  the data (whereas insertion sort requires something more like 1 pass).  
"""

def bubble_sort(A):
  n = len(A)
  for i in range(n):
    swapped = False
    for j in range(n-1,i,-1): #reverse range
      if A[j] < A[j-1]:
        A[j], A[j-1] = A[j-1], A[j] #swap
        swapped = True
    if not swapped: break #means that we have already sorted! so break

def main():
  import random
  seq = [random.randint(1, 4000) for _ in range(4000)]
  sorted_seq = sorted(seq)
  bubble_sort(seq)
  assert (seq == sorted_seq)
  print;print "assertion pass"

if __name__ == "__main__":
    main()    