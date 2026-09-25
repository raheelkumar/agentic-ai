order_amount = int(input("Enter the order amount: "))

delivery_fees = 0 if order_amount > 500 else 30

print(f"Total order amount is: {order_amount+delivery_fees} with {delivery_fees} as delivery fee")