def reverse_words(Sentence):
    
    list1 = Sentence.split(" ")

    new_word_list = [word[::-1] for word in list1]
    
    
    str = " ".join(new_word_list)
    return str

str1 = "My Name is Parsa"
print(reverse_words(str1))