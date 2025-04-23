##	Filename: solveQuadraticEquation.py
##	Author: yu1
##	Date: 2025-02-05 13:15:53 +0800
## 
##	Description:
##		https://www.programiz.com/python-programming/examples/quadratic-roots
##
##      Python Program to Solve Quadratic Equation
##		To understand this example, 
##		you should have the knowledge of the following Python programming topics:
##			Python Data Types
##			Python Basic Input and Output
##			Python Operators
##		
##		The standard form of a quadratic equation is:
##			ax^2 + bx + c = 0, where
##			a, b and c are real numbers and
##			a ≠ 0
##
##		Solution:
##			(-b +- (b^2-4ac)**0.5)/2*a
##

def solution_quadratic_equation(coeffts_1, coeffts_2, coeffts_3):
	if not (isinstance(coeffts_1, int) and coeffts_1 != 0):
		raise ValueError("1st coefficient hava not to be 0 !!")
	if not all(isinstance(x, int) for x in (coeffts_1, coeffts_2, coeffts_3)):
		raise ValueError("All coefficients hava to be Integer!!")
		
	ans_1=(-coeffts_2+(coeffts_2**2-4*coeffts_1*coeffts_3)**0.5)/2*coeffts_1
	ans_2=(-coeffts_2-(coeffts_2**2-4*coeffts_1*coeffts_3)**0.5)/2*coeffts_1
	return (ans_1, ans_2)


coeffts_1=int(input('1st coefficient: '))
coeffts_2=int(input('2nd coefficient: '))
coeffts_3=int(input('3rd coefficient: '))               

print(solution_quadratic_equation(coeffts_1, coeffts_2, coeffts_3))
