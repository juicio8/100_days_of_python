def isPrime(number):
    prime = True
    if not number <= 2:
        for n in range(2, number):
            if number % n == 0:
                prime = False
                break
    if prime:
        print("It's a prime number")
    else:
        print("It's not a prime number")


n = int(input("Check this number: "))

isPrime(number=n)
