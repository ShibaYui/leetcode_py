##	Filename: twoSum.py
##	Author: yu1
##	Date: 2025-04-22 08:21:16 +0800
## 
##	Description:
##		給定一個整數陣列 nums 和一個目標值 target，請你在陣列中找出兩個數字，
##		它們的和等於目標值，並回傳它們的索引值。
##		你可以假設每種輸入只會有一個解，且不能使用同一個元素兩次。
##
##	Solution
##		hash table
##

def twoSum(nums, target):
	index = {}
	for i, num in enumerate(nums):	
	# 使用enumerate()得到"i"(索引)和"num"(實際值)
		another = target - num		
		# 總和是target，另一個(another)就是target-num(索引實際值)
		if another in index:
			return [index[another], i]
		index[num]=i
		# 如果沒有找到，就將索引值存入，供下次索引
	
