import re
import string

def splitUsingDelimiters(inputStr):
    return re.split('; |, |\*|\n ',inputStr)

def removeNonAlphaNumeric(inputList):
    resList=[]
    for i in range(len(inputList)):
        resList.append(re.sub(r'[^a-zA-Z0-9]', '', inputList[i]))
    return resList

def removeStopWords(alNumList, stopWordList):
    alNumCopy=alNumList
    alNumCopy= [x for x in alNumCopy if x not in stopWordList]
    return alNumCopy

def tokenize(inputList, stopWords):

    alNumList=removeNonAlphaNumeric(inputList)
    tokenizedList=removeStopWords(alNumList, stopWords)
    return tokenizedList

def callback( str ):
    return str.replace('.', '')

def abbreviationMoment(strList):
    for i in range(len(strList)):
        curWord=strList[i].split(".")
        print(curWord)
        if any(len(s)>1 for s in curWord):
            strList[i]=" ".join(curWord)
        else:
            strList[i]=''.join(curWord)
    print(strList)



if __name__=="__main__":
    with open("tokenization-input-part-A.txt", "r") as tokenFile:
        with open("stopwords.txt", "r") as stopWordFile: 

            stopWords=stopWordFile.read().split("\n")                 
            initStr= tokenFile.read() #read Lines
            initList=initStr.split()

            

            # initList=[s.translate(str.maketrans('', '', string.punctuation)) for s in initList]     
            initList=["Ph.D.", "Mr. Bentley"]
            initList=[re.sub(r"(?:[A-Z]\.)+", lambda m: callback(m.group()), x) for x in initList ]
            
    

            


            # initList=[re.sub(r"(?:[a-z]\.)+", lambda m: callback(m.group()), x) for x in initList ]

            # # print(str.translate(str.maketrans('', '', string.punctuation)))
            # str=str.translate(str.maketrans('', '', string.punctuation.replace(".", ""))) # remove all punct except period\
            # strList=str.split()
            # initList=[re.sub(r"(?:[a-zA-Z]\.)+", lambda m: callback(m.group()), x) for x in strList ]
            



            # initStr="Don't U.S.A. in Ph.D A.B.C's"
            # initList=initStr.split()

            # print()
            # initList=[re.sub(r"(?:[A-Z]\.)+", lambda m: callback(m.group()), x) for x in initStr ]
            # initList=[word for line in initList for word in line.split('.')]
            # initList=[word.lower() for word in initList]
 










            

            
            
 

 ##MISC COMMENTS



     # splitList=[]
    # for i in range(len(inputList)):
    #     splitList.append(re.split('; |, |\*|\n',inputList[i]))
    # return splitList

             # print(split)
            # print([x for x in pattern.split(string) if x])
            # inputList=[x.strip() for x in tokenInput.read().split(',')]
            #print(inputList)  

                        #print(splitUsingDelimiters("U.S.A don't 200,000"))


            # newStr=re.sub(r'(?i)(?:^|(?<= ))(?:[a-z]\.)+[a-z]\.?(?= |$)', '', initStr)
            # newStr= re.sub(r"(?<=[a-z]).", "", initStr)
           # newStr= re.sub(r"(?:[A-Z]\.)+", lambda m: callback(m.group()), initStr).lower()
            #print(newStr)

            
            

            # token=tokenize(split, stopWords)
            # print(token)

            
                
