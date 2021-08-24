"""
Write a function that takes in an array of integers and returns a boolean representing whether the array is monotonic.
An array is said to be monotonic if its elements, from left to right, are entirely non-increasing or entirely non-decreasing.
Non-increasing elements aren't necessarily exclusively increasing; they simply don't decrease.
Not that empty arrays and arrays of one element are monotonic.

Sample Input: array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
Sample Output: true
"""

# Solution
# 1) Solution which is somewhat complex and run with complexities O(n) Time & O(1) Space
def isMonotonic(array):
	if len(array) <= 2:
		return True
	direction = array[1] - array[0]
	for i in range(2, len(array)):
		if direction == 0:
			direction = array[i] - array[i - 1]
			continue
		if breaksDirection(direction, array[i - 1], array[i]):
			return False
	return True

def breaksDirection(direction, previousInt, currentInt):
	difference = currentInt - previousInt
	if direction > 0:
		return difference < 0
	return difference > 0

# 2) Somewhat better and simpler code which is understandable and have O(n) Time & O(1) Space complexities.
def isMonotonic(array):
	isNonDecreasing = True
	isNonIncreasing = True
	
	for i in range(1, len(array)):
		if array[i] < array[i-1]:
			isNonDecreasing = False
		if array[i] > array[i-1]:
			isNonIncreasing = False
	
	return isNonDecreasing or isNonIncreasing 

