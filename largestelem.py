Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> list1 = [10,20,4,45,99]
>>> list1.sort()
>>> print("Largest element is:", list1[-1])
Largest element is: 99
>>> list1 = [55,85,77,100,500]
>>> print("Largest element is:", max(list1))
Largest element is: 500
>>> list1 =[]
>>> num = int(input("Enter number of elements in list:"))
Enter number of elements in list: 67,87,300,45,235
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    num = int(input("Enter number of elements in list:"))
ValueError: invalid literal for int() with base 10: ' 67,87,300,45,235'
>>> num = int(input("Enter number of elements in list:"))
Enter number of elements in list:5
>>> for i in range (1, num+1):
	ele = int(input("Enter elements:"))
	list1.append(ele)

	
Enter elements:24
Enter elements:55
Enter elements:66
Enter elements:89
Enter elements:56
>>> print("Largest element is:", max(list1))
Largest element is: 89
>>> 