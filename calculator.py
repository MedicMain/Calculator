import math


    
while True:

    print("Choose one of the following options...")
    print("divisible by, square roots, or squared numbers.\n")
    z = input("Type Here: ")


    if z == "divisible by":
        a = int(input("Numbers divisible by: "))
        print("Provide the ranges of numbers.")
        c = int(input("Number no less than: "))
        b = int(input("Number no greater than: "))

        for i in range(c, b + a):
            if i % a == 0:
                print(i)
                
        print("")
        aaa = input("Would you like to run the program again? ")
        if aaa == "yes":
            print("")
            continue
        else:
            print("Thank you for using our calculator!")
            break
        
    elif z == "square roots":
        y = int(input("What number would you like to find the square root of? "))
        x = math.sqrt(y)
        print(x)
        print("")
        aaa = input("Would you like to run the program again? ")
        if aaa == "yes":
            print("")
            continue
        else:
            print("Thank you for using our calculator!")
            break
            
    elif z == "squared numbers":
        w = int(input("What number would you like to be squared? "))
        o = w * w
        print(o, "\n")
        
        aaa = input("Would you like to run the program again? ")
        if aaa == "yes":
            print("")
            continue
        else:
            print("Thank you for using our calculator!")
            break

    else:
        print("")
        continue
