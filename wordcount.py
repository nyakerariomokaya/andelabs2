def wordcount(str):
    occurences = {}
    words = str.split()
    for i,word in enumerate(words):
        if word.isdigit():
           words[i] = int(word)
    for word in words:
        if word in  occurences:
            occurences[word] +=1
        else:
            occurences[word] = 1
    for key in  occurences:
        if key == '':
           del  occurences[key]
        else: 
           return  occurences
def main():
    return word
main()


