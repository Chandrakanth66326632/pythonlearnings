w1 = input("Enter a word1: ")
w2 = input("Enter a word2: ")
w3 = input("Enter a word3: ")

#concatenating
w4 = w1+" "+w2+" "+w3
print("Concatenated word:" , w4)

#substring
w5 = w4[1:6]
print("Substring of the word :" , w5)

#printing each letter with its index
index = 0
while index < len(w1):
    for letter in w1:
        print(index,letter)
        index= index +1



#length of full word
length = len(w4)
print("length of the word :" , length)

#capitalizing
small = w4.lower()
print(small)

upper = w4.upper()
print(upper)

#searching a letter in a word
search = "dra"
pos = w4.find(search)
print("Position of the word is  : ", pos)

#search and replace
newword = w4.replace("Chary", "Chari")
print("New word is :", newword)

#removing the spaces
spaceless= w4.strip()
print("Word without spaces:", spaceless)

#to check for any prefixex
pfx= w4.startswith("Cha")
print(pfx)

#parsing and extracting something from a sentence
email= input("Enter your maild id with junk :")
atpos = email.find("@")
sppos = email.find(" ", atpos)
extword = email[atpos+1 : sppos]
print("Extracted word is :", extword)

