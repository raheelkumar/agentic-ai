chai_type = "Ginger Chai"
customer_name = "Priya"

print(f"Order for {customer_name} : {chai_type} please!")

chai_description = "Aromatic and Bold"

first_word_of_description = chai_description[:8]
last_word_of_description = chai_description[-4:]

print(f"First word: {first_word_of_description}")
print(f"Last word: {last_word_of_description}")

# Reverse a string
print(f"Reverse description: {chai_description[::-1]}")
print()
label_text = "Chai Spécial"
print(f"Non Encoded label: {label_text}")
encoded_text = label_text.encode("utf-8")
print(f"Encoded label: {encoded_text}")
decoded_text = encoded_text.decode("utf-8")
print(f"Decoded text: {decoded_text}")