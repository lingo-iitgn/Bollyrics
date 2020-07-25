import re, random, math, json
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.lm.preprocessing import pad_both_ends
###### IMPORT DONE

def train(lst, tokens):
    dict = {}
    for i in lst:
        temp = ["<start>"] + word_tokenize(i) + [r"<end>"]*2
        for j in range(len(temp)-2):
            c,a,b = temp[j:j+3]
            if tuple([a,b]) not in dict.keys():
                dict[tuple([a,b])]=[]
                # change number of _unk_
                # dict[a] = []
            dict[tuple([a,b])].append(c)
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
# lst = sent_tokenize(text) #### wont work in this case
total_sen = len(lst)
# train_data_len = int(len(lst)*(8/10))
print(total_sen)

# for i in range(len(lst)):
#     temp = (re.sub(r"\n{1,}"," ",lst[i])).lower()
#     lst[i] = temp

print(len(lst))
dict = train(lst, tokens)




### Json problem 
json_dict = {}
count = 1
for k in dict.keys():
    json_dict["k"+str(count)] = list(k)
    json_dict["v"+str(count)] = dict[k]
    count = count+1

fp = open("dict_3_standard.json","w+")
json.dump(json_dict, fp)
fp.close()
### JSon problem ends


# fp = open("dict_3.json","w+")
# fp.write(str(dict))
# fp.close()


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