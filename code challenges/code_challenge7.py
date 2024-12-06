#grocery


print("\nGROCERIES APP")
name = input("\nPLease input your name: ")
isGrocery = input("Did you buy a grocery? (yes / no): ")
if isGrocery.lower() == "yes":
      itemname = input("Please input the item name: ")
      price = int(input("Please input the price of the item: "))
      amount = int(input("Please input your money: "))
      age = eval(input("Please input your age: "))
      if age <=59:
            tax = price * 0.123                    
            total = tax + price
            change = amount - total           
            print(f"\nHi {name}, you purchased {itemname}, with a price of {price} plus 12.3% tax ({tax}) total of ({total})\nAmount given: {amount}\nChange:{round(change,2)}")
      else:
            taxs = price * 0.123
            totals = price + taxs
            discount = totals * 0.052
            overall = totals - discount
            changes = amount - overall
            print(f"\nHi {name}, you purchased {itemname}, with a price of {price} plus 12.3% tax ({taxs}) total of ({totals}) with senior citizen discount of 5.2% ({discount}) with the overall total ({overall})\nAmount given: {amount}\nChange:{round(changes,2)}")    
else:
      print("Thank you, you may now close this app.")

      



