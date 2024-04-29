answer = input("do you want to play this game?[Yes/No]")
if answer == "Yes":
    print("Welcome to the game!")
    answer = input("do you want to go jungle or cave?[jungle/cave]:")
    if answer == "jungle":
        print("you see the hungry tiger😣.The tiger will eat you. Game close.")
    elif answer == "cave":
        print("you seen the bear in front of cave.")
        answer = input("Do you want to fight with the bear or run away![fight/run]:")
        if answer == "fight":
            print("Bear is too much strong! you lose the game!")
        else:
            print("wow!still you are alive.")
            print("you won the game😀")


else:
    print("The game closed.")