# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
# Example
# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]

# Answer : Solution done in 2 ways 

# The Brute Force way 
# O(n(logn)) Time & O(n) Space

def sortedSquareArray(array) :
    sortedSquares = [0 for _ in array]

    for idx in range(len(array)) :
        value = array[idx]
        sortedSquares[idx] = value * value

    sortedSquares.sort()
    return sortedSquares

# This is done using 2 pointers start and end
# O(n) Time & O(n) Space

def sortedSquaredArray(array) :
	sortedSquares = [0 for _ in array]
	smallerValueIdx = 0
	largerValueIdx = len(array) - 1
	
	for idx in reversed(range(len(array))) :
		smallerValue = array[smallerValueIdx]
		largerValue = array[largerValueIdx]
		
		if abs(smallerValue) > abs(largerValue) :
			sortedSquares[idx] = smallerValue * smallerValue
			smallerValueIdx += 1
		else :
			sortedSquares[idx] = largerValue * largerValue
			largerValueIdx -= 1
	
	return sortedSquares
