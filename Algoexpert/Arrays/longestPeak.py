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
