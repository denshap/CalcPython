while True:
    try:
        a = float(input("Enter a: "))
        b = float(input("Enter b: "))
    except ValueError:
        print("Incorrect number!")
        continue
    else:
        action = input("Enter operation: ")
        if action in ('+', '-', '*', '/'):
            if action =='+':
                print("{:.2f}".format(a+b))
            elif action =='-':
                print("{:.2f}".format(a-b))
            elif action =='*':
                print("{:.2f}".format(a*b))
            elif action =='/':
                if b ==0:
                    print("Invalid action!")
                else:
                    print("{:.2f}".format(a/b))
            else:
                print("Incorrect symbol!")