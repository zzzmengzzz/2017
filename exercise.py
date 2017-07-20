import datetime
import random


#Exercise from: http://www.practicepython.org/

def exercise1():
	#Create a program that asks the user to enter their name and their age. 
	#Print out a message addressed to them that tells them the year that they will turn 100 years old.
	#Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. 
	#Print out that many copies of the previous message on separate lines. 
	try:
		userName = input('Please enter your name:')
		userAge = int(input('Now your age:'))
		number = int(input('Enter a number:'))
		currentYear = datetime.datetime.now().year
		yearWhen100 = currentYear + (100 - userAge)
		outputString = userName + ", it will be " + str(yearWhen100) + " when you turn 100 years old!"
		for num in range(number):
			print (outputString)

	except ValueError:
		print("One of the number entered was not an int!")

def exercise2():
	#Ask the user for a number. 
	#Depending on whether the number is even or odd, print out an appropriate message to the user.
	#If the number is a multiple of 4, print out a different message.
	#Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). 
	#If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
	try:
		number = int(input('Enter a number:'))
		residue = number % 2
		residue4 = number % 4
		if (residue4 == 0):
			print("Special case, this is a multiple of 4!")
		elif(residue == 0):
			print("The number entered is even.")
		else:
			print("The number entered is odd.")
		num = int(input("Number to be checked:"))
		check = int(input("Number to divide by:"))
		if(num % check == 0):
			print(str(num) + " can be divided by " + str(check))
			print("The result is " + str(num/check))
		else:
			print(str(num) + " cannot be evenly divided by " + str(check))

	except ValueError:
		print("Number entered was not an int!")

def exercise3():
	#write a program that prints out all the elements of the list that are less than 5
	#Ask the user for a number and return a list that contains only elements from the original list a that are smaller 
	#than that number given by the user.
	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
	number = int(input('Enter a number:'))
	b = [element for element in a if element < number]
	print(b)

def exercise4():
	#Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
	number = int(input('Enter a number:'))
	a = range(1,number + 1)
	b = [element for element in a if number%element == 0]
	print(b)

def exercise5():
	#write a program that returns a list that contains only the elements that are common between the lists 
	a = random.sample(range(0,100),random.randint(0,20))
	b = random.sample(range(0,100),random.randint(0,20))
	c = list(set(a)&set(b))
	print(c)

def exercise6():
	#Ask the user for a string and print out whether this string is a palindrome or not. 
	sentence = input("Enter a sentence:")
	length = len(sentence)
	tester = True
	for index in range(length):
		if sentence[index] != sentence[length-index-1]:
		 	tester = False
		 	break
	print("The word entered is a palindrome: " + str(tester))

def exercise7():
	#Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.
	a = [element for element in random.sample(range(0,100),random.randint(0,20)) if element%2 == 0]
	print(a)

exercise7();