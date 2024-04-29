# import random
#
# Dicerolling = True
# while Dicerolling:
#     print(random.randint(1,6))
#     Playagain = input("Do you want to Roll again [y/n]:")
#     if Playagain == "y":
#         continue
#     else:
#         print("Game over")
#         break

import random
Dicerolling = True

while Dicerolling:
    print(random.randint(1,6))
    Playagain = input("Do you want to play Roll again [y/n]:")
    if Playagain == "y":
        continue
    else:
        print("Game over")
        break










