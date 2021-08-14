# Given an array of integers nums and an integer target, return the two numbers such that they add up to target. You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Input: nums = [2,7,11,15], target = 9
# Output: [2, 7]
# Output: Because nums[0] + nums[1] == 9, we return [2, 7].

# Solutions
# 1) Brute Force method with complexitties  
#    O(n^2) Time & O(1) Space
  
def twoNumberSum(array, targetSum) :
	for i in range(len(array) - 1) :
		firstNum = array[i]
		for j in range(i+1, len(array)) :
			secondNum = array[j]
			if firstNum + secondNum == targetSum :
				return [firstNum, secondNum]
	return []

# 2) Using Hashmap
#    O(n) Time & O(n) Space

def twoNumberSum(array, targetSum) :
	nums = {}
	for num in array :
		result = targetSum - num
		if result in nums :
			return [result, num]
		else :
			nums[num] = True
	return []

# 3) Using sorting at the begining and then traverse through the array once
#    O(nlogn) Time & O(1) Space

def twoNumberSum(array, targetSum) :
	array.sort()
	left = 0
	right = len(array) - 1
	while left < right :
		currentSum = array[left] + array[right] 
		if currentSum == targetSum :
			return [array[left], array[right]]
		elif currentSum < targetSum :
			left += 1
		elif currentSum > targetSum :
			right -= 1
	return []


