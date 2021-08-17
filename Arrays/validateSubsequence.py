# Implement a function that takes two arrays of integers as input and finds whether all the numbers in the sequence array appear in the first array and they 
# appear in the same order. In other words, the function need to find out if we can get the sequence array, when we delete some or no elements in the first 
# array without changing the order of the remaining elements.
# For example:
# array = [5, 1, 22, 25, 6, -1, 8, 10];
# sequence = [1, 6, -1, 10];
# The output should be true.

# Solution
# 1) Using while loop. O(n) Time & O(1) Space
  
  def isValidSubsequence(array, sequence):
	arrayIdx = 0
	seqIdx = 0
	while arrayIdx < len(array) and seqIdx < len(sequence) :
		if array[arrayIdx] == sequence[seqIdx] :
			seqIdx += 1
		arrayIdx += 1
	return seqIdx == len(sequence)

# 2) Using for loop. O(n) Time & O(1) Space
   
  
