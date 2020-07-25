import re, random, math, json
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.lm.preprocessing import pad_both_ends
###### IMPORT DONE

def train(lst, tokens):
    dict = {}
    dict["<UNK>"] = tokens + [r"<\s>"]*len(lst)
    for i in lst:
        temp = ["<s>"]*3 + word_tokenize(i) + [r"<\s>"]
        for j in range(len(temp)-3):
            a,b,c,d = temp[j:j+4]
            if tuple([a,b,c]) not in dict.keys():
                dict[tuple([a,b,c])]=["<UNK>"]*3
                # change number of _unk_
                # dict[a] = []
            dict[tuple([a,b,c])].append(d)
    return dict

f = open("speeches.txt", "r", encoding="utf-8")
text = f.read().lower()
f.close()

tokens = word_tokenize(text.lower())
tokens = tokens + int((15/100)*len(tokens))*["<UNK>"] 
vocab = set(tokens)
print("tokens:")
print(len(tokens))
print("vocab:")
print(len(vocab))
print()

lst = sent_tokenize(text)
total_sen = len(lst)
train_data_len = int(len(lst)*(8/10))
print(total_sen, train_data_len)

for i in range(len(lst)):
    temp = (re.sub(r"\n{1,}"," ",lst[i])).lower()
    lst[i] = temp

print(len(lst))
dict = train(lst[:train_data_len],tokens)

fp = open("dict_4.json","w+")
fp.write(str(dict))
fp.close()


f = open("just_check.txt","w+")
for i in dict.keys():
    f.write(str(i)+" "+str(len(dict[i]))+"\n")
f.close()

# unigram = { "tokens": [] }
# unigram["tokens"] = tokens

# fp = open("dict_1.json","w+")
# json.dump(unigram, fp, sort_keys=True, indent=4)
# fp.close()

# perp = { "whole_vocab" : []}
# perp["whole_vocab"] = list(vocab)

# fp = open("vocab.json","w+")
# json.dump(perp, fp, sort_keys=True, indent=4)
# fp.close()