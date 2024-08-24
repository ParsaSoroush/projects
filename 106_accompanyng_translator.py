n = int(input())


dictionary = {}


for _ in range(n):
    words = input().split()
    english, french, german, persian = words[1], words[2], words[3], words[0]
    dictionary[english] = persian
    dictionary[french] = persian
    dictionary[german] = persian

sentence = input().split()


if sentence[0].lower() == 'i':
    language = 'english'
elif sentence[0].lower() == 'je':
    language = 'french'
elif sentence[0].lower() == 'ich':
    language = 'german'

translated_sentence = []
for word in sentence:
    if language == 'english':
        if word in dictionary:
            translated_sentence.append(dictionary[word])
        else:
            translated_sentence.append(word)
    else:
        translated_sentence.append(word)

print(' '.join(translated_sentence))