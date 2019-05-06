import random

"""
The SHUFFLE lines of codes needs to be seperated 
"""

class ourGame:
    guesses = 3
    score = 0

    wordBucket = ["upon","maid","gone","feel","that","rich","came",
                "much","with","wall","time","sand","Into","Flat",
                "mile","done","part","come","seen","loss", "went",
                "were","rock","long","those","google", "tshimologo",
                "tshirelletso"]

    def generateWord():
        ## a variable that'll represent a word in Array
        wordBucketIndex = random.randint(0,len(ourGame.wordBucket))

        ## convert items in the Array to Uppercase
        wordList = ourGame.wordBucket[wordBucketIndex].upper()

        ## convert the word to a list of characters
        ## for random.shuffle to shuffle the letters
        myWords = list(wordList)

        ## Shuffle the letters of the word
        # random.shuffle(myWords)

        # # ## Output the shuffled letters to the user
        # print("\n")
        # wordScrambled = print('     '.join(myWords))
        # # answer = input("Enter the correct word: ").upper()
        return myWords
## End of generateWord() function


    def shuffledWord(myWords):
        random.shuffle(myWords)
        D = print("     ".join(myWords))
        return D
## End of shuffleWord() function



    def sh():
        ourGame.shuffledWord(ourGame.generateWord())










    def tryTimes(answers, wordlist, myWords):
        while (answers != wordlist) and (ourGame.guesses > 0):
            print(f"\n Your answer is incorrect. TRY AGAIN \n guesses left = {ourGame.guesses} \n")
            print('     '.join(myWords))
            answer = input("Enter the correct word: ").upper()
            answers = answer
            if answers == wordlist:
                ourGame.score += 1
                break
            elif answers != wordlist:
                ourGame.guesses -= 1
            elif guesses == 0:
                ourGame.score -= 1
                break
            
        print(wordlist + " " + answers)
## End of tryTimes() function





    














    # def playTimes(wordsRecieved):
    #     if (wordsRecieved < len(ourGame.wordBucket)) and (wordsRecieved != 0):

    #         ## Loop through the Array of words
    #         # for i in range(0,int(wordsRecieved)):
    #         #     ## a variable that'll represent a word in Array
    #         #     j = random.randint(0,len(ourGame.wordBucket))

    #         #     ## convert items in the Array to Uppercase
    #         #     wordList = ourGame.wordBucket[j].upper()

    #         #     ## convert the word to a list of characters
    #         #     ## for random.shuffle to shuffle the letters
    #         #     myWords = list(wordList)

    #         #     ## Shuffle the letters of the word
    #         #     random.shuffle(myWords)

    #         #     ## Output the shuffled letters to the user
    #         #     print("\n")
    #         #     print('     '.join(myWords))
    #             answer = input("Enter the correct word: ").upper()

    #             ## Compare answer to the actual word
    #             if answer == wordList:
    #                 print("\n Yes! You are correct.")
    #                 ourGame.score += 1

    #             elif ourGame.guesses == 0:
    #                 print("\nGAME OVER\n")
    #                 break

    #             elif (answer != wordList) and (ourGame.guesses != 0):
    #                 ourGame.guesses -= 1
    #                 try:
    #                     ourGame.tryTimes(answer, wordList, myWords)
    #                 except IndexError as ve:
    #                     print("Error")
                    
    #                 print(f"\n \n You have {ourGame.guesses} guesses left \n \n")
                    
    #             else:
    #                 print(f"Sorry. {answer} is not the correct answer. ===== {guesses}")                
    #                 ourGame.score -= 1

    #             print(f'Your score is now {ourGame.score} \n')

    #         ## Message after the loop
    #         if ourGame.score == wordsRecieved:
    #             print(f"Congratulations! You got all {wordsRecieved} answers correct!")
    #         else:
    #             print(f":) Better luck next time in getting all {wordsRecieved} answers correct")


    #     elif wordsRecieved == 0 or wordsRecieved < 0:
    #         print("There's always a next time. :)")

    #     ## Output range exceeded if < length of bucket items
    #     else:
    #         print("\n Sorry for the inconvenience. \
    #             \n Your range has exceeded the Bucket items")

    # # End of playTimes function





