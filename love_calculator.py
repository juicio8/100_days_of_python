
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()
true = 0
love = 0
for letter in "true":
    true += name1.count(letter)
    true += name2.count(letter)

for letter in "love":
    love += name1.count(letter)
    love += name2.count(letter)

total = int(str(true) + str(love))
if (total < 10) or (total > 90):
    print(f"Your score is {total}, you go like coke and mentos.")
elif (total >= 40) and (total <= 50):
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}")
