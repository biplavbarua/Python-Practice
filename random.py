#random_number
import random
n1 = random.randint(1,9)
n2 = random.randint(1,9)
ans = eval(input("What is " + str(n1) + " + " + str(n2) + "? "))
print("Your ans is ", n1+n2 == ans)
