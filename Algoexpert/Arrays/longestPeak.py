"""
Write a fucntion that takes in an array of integers and returns the length of the longest peak in the array.
A peak is defines as adjacent integers in the array that are strictly increasing until they reach a tip(the highest value in the peak),
at which point they become strictly deacreasing. At least three integesr are required to form a peak.
For example, the integers 1, 4, 10, 2 form a peak but the integers 4, 0, 10 don't and neither do the integers 1, 2, 2, 0.
Similarly, the integers 1, 2, 3 don't form a peak because there aren't any strictly decreasing integers after the 3.

Sample input
array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
Sample output
6 // 0, 10, 6, 5, -1, -3
"""

# Solution
# Complexity O(n) Time and O(1) Space.
def longestPeak(array):
	longestPeakLength = 0
	i = 1
	while i < len(array) - 1:
		isPeak = array[i - 1] < array[i] and array[i] > array[i + 1]
		if not isPeak:
			i += 1
			continue
		
		leftIdx = i - 2
		while leftIdx >= 0 and array[leftIdx] < array[leftIdx + 1]:
			leftIdx -= 1
		rightIdx = i + 2
		while rightIdx <  len(array) and array[rightIdx] < array[rightIdx - 1]:
			rightIdx += 1
			
		currentPeakLength = rightIdx - leftIdx - 1
		longestPeakLength = max(longestPeakLength, currentPeakLength)
		i = rightIdx
	
	return longestPeakLength
