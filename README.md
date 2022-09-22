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

**Libraries**: Only the built-in regex library has been used to filter and identify special patterns in the text. 

**Dependencies**: Since there has been no installation of third-party libraries, no installation is required for dependencies. It is, however, important to note that the code must be run on Python versions. The code was developed on Python 3.9.5 so it is recommended that it best be tested on the same version. However, the re library is supported on almost all Python 3+ versions.

**Building and Running**: The script is able to compile and run through a single command that is
    python main.py
    OR
    python3 main.py




