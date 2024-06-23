menu={
       "coffie": 80,
       "tea": 50,
       "pastta":100,
       "pizza": 150,
       "burger": 120,
}
print("Welcome to our cafe")
print("Here is our menu:")
print(" coffie : Rs 80\n tea : Rs 50 \n pastta : Rs 10\n pizza : Rs 150\n burger : Rs 120")
ordertotal=0
item_1=input("enter item you want to order =")
if item_1 in menu:
    ordertotal +=menu[item_1]
    print(f"your order {item_1} has been added to your order")
else:
    print("sorry we dont have this item in our menu")
otherorder=input("do you want to add another item ? (yes/no)") 
if otherorder=="yes":
    item_2=input("enter item you want to order =")
    if item_2 in menu:
        ordertotal +=menu[item_2]
        print(f"your order {item_2} has been added to your order")
    else:
        print("sorry we dont have this item in our menu")
print("total amount of order to pay is", {ordertotal})



