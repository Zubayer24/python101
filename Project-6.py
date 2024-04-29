word = "Hablu"
chances = 5
Guessadd = []
done = False

while not done:
    for letter in word:
        if letter.lower() in Guessadd:
            print(letter,end= " ")
        else:
            print("_", end= "")

    Myguess = input(f"Your chances is {chances},Guess the letter:")
    Guessadd.append(Myguess.lower())
    if Myguess.lower() not in word.lower():
        chances -= 1
        if chances == 0:
            break

    done = True
    for letter in word:
        if letter.lower() not in Guessadd:
            done = False

if done:
    print(f"yes, you have won the game , the word is {word}")
else:
    print("you lose the game!!") 




