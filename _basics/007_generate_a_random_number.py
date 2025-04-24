##	Filename: 007_generate_a_random_number.py
##	Author: yu1
##	Date: 2025-04-24 06:54:53 +0800
## 
##	Description:
##		To generate random number in Python, randint() function is used. This function is defined in random module.
##		Ref. https://www.programiz.com/python-programming/modules/random
##
##		get random.seed volue to create float random value (between 0~1)
##

import random

def generateRandomNumber(seed_val):
	random.seed(seed_val)
	return random.random()

seed_val=int(input('Random.seed() Value: '))

print(generateRandomNumber(seed_val))
	
