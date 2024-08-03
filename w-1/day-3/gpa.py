while True:
    a = int(input("Enter your marks: "))
    if a <= 100 and a >= 80:
        print("A+")
    elif a < 80 and a >= 70:
        print("A")
    elif a < 70 and a >= 65:
        print("A-")
    elif a < 65 and a >= 60:
        print("B+")
    elif a < 60 and a >= 55:
        print("B")
    elif a < 55 and a >= 50:
        print("B-")
    elif a < 50 and a >= 45:
        print("C")
    elif a < 45 and a >= 40:
        print("D")
    elif a < 40 and a >= 33:
        print("E")
    elif a > 100:
        print("Not available number, try again")
    else:
        print("F")
