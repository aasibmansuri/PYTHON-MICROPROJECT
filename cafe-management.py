menu_dict = {
    'pizza': 300,
    'burger': 75,
    'coke': 45,
    'cold coffee': 50,
    'tea': 25
}

ch_dict = {
    1: "Display Menu",
    2: "Place Order",
    3: "Bill",
    4: "Exit"
}
print("*WELL COME TO CAFE SHREENIVAS*")
order={}
def display_choice():
    print("")
    for key, value in ch_dict.items():
        print(f"\t\t{key}:{value}")
    print("")    

def display_menu():
    print("\nMenu:")

    for item, price in menu_dict.items():
        print(f"{item}: {price}")
   

def place_order():
    item = input("Please enter item: ").lower()
    if item in menu_dict:
        quantity = int(input("Enter quantity: "))
        order[item]=quantity
        print(f"Your order is {item} in quantity {quantity}")
    else:
        print("Item not found.")

def bill(menu_dict,):
    print("your order")
    total=0
    tip=0 
    print("*your bill")
    print("item\t\tprice\t\ttotal")
    for item,quantity in order.items():
         price=menu_dict[item]
         subtotal=price*quantity
         total+=tip
         total+=subtotal
         print(f"{item}\t\t{quantity}\t\t{subtotal}")
    print(f"Your Total Bill =: ${total}")
    print("you want give a tip?")
    choice=input("enter yes or not")
    if choice=="yes":
        tip=int(input("how many rupees you want give a tip"))
        print("thank you sir for",tip,"tip")
        total+=tip
        print(f"Your Total Bill =: ${total}")
    else:
        print("visit again")   
        print(f"Your Total Bill =: ${total}")
    

def compare(choice):
    if choice == 1:
        display_menu()
    elif choice == 2:
        place_order()
    elif choice == 3:
        bill(menu_dict)
    elif choice == 4:
        print("Thank you for visiting Cafe Shreenivas!")
        exit()
    else:
        print("Invalid choice. Please try again.")

def main():
    while True:
        display_choice()
        choice = int(input("Enter your choice: "))
        compare(choice)

if _name_ == "_main_":
    main()