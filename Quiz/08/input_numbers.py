summation = 0
while True:
    try:
        try:
            number = float(input("Enter a number: "))
        except ValueError:
            print("Your input is not int or float.")
            continue
        else:
            summation += number
            continue            
    except KeyboardInterrupt:
        print("the summation of numbers is: ", summation)
        break