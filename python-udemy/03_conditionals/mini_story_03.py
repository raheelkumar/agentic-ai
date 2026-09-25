cup_size = input("Enter cup size for the tea: ").casefold()

if cup_size == 'small':
    price = 10
    print(f"Your bill is for: {price}")
elif cup_size == 'medium':
    price = 15
    print(f"Your bill is for: {price}")
elif cup_size == "large":
    price = 20
    print(f"Your bill is for: {price}")
else:
    print("Invalid Cup Size")