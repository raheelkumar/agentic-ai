from fractions import Fraction
from decimal import Decimal

ideal_temp = 95.5
current_temp = 95.49999999999

print(f"Ideal temp: {ideal_temp}")
print(f"Current temp: {current_temp}")
print(f"Diff temp: {ideal_temp - current_temp}")

current_temp = 95.49
print(f"Diff temp: {ideal_temp - current_temp}")