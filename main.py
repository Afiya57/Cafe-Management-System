#Define the menu of restuarant
menu = {
  'Pizza' : 750,
  'Pasta' : 600,
  'Fries' : 200,
  'Burger' : 300,
  'Coffee' : 350,
  'Sandwich' : 200,
  'Salad' : 300,
}

# print(menu)
print("Welcome to the Necto Cafe!")
print("\nHere is our menu: ")
print("Pizza: Rs750\nPasta: Rs600\nFries: Rs200\nBurger: Rs300\nCoffee: Rs350\nSandwich: Rs200\nSalad: Rs300 ")

order_total = 0
item_1 = input("\nWhat would you like to order? ")

if item_1 in menu:
  order_total += menu[item_1]  # 0+750 = 750
  print(f"{item_1} has been added to your order. ")

else:
  print(f"Sorry, {item_1} is not availabe yet!")
    
another_item = input("\nWould you like to order anything else? (Yes/No): ")
if another_item == "Yes":
  item_2 = input("What would you like to order? ")
  if item_2 in menu:
    order_total += menu[item_2]
    print(f"{item_2} has been added to your order.")
  else:
    print(f"Sorry, {item_2} is not availabe yet!")

print(f"\nThe total amount of items to pay is Rs{order_total}")
print("\nThank you for ordering from Necto Cafe! ")