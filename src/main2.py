import re
import string

# def mergeAbbreviations(inputList):
#     # if dot:
            #split by dot. If all words greater than length 1, not an abbv. 
#                           # if "Mr" or "mrs" in word.lower, process by concatenating
            
#     for i in range(len(inputList)):


if __name__=="__main__":
    with open("tokenization-input-part-A.txt") as tokenFile:
        with open("stopwords.txt") as stopWordFile:
            input=tokenFile.read()
            input=input.split()

            input=["Mr. Bentley", "Ph.D."]
            input= [s.translate(str.maketrans('', '', string.punctuation.replace(".", ""))) for s in input]
            
            
