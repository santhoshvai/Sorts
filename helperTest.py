"""
Helper functions for the unitTest programs
"""
import time

showSplitTime = False

def generateIntegerTestCase(nRange = 4000):
  import random
  integerSeq = [random.randint(1, 1000) for _ in range(nRange)]
  return integerSeq

def generateCharacterTestCase(nRange = 4000):
  import random
  characterSeq = [random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(nRange)]
  return characterSeq

def timedcall(fn, *args):
    "Call function with args; return the time in seconds and result."
    t0 = time.time()
    result = fn(*args)
    t1 = time.time()
    return t1-t0, result

def printIntCharTime(intTime,charTime):
  if showSplitTime:
      print "\n\n" + "Time taken for integer sequence: " + str(intTime)
      print "Time taken for character sequence: " + str(charTime) + "\n"

def getArrayCopies(intSeq, charSeq):
  """
  Note:
    List1 = List2 #copies reference to same list in memory
    list1 = list( List2 ) # makes a copy of the list in a new place in memory and references it
  """
  intArray = list(intSeq)
  charArray = list(charSeq)
  return intArray, charArray