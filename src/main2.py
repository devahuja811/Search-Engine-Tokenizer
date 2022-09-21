
import re



def isConsonant(char):
    return char not in "aeiou"

def implementStemmerA(wordList):
    for i in range(len(wordList)):
        curWord=wordList[i]
        if curWord.endswith("sses"):
            wordList[i]=curWord[:len(curWord)-4]+"ss"
        if curWord.endswith("ied") or curWord.endswith("ies"):
            wordList[i]=curWord[:len(curWord)-3] +"i" if len(curWord)-3 > 1 else curWord[:len(curWord)-3]+"ie"
        if curWord.endswith("us") or curWord.endswith("ss"):
            continue
        if curWord.endswith("s"):
            vowels={"a", "e", "i", "o", "u"}
            if curWord[-2] not in vowels:
                wordList[i]= curWord[:len(curWord)-1]
    return wordList
def checkVowelPresence(word, endLength, vowels):
    firstVowel=-2
    firstNonVowel=-1
    for i in range(len(word[:endLength])):
        if word[i] in vowels:
            firstVowel=i
            break
    # for index, char in enumerate(word[:endLength]):
    #     if char in vowels:
    #         firstVowel=index
    #         break
    for j in range(len(word[:endLength])):
        if word[j] not in vowels and j>firstVowel:
            firstNonVowel=j
            break
    # for index, char in enumerate(word[:endLength]):
    #     if char not in vowels and index>firstVowel:
    #         firstNonVowel=index
    #         break
    return word[:endLength]+"ee" if firstVowel >-1 and firstNonVowel>firstVowel else word        
    
def CVCV(word):
    vowelIndex=-1
    for index, char in enumerate(word):
        if not isConsonant(char) and index!=len(word)-1:
            

            vowelIndex=index
            break

            
    return isConsonant(word[0]) and not isConsonant(word[-1]) and vowelIndex!=-1 and any(word.index(s)>vowelIndex and isConsonant(s) for s in word) 

def CVC(word):
    return isConsonant(word[0]) and isConsonant(word[-1]) and any(not isConsonant(s) for s in word)
def VCV(word):
    return not isConsonant(word[0]) and not isConsonant(word[-1]) and any(isConsonant(s) for s in word)
def VC(word):
    return not isConsonant(word[0]) and isConsonant(word[-1])


def implementStemmerB(wordList):
    vowels={"a", "e", "i", "o", "u"}    
    for i in range(len(wordList)):
        curWord=wordList[i]
        print(curWord)
        if (curWord.endswith("eed") or curWord.endswith("eedly")):
            wordList[i] = checkVowelPresence(curWord, len(curWord)-3, vowels) if curWord.endswith("eed") else checkVowelPresence(curWord, len(curWord)-5, vowels)
        elif (curWord.endswith("ed") or curWord.endswith("eedly") or curWord.endswith("ing") or curWord.endswith("ingly")):
            if curWord.endswith("ed"):
                if any(s in vowels for s in curWord[:len(curWord)-2]):
                    wordList[i]=curWord[:len(curWord)-2]
            elif curWord.endswith("eedly") or curWord.endswith("ingly"):
                if any(s in vowels for s in curWord[:len(curWord)-5]):
                    wordList[i]=curWord[:len(curWord)-5]
            elif curWord.endswith("ing"):
                if any(s in vowels for s in curWord[:len(curWord)-3]):
                    wordList[i]=curWord[:len(curWord)-3]
            updatedWord=wordList[i]

            
            if updatedWord.endswith("at") or updatedWord.endswith("bl") or updatedWord.endswith("iz"):
                wordList[i]+="e"
            elif len(wordList[i])>2 and (wordList[i][-2]== wordList[i][-1]) and (wordList[i][-1]!='l' and wordList[i][-1]!='s' and wordList[i][-1]!='z'):
                wordList[i]=wordList[i][:-1]
                updatedWord=""
            elif(len(wordList[i])>2 and (wordList[i][-2]== wordList[i][-1]) and (wordList[i][-1]=='l' or wordList[i][-1]=='s' or wordList[i][-1]=='z')):
                continue
            elif len(updatedWord)>0 and (CVCV(updatedWord) or CVC(updatedWord) or VCV(updatedWord) or VC(updatedWord)):
                wordList[i]+='e'
        #-Whew!
    return wordList
                



# strips input list of all punctuations except apostrophe, commmas, and periods as these are needed for abbreviations and merging
def splitUsingDelimiters(inputStr):
    return re.split("[, \-!?:\n () /]+",inputStr)

#checks for abbreviations and adds to new list accordingly
def processAbbreviations(inputList):
    resList=[]
    for i in range(len(inputList)):
        word=inputList[i]
        if not word:
            continue
        if '.' not in word:
            resList.append(word)
            continue
        else:
            if re.search("^([a-zA-Z]\.)+$|^([a-zA-Z]\.)+([a-zA-Z]$)", word): #is an abbreviation
                resList.append(''.join(word.split(".")))
            elif "mr" in word.lower() or "mrs" in word.lower():
                resList.append(word.split(".")[0]+inputList[i+1])
                inputList[i+1]=None
            else:
                for part in word.split("."):
                    if len(part)>0:
                        resList.append(part)
    return resList

#removes stop words based on given file
def removeStopWords(inputList, stopWordList):
    alNumCopy=inputList
    alNumCopy= [x for x in alNumCopy if x not in stopWordList]
    return alNumCopy

if __name__=="__main__":
    with open("tokenization-input-part-A.txt") as tokenFile:
        with open("stopwords.txt") as stopWordFile:
            input=tokenFile.read()
            stopWordList= stopWordFile.read().split("\n")
            #input= "Don't Mr. Bentley Ph.D. U.S.A. A.B.C.'s 200,000 O'Brian"            
            inputList=splitUsingDelimiters(input)
            inputList=[s.replace("'", "").replace('"', "") for s in inputList]
            afterAbbvs=processAbbreviations(inputList)            
            allLower=[s.lower() for s in afterAbbvs]
            processedList=removeStopWords(allLower, stopWordList)
            testList=["agreed", "feed","fished", "pirating", "falling", "dripping", "hoping"]
            # testList=["pirating"]
            
            print(implementStemmerB(testList))

            

            
            
            
