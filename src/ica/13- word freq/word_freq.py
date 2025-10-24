import string

def compute_frequencies(filename):
    file = open(filename, 'r')  # Opens the file
    line = file.read() #read reads the whole file, whereas readline reads one ife
    print(line)
    words = line.split()
    clean_words=[]
    for word in words:
        newWord = word.strip(string.punctuation)
        clean_words.append(newWord) #Append is how you add to a list
   #print(clean_words)

    word_frequency= {}
    for word in clean_words:
        if word in word_frequency:
            word_frequency[word] = word_frequency[word] + 1
        else:
            word_frequency[word] = 1 # This adds the word to the dictionary, and we are assigning the value

    print(len(word_frequency)) #To see the word count
    print(word_frequency)


compute_frequencies("../TextFiles/alice.txt")





