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

def exercise8():
	#Make a two-player Rock-Paper-Scissors game. 
	#Changed to one player vs computer
	print("Available moves: rock, paper, scissors, quit (case sensitive).")
	while True:
		command = input("\nEnter your move:")
		if command == "quit":
			break
		else:
			move = ['rock','paper','scissors']
			computerMove = random.choice(move)
			if command == computerMove:
				print("Tie!")
			elif command == "rock" and computerMove == "scissors":
				print("You win! Rock beats scissors!")
			elif command == "scissors" and computerMove == "paper":
				print("You win! Scissors beats paper!")
			elif command == "paper" and computerMove == "rock":
				print("You win! Paper beats rock!")
			elif computerMove == "rock" and command == "scissors":
				print("You lose! Computer plays rock. Rock beats scissors!")
			elif computerMove == "scissors" and command == "paper":
				print("You lose! Computer plays Scissors. Scissors beats paper!")
			elif computerMove == "paper" and command == "rock":
				print("You lose! Computer plays paper.Paper beats rock!")
			else:
				print("Wrong input! Try again.")
				print("Available moves: rock, paper, scissors, quit (case sensitive).")

def exercise9():
	#Generate a random number between 1 and 9 (including 1 and 9). 
	#Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
	#Keep the game going until the user types “exit”
	#Keep track of how many guesses the user has taken, and when the game ends, print this out.

	count = 0
	number = random.randint(1,9)
	command = input("Enter your guess here:")

	while command != 'exit':
		try:
			if int(command) == number:
				count += 1
				number = random.randint(1,9)
				command = input("You got it! Enter your guess for new number here:")
			elif int(command) > number:
				count += 1
				command = input("Too high! New guess:")
			elif int(command) < number:
				count += 1
				command = input("Too low! New guess:")
				
		except ValueError:
			print("Wrong entry")
			break
	print(count)

#exercise10 is the same as exercise5

def exercise11():
	#Ask the user for a number and determine whether the number is prime or not.
	try:
		number = int(input("Enter your number:"))
		a = range(1, number + 1)
		isDivisor = False
		for element in a:
			if element == 1 or element == number:
				continue
			if number % element == 0:
				isDivisor = True
				break
		if isDivisor:
			print(str(number) + " is not a prime number.")
		else:
			print(str(number) + " is a prime number.")
	except ValueError:
		print("Your input is not an int.")

def exercise12(listA):
	#Write a program that takes a list of numbers and makes a new list of only the first and last elements of the given list.
	b = [listA[0],listA[-1]]
	return(b)

def exercise13():
	#Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. 
	try:
		number = int(input("How many Fibonnaci numbers do you want?"))
		a = 0
		b = 1
		myList = []
		while number != 0:
			myList.append(b)
			temp = a
			a = b
			b = temp + b
			number -=1
		print(myList)

	except ValueError:
		print("Input must be an int!")

def exercise14():
	pass

exercise13();























