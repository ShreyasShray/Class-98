def countWordsFromFile():
    wordCount = 0
    fileName = input("Enter the file name")
    f = open(fileName, "r")
    for line in f:
        words = line.split()
        wordCount = wordCount + len(words)
    print("Number of words: ", wordCount)

countWordsFromFile()