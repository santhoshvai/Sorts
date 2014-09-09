"""
Basics of Unit_Testing: http://pymotw.com/2/unittest/
Author: Santhosh
Date: 09-Sep-2014
"""
import unittest
import mergeSort
import mergeSort2
import sys;sys.path.append('../')
from helperTest import *

showSplitTime = True

intSeq = generateIntegerTestCase()
sortedIntSeq = sorted(intSeq)
charSeq = generateCharacterTestCase()
sortedCharSeq = sorted(charSeq)


class mergeSortEqualityTest(unittest.TestCase):
  
  def testMergeSortMITVersion(self):
    intArray = list(intSeq)
    charArray = list(charSeq)
    intTime, intArray = timedcall(mergeSort.merge_sort_MIT, intArray)
    charTime, charArray = timedcall(mergeSort.merge_sort_MIT, charArray )
    self.failUnlessEqual(sortedIntSeq, intArray )
    self.failUnlessEqual(sortedCharSeq, charArray )
    printIntCharTime(intTime,charTime)
 
  def testMergeSortCLRSVersion(self):
    intArray = list(intSeq)
    intTime, _ = timedcall(mergeSort2.merge_sort_CLRS, intArray, 0, len(intArray))
    self.failUnlessEqual(sortedIntSeq, intArray)
    printIntCharTime(intTime,"Not Applicable")

  def testMergeSortWebVersion(self):
    intArray = list(intSeq)
    charArray = list(charSeq)
    intTime, _ = timedcall(mergeSort2.merge_sort_web, intArray, 0, len(intArray))
    charTime, _ = timedcall(mergeSort2.merge_sort_web, charArray, 0, len(charArray))
    self.failUnlessEqual(sortedIntSeq, intArray)
    self.failUnlessEqual(sortedCharSeq, charArray)
    printIntCharTime(intTime,charTime)

class mergeSortExceptionTest(unittest.TestCase):
  def testMergeSortCLRSVersion(self):
    charArray = list(charSeq)
    self.failUnlessRaises(TypeError, mergeSort2.merge_sort_CLRS, charArray, 0, len(charArray))

if __name__ == '__main__':
  unittest.main()