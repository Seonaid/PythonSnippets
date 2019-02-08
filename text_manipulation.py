def replace(words, string1, string2):
    new_words = ""
    
    new_strings = words.split(string1)
    new_words = string2.join(new_strings)

    # for letter in words:
    #     if (letter == string1):
    #         new_words = new_words + string2
    #     else:
    #         new_words = new_words + letter

    return new_words