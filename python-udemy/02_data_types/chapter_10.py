chai_order = dict(type="Masala Chai", size="Large", sugar=2)

print(f"Chai Order: {chai_order}")

chai_recepie = {}
chai_recepie["base"] = "balck tea"
chai_recepie["liquid"] = "milk"

print(f"Recipie base: {chai_recepie['base']}")
print(f"Recipie: {chai_recepie}")
del chai_recepie['liquid']
print(f"Recipie: {chai_recepie}")

print(f"Is there sugar in the order? {'sugar' in chai_order}")

chai_order = {"type":"Ginger Chai", "size":"Medium", "sugar":1}

print(f"Order details (Keys): {chai_order.keys()}")
print(f"Order details (Values): {chai_order.values()}")
print(f"Order details (Items): {chai_order.items()}")

customer_note = chai_order.get("customer_note", "No Note")

print(f"Customer note is: {customer_note}")