import random
import urllib.request

class Pixal:

    def welcome():
        print("Hello world")
        
    def farewell():
        print("Goodbye cruel world!")

    def countdown():
        count = ["three", "two", "one"]
        for i in count:
            Pixal.welcome()
        else:
            Pixal.farewell()
                                
    def wheelOfFortune():
        #Open the movie list and pick a random movie (line)
        file=open('movies.csv','r',encoding='utf8')
        movies=file.read().splitlines()
        file2=open('books.csv','r')
        books=file2.read().splitlines()
        file3=open('countries.csv', 'r')
        countries=file3.read().splitlines()
        vowel=['a', 'e', 'i', 'o', 'u']
        playerScores={}
        rounds=[movies, books, countries]
        stage=['movies', 'books', 'countries']
        #Greet the appropriate number of players and register their names
        wheel=['Bankrupt', 750, 800, 300, 200, 1000, 500, 400, 300, 200, 500, 700, 200, 500, 450, 'Lose A Turn', 200, 400, 250, 150, 400, 900, 250, 350]
        playerCount = input("\nWelcome to Wheel of Fortune! Please select the number of players (1-3): ")
        if playerCount == '1':
            player1=input("\nOkay Player One please introduce yourself: ")
            players=[player1]
        elif playerCount == '2':
            player1=input("\nOkay Player One please introduce yourself: ")
            player2=input("\nAnd welcome as well, Player number Two: ")
            players=[player1, player2]
        elif playerCount == '3':
            player1=input("\nOkay Player One please introduce yourself: ")
            player2=input("\nAnd welcome as well, Player number Two: ")
            player3=input("\nLast but not least, say hello to Player Three: ")
            players=[player1, player2, player3]
        else:
            playerCount=input("\nUh-oh, didn't catch that - please try again!: ")
        #Set cash totals to zero for each player
        for name in players:
            playerScores[name] = 0
        for value in rounds:
            grid=[]
            guesses=[]
            answer=random.choice(value).lower()
            for i in answer:
                if i.isalpha() != True:
                    grid.append(i)
                else:
                    grid.append("_")
            round=True
            multiplier=0
            print("\nLet's see the grid for today's '%s' round:\n" % stage[rounds.index(value)])
            #print(answer)
            print(*grid)
            while round == True:
                print("\n%s - it's now your turn on the wheel!" % name)
                for name in players:
                    if playerScores[name] > 249:
                        action=input("\nDo you want to 'guess' a consonant, 'buy' a vowel or attempt to 'solve'?:")
                    else:
                        action=input("\nDo you want to 'guess' a consonant or attempt to 'solve'?:")
                    if action == "guess":
                        print("\nThen let's go ahead and spin the wheel for %s!" % name)
                        spin=random.choice(wheel)
                        if spin == "Bankrupt":
                            print("\nOoh sorry %s, looks like you're bankrupt" % name)
                            playerScores[name]=0
                        elif spin == "Lose A Turn":
                            print("\nSorry %s, you'll be skipping this turn" % name)
                        else:
                            print("You've spun $%s - nice job, you'll get this per letter" % spin)
                            print("\nJust a reminder, the letters we've had so far are:", *sorted(guesses))
                            print("And here's how the grid is shaping up\n")
                            print(*grid)
                            guess=input("\nOkay player, which consonant do you want to try?:")
                        if guess in answer and guess not in guesses and guess not in vowel and len(guess) is 1 and guess.isalpha() == True:
                            guesses.append(guess)
                            for i in answer:
                                    if (i == guess):
                                        indices = [i for i, x in enumerate(answer) if x == guess]
                                        playerScores[name] += spin
                                        for i in indices:
                                            grid[i]=guess
                            print(*grid)
                            print("\nGood guess %s, you're now on a total of $" % name, playerScores[name])
                        #If the letter guessed is not in the word
                        elif len(guess) != 1 or guess.isalpha() == False:
                            print("\nSingle letter guesses only, please! Moving on!")
                        elif guess in guesses:
                            print("\nPay attention %s, we've already had that letter! Next player!" % name)
                        elif guess in vowel:
                            print("\nSorry %s if you want vowels, you'll have to pay for them!" % name)
                        else:
                            print("\nOh tough break %s, let's move on to the next player" % name)
                            if guess not in guesses:
                                guesses.append(guess)
                    elif action == "buy":
                        toBuy=input("\nSo for $250, which vowel would you like to buy?:")
                        playerScores[name] -= 250
                        if toBuy in answer and toBuy not in guesses and toBuy in vowel:
                            guesses.append(toBuy)
                            for i in answer:
                                if (i == toBuy):
                                    indices = [i for i, x in enumerate(answer) if x == toBuy]
                                    for i in indices:
                                        grid[i]=toBuy
                            print(*grid)
                            print("\nGood pick %s, that might make things easier" % name)
                        else:
                            guesses.append(toBuy)
                            print("\nToo bad %s - no %s in this title! On to the next player" % (name, toBuy))
                    elif action == "solve":
                        solve=input("\nGood luck %s, please enter the answer in the format shown by the grid - all lowercase:" % name)
                        if solve == answer:
                            for i in grid:
                                if i == "_" :
                                    multiplier+=1
                            bonus=multiplier*100
                            print("\nNice job, %s you got it spot on! The answer was of course %s\nYou got yourself a bonus $%d" % (name, answer, bonus))
                            playerScores[name] += bonus
                            winner=max(playerScores, key=playerScores.get)
                            totals=sorted(playerScores.values())
                            highest=totals.pop(-1)
                            print("\nAnd the winner for the %s round with a score of $%d is %s! Great job!" % (stage[rounds.index(value)], highest, winner))
                            guess=""
                            round=False
                        else:
                            print("\nOh, tough luck player - that's not quite right! Moving on...")

        winner=max(playerScores, key=playerScores.get)
        totals=sorted(playerScores.values())
        highest=totals.pop(-1)
        print("\nAnd today's winner with a grand total of $%d is %s! Congratulations, we hope to see you all again!" % (highest, winner))
                    
Pixal.wheelOfFortune()
