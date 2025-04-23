##	Filename: twoSum.py
##	Author: yu1
##	Date: 2025-04-22 08:21:16 +0800
## 
##	Description:
##		給定一個整數陣列 nums 和一個目標值 target，請你在陣列中找出兩個數字，
##		它們的和等於目標值，並回傳它們的索引值。
##		你可以假設每種輸入只會有一個解，且不能使用同一個元素兩次。
##

def twoSum(nums, target):
	for i in range(len(nums)):
		for j in range(i+1, len(nums)):
			if nums[i] + nums[j] == target:
				return [i, j]

