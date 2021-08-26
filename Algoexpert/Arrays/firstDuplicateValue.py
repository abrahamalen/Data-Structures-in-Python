"""
Given an array of integers between 1 and n, inclusive where 'n' is the length of the array, write a function that returns the first integer 
that appears more than once(when the array is read from left to right).
In other words, out of all the integers that might occur more than once in the input array, your function should return the one whose 
first duplicate value has the minimum index.
If no integer appears more than once, your function should return -1.
(Note that you are allowed to mutate the input array.)

Sample Input #1
array = [2, 1, 5, 2, 3, 3, 4]
Output = 2 // 2 is the first integer that appears more than once.
           // 3 also appears more than once, but the second 3 appears after the second 2.

Sample Input #2
array = [2, 1, 5, 3, 3, 2, 4]
Output = 3 // 3 is the first integer that appears more than once.
           // 2 also appears more than once, but the second 2 appears after the second 3.
"""

# Solution
# 1) Brute Force approach with O(n^2) Time & O(1) Space complexity

def firstDuplicateValue(array):
	minimumSecondIndex = len(array)
	for i in range(len(array)):
		value = array[i]
		for j in range(i + 1, len(array)):
			valueToCompare = array[j]
			if value == valueToCompare:
				minimumSecondIndex = min(minimumSecondIndex, j)
	
	if minimumSecondIndex == len(array):
		return -1
	
	return array[minimumSecondIndex]

# 2) Solution using Set which is more optimal than previous solution.
#    Complexities O(n) Time & O(n) Space.

def firstDuplicateValue(array):
	seen = set()
	for value in array:
		if value in seen:
			return value
		seen.add(value)
		
	return -1

# 3) A more optimal solution with complexities O(n) Time and O(1) Space.
#    This solution considers the fact that all of the values are inthe range '1 to n' and we are allowed to mutate the input array.

def firstDuplicateValue(array):
	for value in array:
		absValue = abs(value)
		if array[absValue - 1] < 0:
			return absValue
		array[absValue - 1] *= -1
		
	return -1
