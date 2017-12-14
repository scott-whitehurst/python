import random
import urllib.request

class hangman:

    def hangman():
        #Pre-game variables
        game = True
        lives = 8
        names = ["kai", "jay", "cole", "zane", "lloyd", "nya", "misako", "garmadon"]
        #generateWords.chosen = random.choice(names)
        #Retrieve a random word - from an online repo - converting from bytes to string
        #Take the randomly selected word, break down into a list
        #Additionally create a list of blank characters to show the length of the word
        word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
        response = urllib.request.urlopen(word_site)
        txt = response.read()
        WORDS = txt.splitlines()
        chosen=(random.choice(WORDS)).decode("utf-8").lower()
        #Creates list to contain word characters, "skeleton", letters guessed, hangman graphic
        list=[]
        skeleton=[]
        guesses=[]
        hanged=[]
        difficulty = input("\nWelcome, please select a difficulty - easy, medium, hard: ")
        #print(chosen)
        #Difficulties determine characters in word - if mismatch, re-rolls
        if difficulty == "easy":
            while len(chosen) > 4:
                chosen=(random.choice(WORDS)).decode("utf-8").lower()
        elif difficulty == "medium":
            while len(chosen) < 5 or len(chosen) > 8:
                chosen=(random.choice(WORDS)).decode("utf-8").lower()
        elif difficulty == "hard":
            while len(chosen) < 8:
                chosen=(random.choice(WORDS)).decode("utf-8").lower()
        else:
            print("Oh dear, I don't recognise that difficulty - please try again...")
        #Creates the blank character string (aka Skeleton) populating based on word
        for i in chosen:
            list.append(i)
            if i.isalpha() != True:
                skeleton.append(i)
            else:
                skeleton.append('_')
        print(skeleton)
        hanged.extend([' ', ' ___\n|   |\n|   O\n|  -|-\n|', ' ___\n|   |\n|   O\n|  -|\n|', ' ___\n|   |\n|   O\n|   |\n|', ' ___\n|   |\n|   O\n|\n|', ' ___\n|   |\n|\n|\n|', ' ___\n|\n|\n|\n|', '\n|\n|\n|\n|'])
        #Active state of game
        while game == True:
            print("\nSo far you have guessed:", *guesses)
            guess = input("\n\nPlease guess a letter: ")
            if guess.isalpha() != True or len(guess) != 1:
                print("\nInvalid input! Please guess a single letter only!\n%s" % skeleton)
            else:
                if guess in guesses:
                    print("You already said that! Try another letter...\n%s" % skeleton)
                else:
                    guesses.append(guess)
                    if guess in chosen:
                        print(guess, "appears in the word")
                        #print(list.count(guess))
                        #Iterate through the random word, checked for the guessed letter
                        #Replace blanks in the 'skeleton' with the corresponding letter
                        for i in list:
                                if (i == guess):
                                    indices = [i for i, x in enumerate(list) if x == guess]
                                    #print(indices)
                                    for i in indices:
                                        skeleton[i]=guess
                        print(skeleton)
                    #If the letter guessed is not in the word
                    else:
                        lives -= 1
                        print(guess, "does not appear in the word! You have lost a life")
                        print(lives, "lives remaining")
                        print(skeleton)
                        print(hanged.pop(lives))
                #End the game when no blank spaces remain
            if "_" not in skeleton:
                if lives == 1:
                    print("Correct - the word was '%s' - you won with just 1 life remaining!" % chosen)
                else:
                    print("Correct - the word was '%s' - you won with %d lives remaining!" % (chosen,lives))
                game = False
            #End the game if the player runs out of lives and print The Hanged Man
            if (lives == 0):
                print("That's Hangman - Game Over! The word was '%s'\n ___\n|   |\n|   O\n|  -|-\n|   ^" % chosen)
                game = False

hangman.hangman()
