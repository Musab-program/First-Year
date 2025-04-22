while True :
    num = int(input("Enter the number of lines : "))
    i = num
    j = 0
    while i > 0:
        while j <= num:
            if j < i:
                print(" ",end="")
            else:
                print("* ", end="")
            j += 1
        j=1
        while j <= num:
            if j < i:
                print(" ",end=" ")
            else:
                print("* ", end="")
            j += 1
        j = 0
        i -= 1
        print()
    i = num-1
    j = num
    while i > 0:
        while j >= 0:
            if j < i:
                print("* ", end="")
            else:
                print(" ", end="")
            j -= 1
        j=num-1
        while j >= 0:
            if j < i:
                print("* ", end="")
            else:
                print("  ", end="")
            j -= 1
        j = num
        i -= 1
        print()



