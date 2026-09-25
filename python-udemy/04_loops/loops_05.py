customer_names = ['Mary', 'Rose', 'Helen', 'Adam']
order_amount = [120, 175, 133, 204]

for customer, bill in list(zip(customer_names, order_amount)):
    print(f"{customer} paid {bill}") 
