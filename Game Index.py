import random

class wordGuess:

'''To get a list of words from a file'''
##    ''' Change Directory '''
##    os.chdir("d:/Documents")
##    print(f"\n{os.getcwd()}")
##
##    wordBucket = []
##    steps = 0
##    guesses = 3
##    score = 0
##
##
##    def openFile():
##        with open("test.txt", "r") as rFile:
##            oFile = csv.reader(rFile)
##
##            for docLine in oFile:
##                for docWord in docLine:
##                    Words = docWord.split(" ",5)
##                    for wSTR in range(len(Words)):
##                        if Words[wSTR] != "":
##                            wordGuess.wordBucket.append(Words[wSTR])
##                        else:
##                            pass
##                        
##        return list(wordGuess.wordBucket)
#### End of OpenFile() method
##

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
        wordBucketIndex = random.randint(0,len(wordGuess.wordBucket))

        try:
            wordFromIndex = wordGuess.wordBucket[wordBucketIndex].upper()
        except IndexError as listIndexError:
            wordFromIndex = wordGuess.wordBucket[wordBucketIndex-1].upper()
            outPutErr = input("print Error Y/N: ").upper()
            if outPutErr == "Y":
                print(f"\n{listIndexError}\n")
            else:
                return wordFromIndex
       
        return wordFromIndex
## End of generateWord() function


    def shuffleWord(generatedWord):
        brokeDownWord = list(generatedWord)
        random.shuffle(brokeDownWord)
        shuffledLetters = print("     ".join(brokeDownWord))
        return shuffledLetters
## End of shuffleWord() function


    def displayWord():
        wordString = str(wordGuess.generateWord())
        wordGuess.shuffleWord(wordString)
        return wordString
## End of displayWord() function


    def tryTimes(answers, correctword):
        wordGuess.guesses -= 1
        while (answers != correctword):
            print(f"\n Your answer is incorrect. TRY AGAIN \
                \n Guesses Left = {wordGuess.guesses} \n")
            
            wordGuess.shuffleWord(correctword)
            answer = input("\nEnter the correct word: ").upper()

            answers = answer
            if answers == correctword:
                print("You are correct! Well done")
                wordGuess.score += 1
                break
            elif wordGuess.guesses == 0:
                wordGuess.score -= 1
                wordGuess.guesses -= 1
                break
            elif answers != correctword:
                wordGuess.guesses -= 1                            
## End of tryTimes() function


    def playGame():
        wordsToRecieve = int(input(f"There are {len(wordGuess.wordBucket)} words in the Bucket \
        \n How many words would you like to get? : "))

        if (wordsToRecieve <= len(wordGuess.wordBucket)) and (wordsToRecieve > 0):
            
            ## Loop through the Array of words
            while (wordGuess.steps < int(wordsToRecieve)) and \
                (wordGuess.guesses > (-1)):
                print("\n")

                correctWord = str(wordGuess.displayWord())

                userAnswer = input("\nType in the word correctly: ").upper()
                if userAnswer == correctWord:
                    print("You are correct! Well done")
                    wordGuess.score += 1
                elif wordGuess.guesses <= 0:
                    print("\nGame Over")
                    break
                else:
                    try:
                        wordGuess.tryTimes(userAnswer,correctWord)
                    except:
                        return "Something's wrong"

                wordGuess.steps += 1
                print(f"\nCurrent score = {wordGuess.score}.")

            ## Message after the loop
            if wordGuess.guesses <= 0:
                print(f"\nThis is so sad.. You ran out of guesses. GAME OVER \
                    \n Better luck next time in getting all {wordsToRecieve} answers correct")
            elif wordGuess.score == wordsToRecieve:
                print(f"Congratulations! You got all {wordsToRecieve} answers correct!")
            else:
                print(f":) Better luck next time in getting all {wordsToRecieve} answers correct")


        elif wordsToRecieve <= 0:
            print("There's always a next time. :)")
        ## Output range exceeded if > length of bucket items
        else:
            print("\n Sorry for the inconvenience. \
                \n Your range has exceeded the Bucket items")
## End of playGame function
"""
## End of wordGuess Class 
"""

wordGuess.playGame()
