import re, random, math, json
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.lm.preprocessing import pad_both_ends
###### IMPORT DONE

def train(lst, tokens):
    dict = {}
    for i in lst:
        temp = ["<start>"] + word_tokenize(i) + ["<end>"]
        for j in range(len(temp)-1):
            b,a = temp[j:j+2]
            if a not in dict.keys():
                dict[a]=[]
                # change = []
            dict[a].append(b)
    return dict

f = open("outALL.txt", "r", encoding="utf-8")
text = f.read().lower()
f.close()

text = text.replace("<start> ","").replace(" <end>","")
text = text.replace("<start>","").replace("<end>","")

tokens = word_tokenize(text.lower())
vocab = set(tokens)
print("tokens:")
print(len(tokens))
print("vocab:")
print(len(vocab))
print()

lst = text.lower().split("\n")
total_sen = len(lst)
print(total_sen)

# for i in range(len(lst)):
#     temp = (re.sub(r"\n{1,}"," ",lst[i])).lower()
#     lst[i] = temp

print(len(lst))
dict = train(lst,tokens)

# ### Json problem 
# json_dict = {}
# count = 1
# for k in dict.keys():
#     json_dict["k"+str(count)] = k
#     json_dict["v"+str(count)] = dict[k]
#     count = count+1

# fp = open("dict_2_standard.json","w+")
# json.dump(json_dict, fp)
# fp.close()
# ### JSon problem ends

fp = open("dict_2.json","w+")
json.dump(dict, fp, sort_keys=True, indent=4)
fp.close()


f = open("just_check.txt","w+")
for i in dict.keys():
    f.write(i+" "+str(len(dict[i]))+"\n")
f.close()

unigram = { "tokens": [] }
unigram["tokens"] = tokens

# fp = open("dict_1.json","w+")
# json.dump(unigram, fp, sort_keys=True, indent=4)
# fp.close()

# perp = { "whole_vocab" : []}
# perp["whole_vocab"] = list(vocab)

# fp = open("vocab.json","w+")
# json.dump(perp, fp, sort_keys=True, indent=4)
# fp.close()