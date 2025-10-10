list_one = [1,2,3,4,5]
list_two = [7,8,9,10,6]

list_odd = []
list_even = []

for num in list_one:
    if( num % 2 == 0):
        list_even.append(num)
        print(f"Even numbers{list_even}")

for num in list_two:
    if( num % 3 == 0):
        list_odd.append(num)
        print(f"Odd numbers{list_odd}")

