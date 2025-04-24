##	Filename: 008_diceRoller.py
##	Author: yu1
##	Date: 2025-04-24 07:57:55 +0800
## 
##	Description:
## 		using random, make a virtualize dice (1~6)
##

import random

range=int(6)

def rolling_dice(range):
	return random.randint(1, range)

print(rolling_dice(range))
