# value = 13
# remainder = value % 5

# if remainder:
#     print(f"Not divisible, remainder is {remainder}")

value = 13

if (remainder := value % 5):
    print(f"Not divisible, remainder is {remainder}")


available_sizes = ["small", "medium", "large"]

if (requested_size := input("Enter your size: ")) in available_sizes:
    print(f"Serving {requested_size} tea")
else:
    print(f"{requested_size} not availble")



flavors = ['masala', 'ginger', 'lemon', 'mint']

print("Avaialable flavors: ", flavors)

while (flavor := input("Choose your flavors: ")) not in flavors:
    print(f"Sorry {flavor} is not avaialble")
print(f"Your {flavor} tea is being prepared")