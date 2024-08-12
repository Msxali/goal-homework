age = int(input("whats your age"))

if age <= 17:
    print ("u cant have divers licence")
elif age >= 18:
    experience = int(input("input ages of your experience"))
    if experience > 1:
        print ("u can have diver licens")
    else:
        print ("u cant have divers licens")
        