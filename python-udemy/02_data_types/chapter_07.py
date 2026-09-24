masala_spices = ("cardamom", "cloves", "cinnamon")

(spice1, spice2, spice3) = masala_spices

print(f"Spice1: {spice1}\nSpice2: {spice2}\nSpice3: {spice3}")

ginger_ratio, cardamom_ratio = 2, 1
print(f"Ratio is: G: {ginger_ratio} and C: {cardamom_ratio}")

# Swap values in python
ginger_ratio, cardamom_ratio = cardamom_ratio, ginger_ratio
print(f"Ratio is: G: {ginger_ratio} and C: {cardamom_ratio}")


# Membership

print(f"Is ginger in masala spices? {'ginger' in masala_spices}")
print(f"Is ginger in cinnamon spices? {'cinnamon' in masala_spices}")
print(f"Is ginger in Cinnamon spices? {'Cinnamon' in masala_spices}") # Case sensetive