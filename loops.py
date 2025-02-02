#Example for for loop

for i in range(5):
    print(i)

for i in range(1,5):
    print(i)

for i in range(1, 10, 2):
    print(i)
    

#Example for while loop

i = 0
while i < 5:
    print(i)
    i += 1

#Example for Loop Control: Break and Continue

for i in range(10):
    if i == 5:
        break
    print(i)


for i in range(10):
    if i == 2:
        continue
    print(i)


#Write a program that asks for two numbers. If the sum of the numbers is greater than 100, print "That is a big number" and terminate the program.

num1 = 100
num2 = 5

sum = num1 + num2

if sum > 100:
    print("The number is too big")
