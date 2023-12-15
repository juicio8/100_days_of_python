year = int(input("Which year do you want to check? "))
notLeapYear = "Leap year."
leapYear = "Not leap year."

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(leapYear)
        else:
            print(notLeapYear)
    else:
        print(leapYear)

else:
    print(notLeapYear)
