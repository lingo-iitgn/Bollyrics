import re, random, math, json
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.lm.preprocessing import pad_both_ends

###### IMPORT DONE ######

f = open("outALL.txt", "r", encoding="utf-8")
text = f.read().lower()
f.close()

text = text.replace("<start> ","").replace(" <end>","")

# print(text)  ###  comment this

sent = text.lower().split("\n")

# print(sent)

temp = [ (word_tokenize(i)+["<end>"]) for i in sent]

tokens = []
for i in temp:
    tokens += i

vocab = set(tokens)

dict1 = { "TOKENS" : [] }

dict1["TOKENS"] = tokens

fp = open("dict_1.json","w+")
# fp = open("check.json","w+")    ###  comment this
json.dump(dict1, fp, sort_keys=True, indent=4)
fp.close()