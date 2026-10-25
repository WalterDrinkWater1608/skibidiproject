firstinput = input("Nhập 1 câu: ")
sentence = firstinput.strip().lower()
length = len(sentence)
wordlist = sentence.split()
words = len(wordlist)
a = 0
vowels = 0
numbersinsentence = 0
while a != length:
    if sentence[a].isdigit():
        numbersinsentence += 1
    if sentence[a] == "u" or sentence[a] ==  "o" or sentence[a] ==  "a" or sentence[a] ==  "i" or sentence[a] ==  "e":
        vowels += 1
    a += 1
print(f"Length: {length}\nWords: {words}\nVowels: {vowels}\nNumbers: {numbersinsentence}")