op = "="
while op == "=" :
    print(" ______________________")
    print("|  7  |  8  |  9  |  + |")
    print("|----------------------|")
    print("|  4  |  5  |  6  |  - |")
    print("|----------------------|")
    print("|  1  |  2  |  3  |  * |")
    print("|----------------------|")
    print("|  +/-  |  0  | . |  / |")
    print("|----------------------|")
    print("|  C  |       =        |")
    print("|______________________|\n\n")
    num1 = float(input("Enter a number : "))
    op = input("Enter an operation : ")
    if op != "=" :

        # -------------------------------------------------
        while op != "=":
            if op == "+":
                num2 = float(input("Enter a number : "))
                total = num1 + num2
                while op != "=":
                    op = input("Enter an operation : ")
                    if op == "+":
                        num2 = float(input("Enter a number : "))
                        total = total + num2
                    elif op == "-":
                        num2 = float(input("Enter a number : "))
                        total = total - num2
                    elif op == "*":
                        num2 = float(input("Enter a number : "))
                        total = total * num2
                    elif op == "/":
                        num2 = float(input("Enter a number : "))
                        total = total / num2
                    elif op == "=":
                        break
                    else:
                        print("Erorr")

            # ---------------------------------------------------
            elif op == "-":
                num2 = float(input("Enter a number : "))
                total = num1 - num2
                while op != "=":
                    op = input("Enter an operation : ")
                    if op == "+":
                        num2 = float(input("Enter a number : "))
                        total = total + num2
                    elif op == "-":
                        num2 = float(input("Enter a number : "))
                        total = total - num2
                    elif op == "*":
                        num2 = float(input("Enter a number : "))
                        total = total * num2
                    elif op == "/":
                        num2 = float(input("Enter a number : "))
                        total = total / num2
                    elif op == "=":
                        break
                    else:
                        print("Erorr")
            # ---------------------------------------------------
            elif op == "*":
                num2 = float(input("Enter a number : "))
                total = num1 * num2
                while op != "=":
                    op = input("Enter an operation : ")
                    if op == "+":
                        num2 = float(input("Enter a number : "))
                        total = total + num2
                    elif op == "-":
                        num2 = float(input("Enter a number : "))
                        total = total - num2
                    elif op == "*":
                        num2 = float(input("Enter a number : "))
                        total = total * num2
                    elif op == "/":
                        num2 = float(input("Enter a number : "))
                        total = total / num2
                    elif op == "=":
                        break
                    else:
                        print("Erorr")
            # ---------------------------------------------------
            elif op == "/":
                num2 = float(input("Enter a number : "))
                total = num1 / num2
                while op != "=":
                    op = input("Enter an operation : ")
                    if op == "+":
                        num2 = float(input("Enter a number : "))
                        total = total + num2
                    elif op == "-":
                        num2 = float(input("Enter a number : "))
                        total = total - num2
                    elif op == "*":
                        num2 = float(input("Enter a number : "))
                        total = total * num2
                    elif op == "/":
                        num2 = float(input("Enter a number : "))
                        total = total / num2
                    elif op == "=":
                        break
                    else:
                        print("Erorr")
        print(total, "\n\n")
            # ---------------------------------------------------
    elif op == "=" :
        print (num1,"\n\n")
    else :
        print ("Erorr\n\n")
    print ("Do you want to calculate again ? ")
    print ("         Yes     No      ")
    choice =input ()
    if choice == "Yes" or choice == "yes" :
        print ()
    elif choice == "No" or choice == "no" :
        break
    else :
        print ("Erorr")

