Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def Fibonacci(n):
	if n<0:
		print("Fibonacci can't be computed")
		elif n==1:
			
SyntaxError: invalid syntax
>>> 
>>> def Fibonacci(n):
	if n<0:
		print("Fibonacci can't be computed")
		elif n==1:
			
SyntaxError: invalid syntax
>>> 
>>> def Fibonacci(n):
	if n<0:
		print("Fibonacci can't be computed")
	elif n==1:
		return 0
	elif n==2:
		return 1
	else:
		return Fibonacci(n-1)+Fibonacci(n-2)

	
>>> n=10
>>> print(Fibonacci(n))
34
>>> 