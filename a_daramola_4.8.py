#Akinola Daramola Jr
#Programming Exercise 4.8
#Due Date: 06/29/22

"""
Sum of Numbers
Write a program with a loop that asks the user to enter a series of positive numbers.
The user should enter a negative number to signal the end of the series.
After all the positive numbers have been entered, the program should display their sum.

"""

#Declaring value of variable dynamically
number = float(input("Enter a number: "))

#Reassigning number value to total
total = number

#While Loop
while number > 0: #Iterates while number input is positive (positive numbers only)
    number = float(input("Enter a number: ")) #Prompts user to input number
    if number > 0: #if statement for positive numbers
        total += number #Calculates sum total of positive numbers
    else:
        print(f"Total: {total:,.2f}") #Displays sum total
 
                   
        
        
    
