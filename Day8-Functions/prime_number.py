n = int(input("Enter the number: "))

def prime(number):
    f = 0
    for i in range(1, number):
        if number%i == 0:
            f += 1
    if f==1:
        print("Prime")
    else:
        print("Not prime.")

prime(number=n)
        