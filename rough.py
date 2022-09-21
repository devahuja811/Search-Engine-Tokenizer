import enum
import re
import string
def splitUsingDelimiters(inputStr):
    return re.split("[, \-!?:]+",inputStr)

wordList=["Ph.D.", "A.B.C.s", "Mr. Bentley", "U.S.A."]
words= "Ph.D. A.B.C.'s Mr. Bentley U.S.A. 200,000 O'Brian"
# words= words.translate(str.maketrans('', '', string.punctuation.replace(".", "")))

print(splitUsingDelimiters(words))

for word in wordList:
    if '.' not in word:
        continue
    else:

        # if re.search("([A-Za-z]\.)+$ | ([A-Za-z]\.)+([A-Za-z])$", word) is None:
        #     print(word)
        if re.search("^([a-zA-Z]\.)+$|^([a-zA-Z]\.)+([a-zA-Z]$)", word):
            print(word)


def checkVowelPresence(word, endLength, vowels):
    firstVowel=-2
    firstNonVowel=-1
    for index, char in enumerate(word[:endLength]):
        if char in vowels:
            firstVowel=index
            break
    for index, char in enumerate(word[:endLength]):
        if char not in vowels and index>firstVowel:
            firstNonVowel=index
            break
    return word[:endLength]+"ee" if firstNonVowel !=-1 else word   
def isConsonant(char):
    return char not in "aeiou"
def CVCV(word):
    vowelIndex=-1
    for index, char in enumerate(word):
        if not isConsonant(char) and index!=len(word)-1:
            print(char)
            vowelIndex=index
            break
    print(vowelIndex)
            
    return isConsonant(word[0]) and not isConsonant(word[-1]) and vowelIndex!=-1 and any(word.index(s)>vowelIndex and isConsonant(s) for s in word)

def CVC(word):
    return isConsonant(word[0]) and isConsonant(word[-1]) and any(not isConsonant(s) for s in word)
def VCV(word):
    return not isConsonant(word[0]) and not isConsonant(word[-1]) and any(isConsonant(s) for s in word)
def VC(word):
    return not isConsonant(word[0]) and isConsonant(word[-1])
word="hoping"
print(CVC(word))




# def mergeAbbreviations(inputList):
#     # if dot:
#             # split by dot. If all words greater than length 1, not an abbv. 
#             #               # if "Mr" or "mrs" in word.lower, process by concatenating
#     resList=[]
#     for i in range(len(inputList)):
#         if not inputList[i]:
#             continue
#         if '.' not in inputList[i]:
#             resList.append(inputList[i])
#             continue
#         else:
#             curWord=inputList[i]
#             splitWord=curWord.split(".")
#             if "mr" in splitWord[0].lower() or "mrs" in splitWord[0].lower():
#                 resList.append(splitWord[0]+inputList[i+1])
#                 inputList[i+1]=None
#             elif(sum(c.isalpha() for c in curWord) > curWord.count('.')): # need to fix
#                 for part in splitWord:
#                     if len(part)>0:
#                         resList.append(part)
                    
#             else:
#                 resList.append(''.join(splitWord))
#     return resList 


            # input= [s.translate(str.maketrans('', '', string.punctuation.replace(".", ""))) for s in input]
            # processAbbreviations(inputList)