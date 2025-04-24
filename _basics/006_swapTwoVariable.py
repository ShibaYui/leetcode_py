##	Filename: 006_swapTwoVariable.py
##	Author: yu1
##	Date: 2025-04-24 06:16:42 +0800
## 
##	Description:
## 		python progran to swap two variable
##

def swap_two_variable(var_1, var_2):
	temp=0
	temp=var_1
	var_1=var_2
	var_2=temp
	print("Message: Swap the values of two variables.")
	return (var_1, var_2)

var_1=int(input('1st Variable: '))
var_2=int(input('2nd Variable: '))

print(swap_two_variable(var_1, var_2))
