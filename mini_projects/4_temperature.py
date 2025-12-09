device_status = "active"
temperature=int(input("enter a temperature"))

if device_status =="active":
    pass
    if temperature >35:
        print("Temperature is high")
    else:
     print("Normal temperature")
else:
    print("Device is offline")



