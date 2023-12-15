####################
#### Pizza Order ###
####################
print("Welcome to Pizza Deliveries")
price = 0
size = input("What size of Pizza do you want? enter(S, M , L) ")
peperroni = input("Do you want peperroni? enter(Y for yes, N for no) ")
extra_cheese = input("Do you want extra cheese? enter(Y for yes, N for no) ")
if size == "S":
    price += 15
    if peperroni == "Y":
        price += 2
elif size == "M":
    price += 20
    if peperroni == "Y":
        price += 3
elif size == "L":
    price += 25
    if peperroni == "Y":
        price += 3
if extra_cheese == "Y":
    price += 1

print(f"Your final bill is ${price}")
