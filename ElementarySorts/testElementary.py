"""
Basics of Unit_Testing: http://pymotw.com/2/unittest/
Author: Santhosh
Date: 09-Sep-2014

Note:
    List1 = List2 #copies reference to same list in memory
    list1 - list( List2 ) # makes a copy of the list in a new place in memory and references it
"""
import unittest
import bubbleSort
import selectionSort
import insertionSort
import sys;sys.path.append('../')
from helperTest import *

intSeq = generateIntegerTestCase()
sortedIntSeq = sorted(intSeq)
charSeq = generateCharacterTestCase()
sortedCharSeq = sorted(charSeq)

class equalityTest(unittest.TestCase):
    def testSelectionSort(self):
        intArray, charArray = getArrayCopies(intSeq, charSeq)   
        intTime, _ = timedcall(selectionSort.selectionSort,  intArray )
        charTime, _ = timedcall(selectionSort.selectionSort, charArray )
        self.failUnlessEqual(sortedIntSeq, intArray)
        self.failUnlessEqual(sortedCharSeq, charArray)
        printIntCharTime(intTime,charTime)

    def testInsertionSort(self):
        intArray, charArray = getArrayCopies(intSeq, charSeq)  
        intTime, _ = timedcall(insertionSort.insertionSort, intArray )
        charTime, _ = timedcall(insertionSort.insertionSort, charArray )
        self.failUnlessEqual(sortedIntSeq, intArray)
        self.failUnlessEqual(sortedCharSeq, charArray)
        printIntCharTime(intTime,charTime)

    def testBubbleSort(self):
        intArray, charArray = getArrayCopies(intSeq, charSeq)  
        intTime, _ = timedcall(bubbleSort.bubble_sort, intArray )
        charTime, _ = timedcall(bubbleSort.bubble_sort, charArray )
        self.failUnlessEqual(sortedIntSeq, intArray)
        self.failUnlessEqual(sortedCharSeq, charArray)
        printIntCharTime(intTime,charTime)

if __name__ == '__main__':
    unittest.main()