ourGame.sh()






# wordsRecieved = int(input(f"There are {len(ourGame.wordBucket)} \words in the Bucket \
#  \n How many words would you like to get? : "))


# ourGame.playTimes(wordsRecieved)




















































# """

# import random

# """
# The SHUFFLE lines of codes needs to be seperated 
# """

# class ourGame:
#     guesses = 3
#     score = 0

#     wordBucket = ["upon","maid","gone","feel","that","rich","came",
#                 "much","with","wall","time","sand","Into","Flat",
#                 "mile","done","part","come","seen","loss", "went",
#                 "were","rock","long","those","google", "tshimologo",
#                 "tshirelletso"]


#     def tryTimes(answers, wordlist, myWords):
#         while (answers != wordlist) and (ourGame.guesses > 0):
#             print(f"\n Your answer is incorrect. TRY AGAIN \n guesses left = {ourGame.guesses} \n")
#             print('     '.join(myWords))
#             answer = input("Enter the correct word: ").upper()
#             answers = answer
#             if answers == wordlist:
#                 ourGame.score += 1
#                 break
#             elif answers != wordlist:
#                 ourGame.guesses -= 1
#             elif guesses == 0:
#                 ourGame.score -= 1
#                 break
            
#         print(wordlist + " " + answers)


#     def playTimes(wordsRecieved):
#         if (wordsRecieved < len(ourGame.wordBucket)) and (wordsRecieved != 0):

#             ## Loop through the Array of words
#             for i in range(0,int(wordsRecieved)):
#                 ## a variable that'll represent a word in Array
#                 j = random.randint(0,len(ourGame.wordBucket))

#                 ## convert items in the Array to Uppercase
#                 wordList = ourGame.wordBucket[j].upper()

#                 ## convert the word to a list of characters
#                 ## for random.shuffle to shuffle the letters
#                 myWords = list(wordList)

#                 ## Shuffle the letters of the word
#                 random.shuffle(myWords)

#                 ## Output the shuffled letters to the user
#                 print("\n")
#                 print('     '.join(myWords))
#                 answer = input("Enter the correct word: ").upper()

#                 ## Compare answer to the actual word
#                 if answer == wordList:
#                     print("\n Yes! You are correct.")
#                     ourGame.score += 1

#                 elif ourGame.guesses == 0:
#                     print("\nGAME OVER\n")
#                     break

#                 elif (answer != wordList) and (ourGame.guesses != 0):
#                     ourGame.guesses -= 1
#                     try:
#                         ourGame.tryTimes(answer, wordList, myWords)
#                     except IndexError as ve:
#                         print("Error")
                    
#                     print(f"\n \n You have {ourGame.guesses} guesses left \n \n")
                    
#                 else:
#                     print(f"Sorry. {answer} is not the correct answer. ===== {guesses}")                
#                     ourGame.score -= 1

#                 print(f'Your score is now {ourGame.score} \n')

#             ## Message after the loop
#             if ourGame.score == wordsRecieved:
#                 print(f"Congratulations! You got all {wordsRecieved} answers correct!")
#             else:
#                 print(f":) Better luck next time in getting all {wordsRecieved} answers correct")


#         elif wordsRecieved == 0 or wordsRecieved < 0:
#             print("There's always a next time. :)")

#         ## Output range exceeded if < length of bucket items
#         else:
#             print("\n Sorry for the inconvenience. \
#                 \n Your range has exceeded the Bucket items")

#     # End of playTimes function



# wordsRecieved = int(input(f"There are {len(ourGame.wordBucket)} \words in the Bucket \
#  \n How many words would you like to get? : "))


# ourGame.playTimes(wordsRecieved)

