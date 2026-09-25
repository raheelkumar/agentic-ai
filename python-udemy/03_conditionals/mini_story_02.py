snack_order = input("Select a snack for the order: ").casefold()

if snack_order == "cokies" or snack_order == "samosa":
    print(f"Order for {snack_order} confirmed!")
else:
    print(f"{snack_order} item is not available")