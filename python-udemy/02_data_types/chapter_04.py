is_boiling = True
stir_count = 5
total_actions = stir_count + is_boiling # upcasting: casting one type into another whenever compatible
print(f"total actions {total_actions}")

milk_present = 0 # no milk
print(f"Is there milk: {bool(milk_present)}")

milk_present = 1 # yes milk
print(f"Is there milk: {bool(milk_present)}")

water_hot = True
tea_added = False
can_serve_chai = water_hot and tea_added
print(f"Is chai ready: {can_serve_chai}")