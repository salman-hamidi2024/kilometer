work = input("what do you want: ")
kilometer = int(input("how many kilometer: "))
meter = kilometer * 100
centimeter = meter * 100
if work == "meter":
    print(meter)
elif work == "centimeter":
    print(centimeter)