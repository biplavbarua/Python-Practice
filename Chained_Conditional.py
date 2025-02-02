#Chained conditional with user input

number = int(input("Enter a number: "))

if number > 20:
    print("The number is greater than 20.")
elif number > 10:
    print("The number is greater than 10 but less than or equal to 20.")
else:
    print("The number is 10 or less.")

#Check the divisibility test of 6:

if number % 2 == 0:
    print("The number is divisible by 2.")
elif number % 3 == 0:
    print("The number is divisible by 3.")
elif number % 6 == 0:
    print("The number is also divisible by 6.")
else:
    print("The number is not divisible with 2, 3 or 6.")
