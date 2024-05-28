# get sentence from user

original_message = input("Write the message which you want to get changed :").strip().lower()

# split sentence into words
words = original_message.split()

code_words = []

# loop through words and convert to secret code
# if the word starts with vowel, just add "tac" to the end
# Otherwise, move the first consonant cluster to end, and add "az"

for x in words:
    if x[0] in "aeiou":
        code_word = x + "tac"
        code_words.append(code_word)
    else:
        pos_of_vowel = 0
        for letter in x:
            if letter not in "aeiou":
                pos_of_vowel = pos_of_vowel + 1
            else:
                break
        cons = x[:pos_of_vowel]
        the_rest = x[pos_of_vowel:]
        code_word = the_rest + cons + "az"
        code_words.append(code_word)

# stick words back together

code = " ".join(code_words)

# output the final string

print(code)
