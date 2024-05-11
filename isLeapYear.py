# python algorithm

# Is the year a leap year

def leapYear():
    repeat = True
    while repeat == True:
        yearInput = int(input("Input a year to see if it is a leap year: "))
        if yearInput %4 == 0:
            if yearInput %100 == 0 and yearInput %400 == 0:
                print("Is a leap year")
            elif yearInput %100 == 0 and yearInput %400 != 0:
                print("Is not a leap year")
            else:
                print("Is a leap year")  
        else:
            print("Is not a leap year")
        # conditions for repeating
        print()
        anotherYear = input("Would you like to enter another year? (Y/N):")
        if anotherYear.upper() == "Y":
            repeat = True
        else:
            repeat = False
        print()
    
leapYear()