                # ***LAB 1***


# Task 1
                  # Program 1:  integers
a = 5
b = 10
print( a + b)

# Program 2: Check if a number is even or odd
number = 7
if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")
               #  program 1 : Float 
               # Fahrenheit to Celsius
fahrenheit = 27.4
celsius = (fahrenheit - 32) * 5/9
print(f"{fahrenheit}°F is equal to {celsius}°C")


             # Program 2: Celsius to Fahrenheit
celsius = 25.0
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit)

              # Program 1:  Strings
greeting = "Hello"
name = "World"
print(greeting + " " + name)

               # Program 2:  String 
word = "Hello"
print((  word  + "" )* 3)

                   # Program 1:  List
fruits = ["apple", "orange", "cherry"]
print("First fruit:", fruits[0])

                    # Program 2: List
numbers = [1, 2, 3]
numbers.remove(1)

print("Modified list:", numbers)

                    # Program 1:  Tuple 
coordinates = (10, 20)
print("X-coordinate:", coordinates[0])

                      # Program 2: Tuple 
axis = (5, 10)
x , y = axis
print("x:", x, "y:", y)

                    # Program 1:  Dictionary 
person = {"name": "Ali", "age": 25}
print("Name:", person["name"])

                       # Program 2:  Dictionary 
person["city"] = "New York"
person["age"] = 26
print("Updated person info:", person)


                    # Program 1:  Set 
colors = {"red", "green", "blue"}
colors.add("yellow")
print("Colors set:", colors)

                     # Program 2: Set
if "green" in colors:
    print("Green is in the set")


           # Program 1: Boolean  with AND and OR
a = True
b = False
print("a AND b:", a and b)
print("a OR b:", a or b)

               # Program 2: Boolean
num = -10
is_positive = num > 0
print("Is number positive?", is_positive)

                       # Task 2
          # 10 Programs :  Shapes using Strings
print("Square:\n" + "****\n" * 4)
print("Triangle:\n  *  \n *** \n*****")
print("Rectangle:\n" + "*****\n" * 3)
print("Diamond:\n  *  \n *** \n*****\n *** \n  *  ")
print("Arrow:\n  *  \n *** \n*****\n  |  \n  |  ")
print("Heart:\n ** ** \n*******\n ***** \n  ***  \n   *   ")
print("Right-angled triangle:\n*\n**\n***\n****")
print("Divide:\n  *  \n*****\n  *   ")
print("Star:\n  *  \n * * \n*****\n * * \n  *  ")
print("House:\n   *   \n  ***  \n ***** \n*******\n |   |")


                       # ***LAB 2***
                       
                
# Task 1
   # This will be True or False

value = 12 > 3  
print("Is value true?", value)

                 # Task 2
# Calculator program
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operator = input("Enter operator (Add, Sub, Multi, Div): ")
input("Select any one")

if operator == "Add":
    print("Result:", a + b)
elif operator == "Sub":
    print("Result:", a - b)
elif operator == "Multi":
    print("Result:", a * b)
elif operator == "Div":
    if b != 0:
        print("Result:", a / b)
    else:
        print("Error: Division by zero")
else:
    print("Invalid operator")

                  # Task 3
                  
          # Using single quotes
text1 = 'Single Quotes'
print(text1)

       # Using double quotes
text2 = "Double Quotes"
print(text2)

          # Using triple quotes 
text3 = """Triple Quotes"""
print(text3)              


                            # ***LAB 3***
                            
                            
                            
                            # Code:
# ATM Machine Program

# Initial balance
balance = 1000

# Correct PIN
correct_pin = 1234

# Function to display the menu
def atm_menu():
    print("Asalam-o-alaikum :")
    print("WELCOME TO ATM MASHINE:")
    print("\nATM Menu:")
    print("1. Check Balance")
    print("2. Withdraw Money")
    print("3. Exit")

# Function to check balance
def check_balance():
    print(f"\nYour current balance is: ${balance}")

# Function to withdraw money
def withdraw_money():
    global balance
    amount = float(input("\n Piyar Ali please Enter the amount to withdraw: "))
    if amount <= balance:
        balance -= amount
        print(f"${amount} withdrawn.Now your remaining balance is : ${balance}")
    else:
        print("Insufficient balance!")

