**Project 1**
**Dev Ahuja**

**AB Breakdown**
All code is implemented in main.py. The main method has supporting functions that collectively produce the required output for Parts A and B. The working of the code is explained by comments in the file and the description below
Part A:
    processAbbreviations() takes care of abbreviations in the list that is formed by splitting the initial text file by delimiters except the apostrophe and the period. The period is handled inside this function and three special cases have been defined depending on the type of the abbreviation i.e. Title abbreviation, single letter abbreviations and multi-letter abbreviations. The contractions are handled during the refining of the input in the main function. Words are converted to lowercase after abbreviations have been handled.

    removeStopWords() takes in an inputList, which is the list containing the list of words that need to be filtered and a stopWordList which consists of all stop words that need to be removed from the inputList. The function returns the copy of inputList without the stop words.

    implementStemmerA and implementStemmerB take care of steps 1a and 1b of the Porter Stemmer as mentioned in the textbook. Their working is elaborated in the description section below.

Part B:
    partB() implements the tokenization process for the second text provided to us. Upon receiving the tokenized list, it counts the frequency of each word and ranks them accordingly in the output file.

**Description**:
The project file is divided in such a way that each function defined apart from the main serves to each of the steps of the tokenizer thereby creating a hierarchy of sorts. Part A consists of implementing the skeleton code for a tokenizer which was tested on the given text file. It begins by splitting the string by delimiters except period and apostrophe as they will be handled independently as per requirements. Splitting is conducted using the regex patterns mentioned in the code. Once we have a list void of main punctuations, the code concatenates the apostrophes to combine words instead of splitting them. We then move into the abbreviations. The processAbbreviations method creates a new list in which if the words do not contain a period, they are added without modifications or else they are modified as mentioned below.
Case 1: Abbreviations are of type A.B.C/ 1.2.3. where each period is preceded by a single alphanumeric character. The periods are removed and the letters are joined to make a single string.
Case 2: As specially required for this case, the titles are an edge case given that we cannot split names and titles. That is why in this case, we are combining titles and names and setting the (i+1)st element to None where the ith element is that of the title. This is done to prevent repetition in the resulting array and is accounted for at the beginning of the loop.
Case 3: This is the default case where words like Ph.D. are handled. The period is removed and they are split into two elements in the result array. There is a minor runtime tradeoff in the way that since words cannot be combined, we may have to compromise on runtime to process larger words in this manner. 

Once abbreviations are processed, the resulting list is capable enough to be filtered by stopwords. So, removeStopWords iterates over the list while creating a new one and appends only those words that are not in the stopword file provided to us.

With the stop words removed, the Porter Stemmer steps are executed. implementStemmerA works on basic conditions that check for word suffixes are perform removals and appends accordingly as given in the book. implementStemmerB tends to be one of the more expensive methods of the file as it involves iterating over a few words that require a check on vowel presence. Moreover, the condition for a word being short is also a computationaly complicated algorithm which checks for each of the 4 cases mentioned in the project description by checking patterns of vowels and consonants. 

All steps are supported with documents in the code. 

**Libraries**: Only the built-in regex library has been used to filter and identify special patterns in the text. 

**Dependencies**: Since there has been no installation of third-party libraries, no installation is required for dependencies. It is, however, important to note that the code must be run on Python versions. The code was developed on Python 3.9.5 so it is recommended that it best be tested on the same version. However, the re library is supported on almost all Python 3+ versions.

**Building and Running**: The script is able to compile and run through a single command that is
    python main.py
    OR
    python3 main.py




