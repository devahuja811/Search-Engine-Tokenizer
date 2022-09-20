import re
import string


def mergeAbbreviations(inputList):
    # if dot:
            # split by dot. If all words greater than length 1, not an abbv. 
            #               # if "Mr" or "mrs" in word.lower, process by concatenating
    resList=[]
    for i in range(len(inputList)):
        if not inputList[i]:
            continue
        if '.' not in inputList[i]:
            resList.append(inputList[i])
            continue
        else:
            curWord=inputList[i]
            splitWord=curWord.split(".")
            if "mr" in splitWord[0].lower() or "mrs" in splitWord[0].lower():
                resList.append(splitWord[0]+inputList[i+1])
                inputList[i+1]=None
            elif(sum(c.isalpha() for c in curWord) > curWord.count('.')): # need to fix
                for part in splitWord:
                    if len(part)>0:
                        resList.append(part)
                    
            else:
                resList.append(''.join(splitWord))
    return resList 

    



if __name__=="__main__":
    with open("tokenization-input-part-A.txt") as tokenFile:
        with open("stopwords.txt") as stopWordFile:
            input=tokenFile.read()
            input=input.split()
            input= "Mr. Bentley Ph.D. U.S.A. A.B.C.'s"
            input=input.split()
            # input= [s.translate(str.maketrans('', '', string.punctuation.replace(".", ""))) for s in input]
            print(input)

            print(mergeAbbreviations(input))
            
            
