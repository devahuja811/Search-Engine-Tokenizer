from lib2to3.pgen2 import token
import matplotlib.pyplot as plt
import re

# checks if character is a consonant
def isConsonant(char):
    return char not in "aeiou"

#Main function to implement step 1a of the Porter Stemmer
def implementStemmerA(wordList):
    for i in range(len(wordList)):
        curWord=wordList[i]
        #check word ending based on given cases and add appropriate replacement suffixes
        if curWord.endswith("sses"):
            wordList[i]=curWord[:len(curWord)-4]+"ss"
        if curWord.endswith("ied") or curWord.endswith("ies"):
            wordList[i]=curWord[:len(curWord)-3] +"i" if len(curWord)-3 > 1 else curWord[:len(curWord)-3]+"ie"
        if curWord.endswith("us") or curWord.endswith("ss"):
            continue
        if curWord.endswith("s"):
            vowels={"a", "e", "i", "o", "u"}
            if len(curWord) >1 and curWord[-2] not in vowels:
                wordList[i]= curWord[:len(curWord)-1]
    return wordList

#used in part b of the Porter Stemmer to check if vowel exists in the word and first consonant occurs after it Returns modified or same word accordingly
def checkVowelPresence(word, endLength, vowels):
    firstVowel=-2
    firstConsonant=-1
    # end length specified to only iterate until the suffix as suffix needs to be modified
    for i in range(len(word[:endLength])):
        if word[i] in vowels:
            firstVowel=i
            break

    for j in range(len(word[:endLength])):
        if word[j] not in vowels and j>firstVowel:
            firstConsonant=j
            break

    return word[:endLength]+"ee" if firstVowel >-1 and firstConsonant>firstVowel else word        

# follows CVCV pattern of word being short consisting of series of consonants and vowels respectively in alternate manner   
def CVCV(word):
    vowelIndex=-1
    for index, char in enumerate(word):
        if not isConsonant(char) and index!=len(word)-1: 
            vowelIndex=index
            break

            
    return isConsonant(word[0]) and not isConsonant(word[-1]) and vowelIndex!=-1 and any(word.index(s)>vowelIndex and isConsonant(s) for s in word) 

# follows CVC pattern of word being short consisting of series of consonants and vowels respectively in alternate manner 
def CVC(word):
    return isConsonant(word[0]) and isConsonant(word[-1]) and any(not isConsonant(s) for s in word)

# follows VCV pattern of word being short consisting of series of consonants and vowels respectively in alternate manner 
def VCV(word):
    return not isConsonant(word[0]) and not isConsonant(word[-1]) and any(isConsonant(s) for s in word)

# follows VC pattern of word being short consisting of series of consonants and vowels respectively in alternate manner 
def VC(word):
    return not isConsonant(word[0]) and isConsonant(word[-1])

#main function to implement part 1b of the Porter Stemmer
def implementStemmerB(wordList):
    vowels={"a", "e", "i", "o", "u"}    
    for i in range(len(wordList)):
        curWord=wordList[i]
        #checking suffixes and calling checkVowelPresence based on length of suffix
        if (curWord.endswith("eed") or curWord.endswith("eedly")):
            wordList[i] = checkVowelPresence(curWord, len(curWord)-3, vowels) if curWord.endswith("eed") else checkVowelPresence(curWord, len(curWord)-5, vowels)
        elif (curWord.endswith("ed") or curWord.endswith("eedly") or curWord.endswith("ing") or curWord.endswith("ingly")):
            #deleting suffix if word ends with above suffixes
            if curWord.endswith("ed"):
                if any(s in vowels for s in curWord[:len(curWord)-2]):
                    wordList[i]=curWord[:len(curWord)-2]
            elif curWord.endswith("eedly") or curWord.endswith("ingly"):
                if any(s in vowels for s in curWord[:len(curWord)-5]):
                    wordList[i]=curWord[:len(curWord)-5]
            elif curWord.endswith("ing"):
                if any(s in vowels for s in curWord[:len(curWord)-3]):
                    wordList[i]=curWord[:len(curWord)-3]
            #new word pointer for modified word
            updatedWord=wordList[i]

                   
            if updatedWord.endswith("at") or updatedWord.endswith("bl") or updatedWord.endswith("iz"):
                wordList[i]+="e"
            #checking if word ends with a double letter and not ll,ss, zz
            elif len(wordList[i])>2 and (wordList[i][-2]== wordList[i][-1]) and (wordList[i][-1]!='l' and wordList[i][-1]!='s' and wordList[i][-1]!='z'):
                wordList[i]=wordList[i][:-1]
                updatedWord=""
            # escape condition for words like "fall" that may enter the condition below for short words.
            elif(len(wordList[i])>2 and (wordList[i][-2]== wordList[i][-1]) and (wordList[i][-1]=='l' or wordList[i][-1]=='s' or wordList[i][-1]=='z')):
                continue
            #checking if word is short based on patterns as mentioned in the book
            elif len(updatedWord)>0 and (CVCV(updatedWord) or CVC(updatedWord) or VCV(updatedWord) or VC(updatedWord)):
                wordList[i]+='e'
    
    return wordList # returns modified word list


