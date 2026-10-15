def count_words(path):

    file = open(path , 'r')
    
    lines = file.readlines()
    file.close()
    
    wordCount = 0
    for line in lines:
        wordList = line.split(',')
        words = len(wordList)
        wordCount+=words
    
    return wordCount

def count_chars(path):
    file = open(path , 'r')
    lines = file.readlines()
    file.close()

    cherCount = 0
    for line in lines :
        chers = len(line)
        cherCount +=chers
    return cherCount
