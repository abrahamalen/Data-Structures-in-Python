"""
Given an array of positive integers representing the values of coins in your possession, write a function that returns the minimum amount of change (the minimum sum 
of money) that you cannot create. The given coins can have any positive integer value and aren't necessarily unique (.e., you can have multiple coins of the same value). 
For example, if you're given coins = [1, 2, 5], the minimum amount of change that you can't create is 4. If you're given no coins, the minimum amount of change
that you can't create is 1.
Input [5, 7, 1, 1, 2, 3, 22] >> Output 20
"""

# Solution
# 1) Using sorting
# O(nlogn) Time & O(1) Space

def nonConstructibleChange(coins) :
	coins.sort()
	changeCreated = 0
	for coin in coins :
		if coin > changeCreated +1 :
			return changeCreated + 1
		changeCreated += coin
	return changeCreated + 1

# 2) Using sorting but in another logic

def nonConstructibleChange(coins) :
	coins.sort()
	changeCreated = 0
	for coin in coins :
		if coin <= changeCreated + 1 :
			changeCreated += coin
		elif coin > changeCreated + 1 :
			break
	return (changeCreated + 1)
