number = int(input("Enter the number"))

if  number != 0 and number % 2 == 0:
    print(f"{number} is even")
elif number != 0 and number % 3 == 0:
    print (f"{number} is odd")
else:
    print(f"{number} is neither even nor odd")
    