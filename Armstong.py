Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> num = int(input("Enter a number:"))
Enter a number:
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    num = int(input("Enter a number:"))
ValueError: invalid literal for int() with base 10: ''
>>> num = int(input("Enter a number:"))
Enter a number: 1
>>> sum = 0
>>> temp = num
>>> while temp>0:
	digit = temp % 10
	sum += digit ** 3
	temp//= 10
	if num == sum:
		print(num,"is an Armstrong number")
	else:
		print(num,"is not an armstrong number")

		
1 is an Armstrong number
>>> 
>>> 