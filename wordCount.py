def CountWordsFromFile():
    file_name=input("Enter the file name:")
    file=open(file_name,"r")
    number_of_words=0
    for line in file:
        words=line.split()
        number_of_words=number_of_words + len(words)
    print(number_of_words)


CountWordsFromFile()