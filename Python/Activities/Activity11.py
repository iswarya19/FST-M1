fruitShop = {

    "apple": 25,
    "orange": 50,
    "watermelon": 25,
    "Mango": 60

}

fruitName = input("Enter the fruit name").lower()

if(fruitName in fruitShop):
   
    print("Yes Available")
else:
    print("No not Availabe")


