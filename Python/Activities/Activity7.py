#number = [1,2,3,4,5]
number = input("Enter the number").split(",")
sum = 0
for i in number:
    sum = sum + int (i)
    print(sum)
