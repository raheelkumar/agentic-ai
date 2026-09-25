skip_flavor = ['green', 'cardamom']

break_flavor = ['red', 'honey']

while True:
    order_tea_flavor = input("Enter order tea flavor: ").casefold()

    if order_tea_flavor in skip_flavor:
        continue
    elif order_tea_flavor in break_flavor:
        break
    else:
        print(f"Ordered tea of flavor {order_tea_flavor}")