# Code for Soundex Algorithm.

def preprocessing(word):
    word = word.lower()
    word = word.replace(" ", "")
    word = word.replace("open", "")
    word = word.replace("alexa", "")
    word = word.replace("play", "")
    
    return word


def eliminate_vowels(word):
    eliminators = "aeiouyhw"
    word_without_eliminators = ""
    for character in word:
        if character not in eliminators:
            word_without_eliminators+=character

    return word_without_eliminators

def eliminate_duplicate_characters(word):

    word_without_duplicate_characters = ""

    index = 0
    length_of_word = len(word)

    while(index<length_of_word):
        temp = word[index]
        word_without_duplicate_characters += temp

        while(index+1<length_of_word and (word[index+1] == word[index])):
            index+=1

        index+=1

    return word_without_duplicate_characters
        
def encode_word(word):
    consonant_dictionary = {
        'b':1,
        'f':1,
        'p':1,
        'v':1,
        'c':2,
        'g':2,
        'j':2,
        'k':2,
        'q':2,
        's':2,
        'x':2,
        'z':2,
        'd':3,
        't':3,
        'l':4,
        'm':5,
        'n':5,
        'r':6
    }

    final_encoded = word[0]
    for index in range(1,len(word)):
        final_encoded+=str(consonant_dictionary[word[index]])

    return final_encoded

def covert_to_soundex_code(word):

    word = preprocessing(word)

    coverted_soundex = word[0]
    word_without_eliminators = eliminate_vowels(word[1:])
    coverted_soundex += word_without_eliminators
    word_without_duplicate_characters = eliminate_duplicate_characters(coverted_soundex)
    phonetic_exp = encode_word(word_without_duplicate_characters)

    if(len(phonetic_exp)>=4):
        phonetic_exp = phonetic_exp[:4]
    else:
        phonetic_exp+= "0"*(4 - len(phonetic_exp))


    return phonetic_exp

def find_similar_innvocators(skill_innvocation_commands):

    dictionary = {}
    print("")    
    for invc in skill_innvocation_commands:
        
        soundex = covert_to_soundex_code(invc)
        print(invc ,"-",soundex)
        if soundex in dictionary:
            dictionary[soundex].append(invc)

        else:
            dictionary[soundex] = [invc]
    print("")
    final = list(dictionary.values())
    print("The similar Commands are as Follows")
    for index in range(len(final)):
        print("{}. {}".format(index+1, final[index]))

    print("")



skill_innvocation_commands = ["Alexa open Ashcroft","Alexa open capital one", "Alexa open bazaar", "Alexa open capital won","Alexa open bizarre","Alexa open Ashcraft"]


find_similar_innvocators(skill_innvocation_commands)


#Capital One - Bank Transactions - Mobile NUmber, Account numbr, details 


#Capital Won  - Alexa Hackers Skill - Instead Complet --> Sending to hacker  

# Voice Squating Works