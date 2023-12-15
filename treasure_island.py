treasure = '''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
'''
print(treasure)
print("Welcome to Treasure Island")
print("Your mission is to find the treasure")
choice1 = input("Do you want to go left(l) or right(r)?\n").lower()
game_over = ''' 
***********************************************
****************  GAME OVER   *****************
***********************************************
'''

if choice1 == 'l':
    print("You went left")
    print("Nice Choice")
    choice2 = input("Do you want to swim(s) or wait(w)?\n").lower()
    if choice2 == 'w':
        print("Waiting...")
        print("Doors arrive")
        choice3 = input(
            "What door are you picking red door(r), blue door(b), or yellow door(y)?\n").lower()
        if choice3 == 'r':
            print("Entered the red door")
            print("You were consumed by fire")
            print(game_over)
        elif choice3 == 'b':
            print("Entered the blue door")
            print("Wild beasts arriving...")
            print("You were attacked by wild beast")
            print(game_over)
        elif choice3 == 'y':
            print("Entered the yellow door")
            print("Treasure found")
            print(treasure)
            print("YOU WIN!!!")
        else:
            print("Jumped into the river")
            print(game_over)
    else:
        print("You were attacked by a trout, you died")
        print(game_over)
else:
    print("You fell into a hole")
    print(game_over)
