import random, os, csv

class wordGuess:
    """ To get a list of words from a file """
    # ''' Change Directory '''
    # os.chdir("{DriveLetter}:/{Folder}")
    # print(f"\n{os.getcwd()}")

    # wordBucket = []
    steps = 0
    guesses = 3
    score = 0
    correctWord = ""

    wordBucket = ["upon","maid","gone","feel","that","rich","came",
                "much","with","wall","moliki","time","sand","Into","Flat",
                "mile","done","part","come","seen","loss", "went",
                "were","rock","long","those","google", "tshimologo",
                "tshirelletso","python","reginald"]


#     def openFile():
#         with open("sowpods.txt", "r") as rFile:
#             oFile = csv.reader(rFile)

#             for docLine in oFile:
#                 for docWord in docLine:
#                     wordList = docWord.split(" ")
#                     for wordStrings in wordlist:
#                         if wordStrings != "":
#                             wordGuess.wordBucket.append(wordStrings)
                
#         return f"WordBucket has been populated with {len(wordGuess.wordBucket)} words."
# ## End of OpenFile() method


    def generateWord():
        ## a variable that'll represent a word in Array
        wordBucketIndex = random.randint(0,len(wordGuess.wordBucket))

        try:
            wordFromIndex = wordGuess.wordBucket[wordBucketIndex].upper()
        except IndexError as listIndexError:
            wordFromIndex = wordGuess.wordBucket[wordBucketIndex-1].upper()
            # outputErr = input("print Error Y/N: ").upper()
            # if outputErr == "Y":
                # print(f"\n{listIndexError}\n")

        wordGuess.correctWord = wordFromIndex 
        return wordFromIndex
## End of generateWord() function


    def shuffleWord(generatedWord):
        brokenDownWord = list(generatedWord)
        random.shuffle(brokenDownWord)
        shuffledLetters = "    ".join(brokenDownWord)
        return shuffledLetters
## End of shuffleWord() function


    def tryTimes(correctword):
        wordGuess.guesses -= 1
        while True:
            print(f"\n Your answer is incorrect. TRY AGAIN \
                \n Guesses Left = {wordGuess.guesses} \n \
                \n {wordGuess.shuffleWord(correctword)}")
                        
            answer = input("\nEnter the correct word: ").upper()

            if answer == correctword:
                print("You are correct! Well done")
                wordGuess.score += 1
                break
            elif wordGuess.guesses == 0:
                wordGuess.score -= 1
                wordGuess.guesses -= 1
                break
            elif answer != correctword:
                wordGuess.guesses -= 1                            
## End of tryTimes() function


    def playGame():
        # wordGuess.openFile()
        wordsToRecieve = int(input(f"There are {len(wordGuess.wordBucket)} words in the Bucket \
        \n How many words would you like to get? : "))

        if (wordsToRecieve <= len(wordGuess.wordBucket)) and (wordsToRecieve > 0):
            
            ## Loop through the Array of words
            while (wordGuess.steps < int(wordsToRecieve)) and \
                (wordGuess.guesses > (-1)):

                print(f"\n {wordGuess.shuffleWord(wordGuess.generateWord())}")
                
                userAnswer = input("\nEnter the correct word: ").upper()
                if userAnswer == wordGuess.correctWord:
                    print("You are correct! Well done")
                    wordGuess.score += 1
                elif wordGuess.guesses <= 0:
                    print("\nGame Over")
                    break
                else:
                    wordGuess.tryTimes(wordGuess.correctWord)
                    
                wordGuess.steps += 1
                print(f"\nCurrent score = {wordGuess.score}.")

            ## Message after the loop
            if wordGuess.score == wordsToRecieve:
                print(f"Congratulations! You got all {wordsToRecieve} answers correct!")
            elif wordGuess.guesses <= 0:
                print(f"\nThis is so sad.. You ran out of guesses. GAME OVER \
                    \n Better luck next time in getting all {wordsToRecieve} answers correct")
            else:
                print(f":) Better luck next time in getting all {wordsToRecieve} answers correct")


        elif wordsToRecieve <= 0:
            print("There's always a next time. :)")
        ## Output range exceeded if > length of bucket items
        else:
            print("\n Sorry for the inconvenience. \
                \n Your range has exceeded the words in the Bucket")
## End of playGame function
"""
## End of wordGuess Class 
"""

wordGuess.playGame()
