# Basically nonlocal keyword to refer the one lvel outer version of variable and global keyword for gloabal version of variable

chai_type = "Plain"

def update_order():
    #chai_type = "ginger"
    global chai_type
    print("Update global chai type")
    chai_type = 'Milk'
    def kitchen():
        # chai_type = 'lemon'

        print("Update outer chai type")
        # nonlocal chai_type
        chai_type = 'Red'
        #print(f"Inner: {chai_type}")

    # print(f"Outer: {chai_type}")
    # kitchen()
    # print(f"Outer: {chai_type}")

print(f"Global: {chai_type}")
update_order()
print(f"Global: {chai_type}")