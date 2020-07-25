### only dict_3 has tuples => key,val => 
import random 

def Rand(start, end, num): 
    res = [random.randint(start, end) for j in range(num)]
    return res 

import random, json
# from demjson import decode

dicttemp = {}

fp = open("dict_3_standard.json","r")
# str_dict = fp.read()
dict3 = json.load(fp)
# dict3 = decode(str_dict)
print("dict3 loaded")
fp.close()

count = 1
maxima = max([int(i[1:]) for i in dict3.keys()])
print(maxima)
while(True):
    if count<maxima:
        dicttemp[tuple(dict3["k"+str(count)])] = dict3[("v"+str(count))]
        count = count +1
    else:
        print("dict3 - ",str(count))
        dict3 = dicttemp
        dicttemp = {}
        break
        
f = open("check.json","w+")
f.write(str(dict3))
f.close()


fp = open("dict_1.json","r")
# str_dict = fp.read()
dict1 = json.load(fp)
print("dict1 loaded")
fp.close()

fp = open("dict_2_double.json","r")
# str_dict = fp.read()
dict2 = json.load(fp)
print("dict2 loaded")
fp.close()

stanza = int(input("number of stanza: "))

poem = []
final = []


### choose A/B ###

temp_list = []
fp = open("rhymes.json","r")
# str_dict = fp.read()
temp_list = json.load(fp)
print("RHYMES loaded")
fp.close()

new_keys = [i for i in temp_list.keys() if len(temp_list[i])>=stanza]
randlist = list(set(Rand(0,len(new_keys),40)))

a = new_keys[randlist[0]]
b = new_keys[randlist[1]]

rhyme = []
for i in range(stanza):
    rhyme.append(temp_list[a][i])
    rhyme.append(temp_list[b][i])

#### choose A/B ends ####



for i in rhyme:
        while(True):
            if len(final)>5 and len(final)<11:
                poem.append( (" ").join(final) )
                final = []
                break
            else:
                previous = (i.split())[0:2]
                final = previous
                print(previous[0],previous[1], end=" ")
                predicted = ""
                check= []
                while(True):
                    if predicted == "<start>":
                        break
                    if tuple(previous) in dict3.keys():
                        # print(3,end=" ") 
                        predicted = random.choice(dict3[tuple(previous)])
                        print("tri")
                    elif previous[1] in dict2.keys():
                        # print(2,end=" ")
                        predicted = random.choice(dict2[previous[1]])
                        print("bi")
                    else:
                        # print(1,end=" ")
                        predicted = random.choice(dict1["TOKENS"])
                        print("uni")
                    print(predicted, end=" ")
                    check=check+[previous]
                    previous = [predicted , previous[0]]
                    final = [predicted] + final
                print("\n - final line ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----")
                

for i in poem:
    print(i) 