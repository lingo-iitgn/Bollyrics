import ast 
import random, json

fp = open("dict_4.json","r")
str_dict = fp.read()
fp.close()
dict4 = ast.literal_eval(str_dict)

fp = open("dict_3.json","r")
str_dict = fp.read()
fp.close()
dict3 = ast.literal_eval(str_dict)

fp = open("dict_2.json","r")
str_dict = fp.read()
fp.close()
dict2 = ast.literal_eval(str_dict)

previous = ["<s>"]*3
print(previous[0],previous[1],previous[2], end=" ")
predicted = ""
used_gram = []
while(True):
    if predicted == r"<\s>":
        break
    if tuple(previous) in dict4.keys():
        # print(4,end=" ")
        used_gram.append(4)
        predicted = random.choice(dict4[tuple(previous)])
    elif tuple(previous[1:]) in dict3.keys():
        # print(3,end=" ")
        used_gram.append(3)
        predicted = random.choice(dict3[tuple(previous[1:])])
    elif previous[2] in dict2.keys():
        # print(2,end=" ")
        used_gram.append(2)
        predicted = random.choice(dict2[previous[2]])
    else:
        # print(1,end=" ")
        used_gram.append(1)
        predicted = random.choice(dict2["<UNK>"])
    print(predicted, end=" ")
    previous = [previous[1] , previous[2] , predicted]

print(used_gram)