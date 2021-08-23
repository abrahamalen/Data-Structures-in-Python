# Given an array of distinct integers and an integer representing a target sum, write a function that find all combinations of three numbers in the array
# that add up to the target sum. The function should return a 2-dimensional array of all these combinations. The numbers in each combination should be ordered 
# in ascending order, and the combinations themselves should also be ordered in ascending order, for instance: [[-8, 2, 6],[-8, 3, 5], [-6, 1, 5]]. 
# If there is no such combination, return an empty array.
# Sample input -> array = [12, 3, 1, 2, -6, 5, -8, 6] , targetSum = 0
# Output -> [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]

# Solution

# Using sorting O(n^2) Time and O(n) Space
def threeNumberSum(array, targetSum) :
	array.sort()
	triplets = []
	for i in range(len(array) - 2) :
		left = i + 1
		right = len(array) - 1
		while left < right :
			currentSum = array[i] + array[left] + array[right]
			if currentSum == targetSum :
				triplets.append([array[i], array[left], array[right]])
			    left += 1
				right -= 1
			elif currentSum < targetSum :
				left += 1
			elif currentSum > targetSum :
				right -= 1		
	return triplets

