#numbers = (10,22,35,42,50)

numbers = input("Eneter numbers").split(",")
for i in numbers:

    num = int(i)
    if(num % 5 == 0):
        print(f"Divisble numbers by 5 {num}")