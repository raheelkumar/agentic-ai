device_status = input("Enter device status: ").casefold()
temprature = int(input("Enter temprature: "))

if device_status == 'active':
    if temprature > 35:
        print("High Temprature alert")
    else:
        print("Temprature Normal")
else:
    print("Device is offline")
