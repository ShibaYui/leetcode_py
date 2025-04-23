##	Filename: caculateAreaOfTriangle.py
##	Author: yu1
##	Date: 2025-02-05 11:05:07 +0800
## 
##	Description:
##		Python Program to Calculate the Area of a Triangle
##		To understand this example, 
##		you should have the knowledge of the following Python programming topics:
##			Python Basic Input and Output
##	   		Python Data Types
##			Python Operators
##		
##		get three sides of triangle (float)
##			side_1
##			side_2
##			side_3
##		caculate area via Heron's formula:
##			h=(sida_1+side_2+side_3)/2
##			area=√(h(h-side_1)*(h-side_2)*(h-side_3))
##

side_1=float(input('Enter 1st side: '))
side_2=float(input('Enter 2nd side: '))
side_3=float(input('Enter 3rd side: '))

h=(side_1+side_2+side_3)/2
area=(h*(h-side_1)*(h-side_2)*(h-side_3))**0.5
print(f'Ans: {area}')
