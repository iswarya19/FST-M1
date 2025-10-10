#numbers = [5,10,15,20,25,30]

numbers = input("Enter the number").split(",")
first_num = numbers[0]
last_num = numbers[5]

if (first_num == last_num):
    print ("same numbers")
else:
    print("not same")