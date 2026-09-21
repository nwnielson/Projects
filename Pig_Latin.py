#Get's input from the user about whether or not they want to make pig latin sentences
#That answer then gets stored, then converting that answer to a boolean
pig_latin_continue = input("Would you like to create a sentence into pig latin? Y/N \n")
if pig_latin_continue.upper() == "Y" :
    pig_latin_loop = True
#Makes for loop to keep asking user if they want to make pig latin sentences
while(pig_latin_loop) :
#If the user did want to make sentences, they are prompted to give a sentence, which is split into a list inlcuding every word in the sentence
    if pig_latin_continue.upper() == "Y" :
        pig_latin_sentence = input("What is the sentence you would like to convert to pig latin? (No punctuation) \n")
        pig_latin_words = pig_latin_sentence.split()
#Loops through each word in the sentence
    for index, pig_latin_word in enumerate(pig_latin_words):
        pig_latin_last_letter = ""
        pig_latin_letter = pig_latin_word[0]

        #Finds puncuation
        pig_latin_last_letter = pig_latin_word[-1]
        if pig_latin_last_letter in ",.?!" :
            pig_latin_word = pig_latin_word[:-1]
        else :
            pig_latin_last_letter = ""

        #Rule for if the word starts with a vowel
        if pig_latin_word.upper().startswith(("A", "E", "I", "O", "U")) :
            pig_latin_word = pig_latin_word + "yay"

        #Rule for if the word starts with a consenant 
        else :
        #Rule for if the word starts with 3 consenants
            if pig_latin_word.upper().startswith(("SCR", "SPL", "SPR", "STR", "SQU", "SHR", "THR", "SCH")) :
                pig_latin_letter = pig_latin_word[:3]
                pig_latin_word = pig_latin_word[3:] + pig_latin_letter + "ay"

            #Rule for if the word starts with 2 consenants
            elif pig_latin_word.upper().startswith(("WH", "PH", "GH", "KN", "WR", "GN", "RH", "PS", "PN", "PT", "MN", "SC", "TS", "CZ", "DJ", "QU", "CH", "ST",
                                                    "SH", "ST", "BL", "BR", "CL", "CR", "DR", "DW", "FL", "FR", "GL", "GR", "PL", 'PR', "SC", "SK", "SL", "SM", 
                                                    "SN", "SP", "SW", "TR", "TW", "TH")) :
                pig_latin_letter = pig_latin_word[:2]
                pig_latin_word = pig_latin_word[2:] + pig_latin_letter + "ay"

            #Rule for if the word starts with only 1 consenant
            else :
                pig_latin_word = pig_latin_word[1:] + pig_latin_letter.lower() + "ay"
        if index == 0 :
            print(pig_latin_word.capitalize() + pig_latin_last_letter, end=" ")
        else :
            print(pig_latin_word.lower() + pig_latin_last_letter, end=" ")
        
        
    #Prompts user for if they want to do another sentence, if so, repeat loop.
    pig_latin_continue = input("\nWould you like to turn another sentence into pig latin? Y/N \n")
    if pig_latin_continue.upper() == "Y" :
        pig_latin_loop = True
    else :
        pig_latin_loop = False

#for char in ",.!?" :
    #text = text.replace(char, f" {char} ")