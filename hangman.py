length_word = int(input("Enter the length of the word:"))
words, word = [], ''.join(['_' for x in range(length_word)])
with open('english.txt', 'r', encoding="utf-8") as wordlist:
    for x in wordlist:
        words.append(x)
possibleWords = [x[:len(x) - 1] for x in words if len(x) == length_word + 1]
while input("Continue? y/n") != "n":
    t = int(input("How many of the same letter do you wanna input?"))
    for j in range(t):
        g, d = input("Right or wrong? r/w"), input("Letter?")
        if g == 'r':
            p = int(input("Position?"))
            word = word[:p - 1] + d.upper() + word[p:]
            possibleWords = [x for x in possibleWords if x[p - 1] == d.upper() and x.count(d.upper()) == t]
        else:
            possibleWords = [x for x in possibleWords if d.upper() not in x]
    print(possibleWords)
