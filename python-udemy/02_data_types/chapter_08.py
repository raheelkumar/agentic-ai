ingredients = ["Water", "Milk", "tea leaves"]

ingredients.append("Sugar")
print(f"Tea Ingredients are: {ingredients}")
ingredients.remove("Sugar")
print(f"Tea Ingredients are: {ingredients}")

spice_options = ["ginger", "cardamom"]
chai_ingredients = ["water", "milk"]
print(f"Chai Ingredients: {chai_ingredients}")
chai_ingredients.extend(spice_options)
print(f"Masala Chai Ingredients: {chai_ingredients}")

chai_ingredients.insert(2, "tea leaves")
print(f"Chai Ingredients: {chai_ingredients}")

last_added = chai_ingredients.pop()

print(f"Last item: {last_added}")
print(f"Chai Ingredients: {chai_ingredients}")
chai_ingredients.reverse()
print(f"Reverse Chai Ingredients: {chai_ingredients}")

chai_ingredients.sort()
print(f"Sorted Chai Ingredients: {chai_ingredients}")

sugar_level = [1,2,3,4,5]
print(f"Highest sugar level: {max(sugar_level)}")
print(f"Lowest sugar level: {min(sugar_level)}")

# Operator overloading
base_liquid = ["water", "milk"]
extra_flavor = ["ginger"]

masala_liquid = base_liquid + extra_flavor

print(f"Masala Liquid: {masala_liquid}")

strong_brew = ["black tea"] * 3
print(f"Strong brew: {strong_brew}")

strong_brew = ["black tea", "Water"] * 3
print(f"Strong brew: {strong_brew}")

raw_spice_data = bytearray(b"CINNAMON")
print(f"Raw Spices: {raw_spice_data}")
raw_spice_data = raw_spice_data.replace(b"CINNA", b"CARD")
print(f"Raw Spices: {raw_spice_data}")