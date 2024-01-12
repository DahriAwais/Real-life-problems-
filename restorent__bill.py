def restau_bill(ordered_items, price, discounts, tax, sp):
    total = ordered_items * price
    discount = total * (discounts / 100) if discounts > 0 else 0
    total_after_discount = total - discount
    total_after_tax = total_after_discount + (total_after_discount * (tax / 100)) if tax > 0 else total_after_discount
    per_person_cost = total_after_tax / sp if sp > 0 else total_after_tax

    print(f'Total price is: {total}')
    print(f'Discount: {discount}')
    print(f'Total after discount: {total_after_discount}')
    print(f'Total after Tax: {total_after_tax}')
    print(f'Each person can split into: {per_person_cost}')


ordered_items = int(input("Enter how many orders you made: "))
price = int(input("Enter price per item: "))
discounts = int(input("Enter discount percentage or 0 for no discount: "))
tax = int(input("Enter sales tax percentage or 0 for no tax: "))
sp = int(input("Enter number of people to split the bill or 0 for no splitting: "))

restau_bill(ordered_items, price, discounts, tax, sp)


    
    