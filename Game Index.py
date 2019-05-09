import random

"""
The SHUFFLE lines of codes needs to be seperated 
Modify tryTimes() method

TRY THIS
gameAnswer
answer = input(....)
gameAnswer = answer

if gameAnswer == correctWord: ....

try():
    answer = input(....)
    gameAnswer = answer

    if gameAnswer == correctWord: ....
"""

class ourGame:
    steps = 0
    guesses = 3
    score = 0

    wordBucket = ["upon","maid","gone","feel","that","rich","came",
                "much","with","wall","time","sand","Into","Flat",
                "mile","done","part","come","seen","loss", "went",
                "were","rock","long","those","google", "tshimologo",
                "tshirelletso","python"]


    def generateWord():
        ## a variable that'll represent a word in Array
        wordBucketIndex = random.randint(0,len(ourGame.wordBucket))
        try:
            wordFromIndex = ourGame.wordBucket[wordBucketIndex].upper()
        except IndexError as eGen:
            wordFromIndex = ourGame.wordBucket[wordBucketIndex-1].upper()
            tEstErr = input("print Error Y/N: ").upper()
            if tEstErr == "Y":
                return eGen
            else:
                return wordFromIndex
            # return eGen
        ## convert items in the Array to Uppercase
##        wordFromIndex = ourGame.wordBucket[wordBucketIndex].upper()

        return wordFromIndex
## End of generateWord() function




    def shuffleWord(generatedWord):
        brokeDownWord = list(generatedWord)
        random.shuffle(brokeDownWord)
        shuffledLetters = print("     ".join(brokeDownWord))
        return shuffledLetters
## End of shuffleWord() function




    def displayWord():
        wordString = str(ourGame.generateWord())
        ourGame.shuffleWord(wordString)
        return wordString
## End of displayWord() function




    def tryTimes(answers, correctword):
        ourGame.guesses -= 1
        while (answers != correctword):
            print(f"\n Your answer is incorrect. TRY AGAIN \
                \n guesses left = {ourGame.guesses} \n")
            
            ourGame.shuffleWord(correctword)
            
            answer = input("\nEnter the correct word: ").upper()
            answers = answer
            if answers == correctword:
                ourGame.score += 1
                break
            elif ourGame.guesses == 0:
                ourGame.score -= 1
                ourGame.guesses -= 1
                break
            elif answers != correctword:
                ourGame.guesses -= 1                            
## End of tryTimes() function




    def playGame():
        wordsRecieved = int(input(f"There are {len(ourGame.wordBucket)} words in the Bucket \
        \n How many words would you like to get? : "))

        if (wordsRecieved < len(ourGame.wordBucket) or \
            wordsRecieved == len(ourGame.wordBucket)) and (wordsRecieved != 0):
            
            ## Loop through the Array of words
            while (ourGame.steps < int(wordsRecieved)) and \
                (ourGame.guesses > (-1)):

                correctWord = str(ourGame.displayWord())

                userAnswer = input("Word: ").upper()
                if userAnswer == correctWord:
                    ourGame.score += 1
                elif ourGame.guesses == 0 or ourGame.guesses < 0:
                    print("\nGame Over")
                    break
                else:
                    try:
                        ourGame.tryTimes(userAnswer,correctWord)
                    except:
                        return "Something's wrong"

                ourGame.steps += 1


                print(f"\nCurrent score = {ourGame.score}. Guesses left = {ourGame.guesses}")

            ## Message after the loop
            if ourGame.guesses < 0 or ourGame.guesses == 0:
                print(f"\nThis is so sad.. You ran out of guesses. GAME OVER \
                    \n Better luck next time in getting all {wordsRecieved} answers correct")
            elif ourGame.score == wordsRecieved:
                print(f"Congratulations! You got all {wordsRecieved} answers correct!")
            else:
                print(f":) Better luck next time in getting all {wordsRecieved} answers correct")


        elif wordsRecieved == 0 or wordsRecieved < 0:
            print("There's always a next time. :)")
        ## Output range exceeded if < length of bucket items
        else:
            print("\n Sorry for the inconvenience. \
                \n Your range has exceeded the Bucket items")
## End of playGame function
"""
## End of ourGame Class 
"""

ourGame.playGame()

