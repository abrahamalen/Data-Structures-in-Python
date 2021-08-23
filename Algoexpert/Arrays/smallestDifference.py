"""
Given two arrays of integers, I am asked to write a function that finds two numbers, where one number comes from the first array and another number comes 
from the second array, with smallest absolute difference, and returns them in an array. 
In the resulting array, the number from the first array should come first.
"""

# Sample Input,
# arrayOne = [-1, 5, 10, 20, 28, 3];
# arrayTwo = [26, 134, 135, 15, 17];
# Sample Output is [28, 26].

# Solution
# Using sorting
# O(nlog(n) + mlog(m)) Time (where n & m are length of arrayOne and arrayTwo respectively) and O(1) Space complexity

def smallestDifference(arrayOne, arrayTwo) :
	arrayOne.sort()
	arrayTwo.sort()
	idxOne = 0
	idxTwo = 0
	smallest = float("inf")  # declaring smallest as infinity
	current = float("inf")   # declaring current as infinity
	smallestPair = []
	while idxOne < len(arrayOne) and idxTwo < len(arrayTwo) :
		firstNum = arrayOne[idxOne]
		secondNum = arrayTwo[idxTwo]
		if firstNum < secondNum :
			current = secondNum - firstNum
			idxOne += 1
		elif secondNum < firstNum :
			current = firstNum - secondNum
			idxTwo += 1
		else :
			return [firstNum, secondNum]
		if smallest > current :
			smallest = current
			smallestPair = [firstNum, secondNum]
	return smallestPair
