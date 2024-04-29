import random
RandomNumber = random.randrange(1,200)
# print(RandomNumber)

Userinput = int(input("Guess the number:"))


if Userinput > RandomNumber:
    print("The number is too high.")

elif RandomNumber> Userinput:
    # print(RandomNumber)
    print("The number is too low.")


else:
    print(RandomNumber)
    print("yes, you matched the number")