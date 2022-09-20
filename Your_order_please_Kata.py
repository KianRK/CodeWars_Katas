def order(sentence):
    if sentence == "":                              #if sentence is an empty string return empty string
        return ""
    words = sentence.split()                        #split sentence in list of single words
    new_sentence = [i for i in range(len(words))]   #create new list the same size as words
    for word in words:                              #if number occurs in word of words assign the word to the index of new_sentence
        for n in range(len(words)):
            if str(n+1) in word:
                new_sentence[n] = word

    return ' '.join(new_sentence)

# task description:
# Your task is to sort a given string. Each word in the string will contain a single number. This number is the position the word should have in the result.
#
# Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).
#
# If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.