# strips input list of all punctuations except apostrophe, and periods as these are needed for abbreviations and merging
def splitUsingDelimiters(inputStr):
    return re.split("[, \-!?:\n () /_ \[\] /{\} \*;\" #]+",inputStr)

#checks for abbreviations and adds to new list accordingly
def processAbbreviations(inputList):
    resList=[]
    for i in range(len(inputList)):
        word=inputList[i]
        # if word is None, as done in cases where 2 elements are being concatenated
        if not word:
            continue
        #if the word does not contain a . , it is not modified.
        if '.' not in word:
            resList.append(word)
            continue
        else:
            # Case 1: Abbreviation is of type A.B.C. where there is a single alphanumeric character before a period.
            if re.search("^([a-zA-Z]\.)+$|^([a-zA-Z]\.)+([a-zA-Z]$)", word):
                resList.append(''.join(word.split(".")))
            #Case 2: Title case: As assumed in the class discussion, titles are to be concatenated with the name of the person
            elif "mr." in word.lower() or "mrs." in word.lower():
                #Checking if there is a name after title
                if(i+1)>=len(inputList): 
                    continue
                #Concatenate title and name    
                resList.append(word.split(".")[0]+inputList[i+1])
                #Setting name index to None to prevent repetition.
                inputList[i+1]=None
            else:
                #For words like Ph.D., adding all the words into the result list after splitting by the period.
                for part in word.split("."):
                    if len(part)>0:
                        resList.append(part)
    return resList

#removes stop words based on given file
def removeStopWords(inputList, stopWordList):
    alNumCopy=inputList
    alNumCopy= [x for x in alNumCopy if x not in stopWordList]
    return alNumCopy

def tokenizeFile(inputFilename, stopWordFilename):
    with open(inputFilename, encoding='utf-8-sig') as tokenFile:
        with open(stopWordFilename) as stopWordFile:

            ################### PART 1 #################################
            inputFile=tokenFile.read() #string containing input data
            stopWordList= stopWordFile.read().split("\n")          
            #convert input to list by removing punctuations 
            inputList=splitUsingDelimiters(inputFile)           
            #concatenating words with apostrophes such as don't and O'Brian
            inputList=[s.replace("'", "").replace('"', "") for s in inputList]
            #Merging and Splitting abbreviations 
            afterAbbvs=processAbbreviations(inputList) 
            #  converting all words to lowercase         
            all_lower=[s.lower() for s in afterAbbvs]

            ################### PART 2 #################################
            #removing stop words so that the list is ready to be stemmed in part 3
            processedList=removeStopWords(all_lower, stopWordList)

            ################### PART 3 #################################
            #implement step 1a of stemmer
            stemA=implementStemmerA(processedList)
            #implement step 1b of stemmer to receive the final refined list
            finalList=implementStemmerB(stemA)
    return finalList



def partA():
    tokenizedList=tokenizeFile("tokenization-input-part-A.txt", "stopwords.txt")
    with open("tokenized-A.txt", 'w', encoding='utf-8-sig') as outfile:
        for term in tokenizedList:
            outfile.write(term +"\n")
    return tokenizedList

def partB():
    tokenizedList=tokenizeFile("tokenization-input-part-B.txt", "stopwords.txt")
    wordCounts={}
    #Counting words and appending to dictionary
    for term in tokenizedList:
        if term in wordCounts:
            wordCounts[term]+=1
        else:
            wordCounts[term]=1
    #Sorting dictionary values in reverse order to get the most frequent elements (higher count) at the start
    sortedWordCounts=sorted(wordCounts.items(), key=lambda kv: kv[1], reverse=True)
    #writing results to output file as required.
    with open("terms-B.txt", "w", encoding='utf-8-sig') as outfile:
        for word in list(sortedWordCounts)[:300]:
            outfile.write(word[0] +"\n")
    return tokenizedList

def makeGraph(tokenizedList):
    ##########################Graphing ######################
    uniqueWords=set()
    collectionWordCount=[]
    uniqueWordCount=[]
    numUnique=0
    numSeen=0

    for i in range(len(tokenizedList)):
        if tokenizedList[i] not in uniqueWords:
            numUnique+=1
            uniqueWords.add(tokenizedList[i])
        numSeen+=1
        collectionWordCount.append(numSeen)
        uniqueWordCount.append(numUnique)

    plt.plot(collectionWordCount, uniqueWordCount)
    plt.xlabel("Words in Collection")
    plt.ylabel("Words in Vocabulary")
    plt.title("Vocabulary Growth for Pride and Prejudice")
    plt.show()

if __name__=="__main__":
    partA()
    graphList= partB() ## return type assigned solely for graphing, no relation to tokenizer
    makeGraph(graphList)       

            
            
            