# Main program logic
def atm():
    # User enters PIN
    pin = int(input("Enter your PIN: "))
    
    # Check if the PIN is correct
    if pin == correct_pin:
        while True:
            atm_menu()
            choice = input("\n Please Choose an option of the following: ")
            
            if choice == '1':
                check_balance()
            elif choice == '2':
                withdraw_money()
            elif choice == '3':
                print("Exiting the ATM. Thank you!")
                break
            else:
                print("Invalid option. Please try again.")
    else:
        print("Incorrect PIN. Terminating program.")

# Run the ATM program
atm()








# Output: 1:  Check balance:
 
# 2: Withdraw money:
 
# 3: Exit:
 
# Lab Task 2:
#  Write a program that asks the user to enter a username and password.
# ⦁	The correct username should be "admin" and the correct password should be the numeric value 12345.
# ⦁	If both the username and password are correct, the program should display "Login Successful!".
# ⦁	If the username is incorrect, display "Incorrect username".
# ⦁	If the password is incorrect, display "Incorrect password".

# Code:
# Program to check username and password

# Set the correct username and password
correct_username = "admin"
correct_password = 12345

# Ask the user to enter the username and password
username = input(" \n Hello Comrade Enter User Name: ")
password = input(" Enter password: ")

# Check if both username and password are correct
if username == correct_username and password == str(correct_password):
   print(" congratulation Login Successful!")
# Check if the username is incorrect
elif username != correct_username:
   print("Incorrect username")
# Check if the password is incorrect
elif password != str(correct_password):
   print("Incorrect password")






# output:
# Login Successful!
 
# Incorrect username:
 
# Incorrect password: 
 
 
 
                            
                            # ***LAB 4***
            
            
 # Task 1
      # Program 1 : Even or Odd
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("The number is Even")
else:
    print("The number is Odd")


                   # Task 2

pin = 1234  
balance = 1000 

# Step 1:  PIN
user_pin = int(input("Enter your PIN: ")) 

# Step 2: PIN is correct
if user_pin == pin:
    print("\nPIN correct! Welcome to the ATM.")
    
    # Step 3: Display Menu
    while True:
        print("\nMenu:")
        print("1. Check Balance")
        print("2. Withdraw Money")
        print("3. Exit")
        
        # Step 4:  user choice
        choice = int(input("Choose an option (1-3): "))  
        
        if choice == 1:
            # Option 1: Check balance
            print(f"Your current balance is: ${balance}")
            
        elif choice == 2:
            # Option 2: Withdraw money
            withdraw_amount = int(input("Enter amount to withdraw: "))  

            if withdraw_amount <= balance:
                balance -= withdraw_amount
                print(f"${withdraw_amount} withdrawn. New balance: ${balance}")
            else:
                print("Insufficient funds.")
                
        elif choice == 3:
            # Option 3: Exit
            print("Thank you for using the ATM. Goodbye!")
            break
            
        else:
            print("Invalid option. Please try again.")
else:
    print("Incorrect PIN")

                # Task 3

   
    correct_username = "admin"
    correct_password = 12345
    
    # Get 
    username = input("Enter username: ")
    password = int(input("Enter password: "))
    
    # Check 
    if username == correct_username and password == correct_password:
        print("Login Successful!")
    elif username != correct_username:
        print("Incorrect username")
    elif password != correct_password:
        print("Incorrect password")



                          # ***LAB 5***

                          # Task : 1 


## Q No 1: Write a program that uses a loop to print numbers from 1 to 10?

print("Write a program that uses a loop to print numbers from 1 to 10:")
for i in range(1, 11):
    print("The Number is: ", i)
    
                             # Task : 2   
                             

## Q No 2: Write a function that calculates the sum of all numbers up to a given number using a loop

print("The Sum of the Numbers 1 to 10")
sum = 0
for i in range(1, 10):
    sum += i
print("The Sum of all Numbers:",sum)

                              # Task : 3
                              

## Q No 3: Write code using loops and nested loops to create star pattern

# Number of rows for the upper part
rows = 5

# Upper part 
for i in range(1, rows + 1):
    # Print spaces for alignment
    for j in range(rows - i):
        print(' ', end=' ')
    # Print stars
    for k in range(2 * i - 1):
        print('*', end=' ')
    print()

# Lower part
for i in range(rows - 1, 0, -1):
    # Print spaces for alignment
    for j in range(rows - i):
        print(' ', end=' ')
    # Print stars
    for k in range(2 * i - 1):
        print('*', end=' ')
    print()

                             # Task : 4
                             
        
