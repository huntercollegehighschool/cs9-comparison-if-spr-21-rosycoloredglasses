'''
______
PART 1
______
The code below prompts the user to enter two numbers, and then prints out the smaller of the numbers entered. Modify so that it prompts the user to enter THREE numbers, and then prints the smallest of the three numbers entered in a sentence.

(Hint: You'll need to be careful for the cases when the user enters the same number twice or all three times.)

An example of what should appear on the console when the code is run:

Enter a number: 11
Enter another number: 2
Enter another number: 5

The smallest number is 2
'''

number1 = int(input("Enter a number: "))
number2 = int(input("Enter another number: "))
number3 = int(input("Enter another number: "))

if number1 <= number2 <= number3 or number1 <= number3 <= number2:
  print("The smallest number is ", number1)
elif number2 <= number1 <= number3 or number2 <= number3 <= number1:
  print("The smallest number is ", number2)
else:
  print("The smallest number is ", number3)