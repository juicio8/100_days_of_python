import random

names = input("Give me everybody's name seperated by a comma(,): ")
print(names)
names = names.split(', ')
print(names)
key = random.randint(0, len(names) - 1)
print(f"{names[key]} is going to pay the bills today")