## Q No 4: Write a function that takes a list of numbers and prints only the even numbers.

print("Those are Even Number The Range in 1 to 21")
for i in range(1, 21):
    if i % 2 == 0:
        print("The Only Even Numbers is: ", i)


                            # ***LAB 6***
                            
                          
                            # task # 1
                            
# Write a Python function that takes a number as input and returns the sum of its digits.
# take user input
num = int(input("Enter the number: "))

# define a function that take one input and add them
def checksum(a):
    sum = 0
    for i in range(1, a + 1):
        sum += i
    return f"the sum of its digits {sum}"


# checksum(num)
# # function call
result1 = checksum(num)
# your desire result
print(result1)

                            # task # 2
                            
# Write a Python function that takes a sentence as input and returns the number of words in it.

userInput = input("Enter the Sentence: ")


# print(userInput)
def CalSentenceLength(x):
    return len(x)


result2 = CalSentenceLength(userInput)
print(f"the length of the sentence is {result2}")

                            # task # 3
                            
# Write a Python function that takes an integer and returns whether the number is even or odd.


num1 = int(input("Enter the number: "))


def checkEvenOrOdd(x):
    if x % 2 == 0:
        return f"{x} is even Number"
    else:
        return f"{x} is odd Number"


result3 = checkEvenOrOdd(num1)
print(result3)  


                            #***LAB 7***
                            
                             #task 1
                             
# Write a Python function that draws a square using asterisks (*). The side length of the square should be provided by the user.

def draw_square(side_length):
 
    for _ in range(side_length):
        print('*' * side_length)
length = int(input("Enter the side length of the square: "))
draw_square(length)

                             #task 2
                             
#Write a Python function that takes a list of numbers as input and returns the sum of only the even numbers.


def sum_of_evens(numbers):
    """
    This function calculates the sum of even numbers in a list.

    :param numbers: List of integers
    :return: Sum of even integers in the list
    """
    even_sum = 0
    for num in numbers:
        if num % 2 == 0:  # Check if the number is even
            even_sum += num
    return even_sum

# Taking input from the user
numbers_list = list(map(int, input("Enter numbers separated by spaces: ").split()))

# Call the function and display the result
print("Sum of even numbers:", sum_of_evens(numbers_list))


                             #task 3

# Write a Python function that takes a number as input and counts down to zero, printing each number.

def countdown_to_zero(number):
   for i in range(number, -1, -1):
        print(i)
start_number = int(input("Enter a number to count down from: "))
countdown_to_zero(start_number)
                                                   
                             #***LAB 8***               
                             
                             #task 1
                             
#  Write a Python class named Car that represents a car. The class should have the following attributes:
# make: the car's make (e.g., "Toyota")
# model: the car's model (e.g., "Corolla")
# year: the car's manufacturing year (e.g., 2020)
# mileage: the number of miles driven by the car.
# The class should have the following methods:
# __init__(self): Constructor to initialize the car's attributes.
# display_info(): Displays the car's information (make, model, year, mileage).
# drive(miles): Increases the mileage by the specified number of miles        
                            
                            
class Car:
    def __init__(self, make, model, year, mileage=0):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage

    def display_info(self):
        print(f"Car Make: {self.make}")
        print(f"Car Model: {self.model}")
        print(f"Manufacturing Year: {self.year}")
        print(f"Mileage: {self.mileage} miles")

    def drive(self, miles):
        self.mileage += miles
        print(f"Driven {miles} miles. New mileage: {self.mileage} miles.")

my_car = Car("Toyota", "Corolla", 2020)
my_car.display_info()
my_car.drive(100)



#Task 2
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.marks = []

    def add_marks(self, marks):
        self.marks.extend(marks)

    def average_marks(self):
        if not self.marks:
            return 0
        return sum(self.marks) / len(self.marks)

    def display_info(self):
        avg_marks = self.average_marks()
        print(f"Student Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Average Marks: {avg_marks:.2f}")

student = Student("Alice", 20)
student.add_marks([85, 90, 78])
student.display_info()

             #Task 3
class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount}. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds for this withdrawal.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrew: ${amount}. New balance: ${self.balance:.2f}")

    def display_balance(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Current Balance: ${self.balance:.2f}")

account = BankAccount("John Doe", 1000)
account.display_balance()
account.deposit(500)
account.withdraw(200)
account.withdraw(1500)             