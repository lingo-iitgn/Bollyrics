### only dict_3 has tuples => key,val => 
import random, json, math


def Rand(start, end, num): 
    counter = 0
    list_rand = []
    new = 0
    while(counter < num):
        new = random.randint(start, end-1)
        if new not in list_rand:
            list_rand.append(new)
            counter = counter + 1
    return(list_rand)

# from demjson import decode

dicttemp = {}

fp = open("dict_3_standard.json","r")
# str_dict = fp.read()
dict3 = json.load(fp)
# dict3 = decode(str_dict)
# print("dict3 loaded")
fp.close()

count = 1
maxima = max([int(i[1:]) for i in dict3.keys()])
# print(maxima)
while(True):
    if count<maxima:
        dicttemp[tuple(dict3["k"+str(count)])] = dict3[("v"+str(count))]
        count = count +1
    else:
        # print("dict3 - ",str(count))
        dict3 = dicttemp
        dicttemp = {}
        break

fp = open("dict_1.json","r")
# str_dict = fp.read()
dict1 = json.load(fp)
# print("dict1 loaded")
fp.close()

fp = open("dict_2.json","r")
# str_dict = fp.read()
dict2 = json.load(fp)
# print("dict2 loaded")
fp.close()



### rhyme deciding start


stanza = 4              ##### stanza length #####
r_scheme = input()
# print(r_scheme)

types = list(set(i for i in r_scheme))


### rhyme deciding start


temp_list = []
fp = open("rhymes.json","r")
# str_dict = fp.read()
temp_list = json.load(fp)
# print("RHYMES loaded")
fp.close()

new_keys = [i for i in temp_list.keys() if len(temp_list[i])>=stanza]
# print("c1")
# print(new_keys)
# print("check2")
randlist = Rand(0,len(new_keys),len(types))

n_dict_for_rhyme = {}
c=0
for i in types:
    n_dict_for_rhyme[i] = new_keys[randlist[c]]
    c = c + 1

main_dic_for_rhyme = {}
for i in types:
    main_dic_for_rhyme[i] = []
    for j in (Rand(0,len(temp_list[n_dict_for_rhyme[i]]),stanza)):
        main_dic_for_rhyme[i].append(temp_list[n_dict_for_rhyme[i]][j])


rhyme = []
for i in range(stanza):
    for j in r_scheme:
        rhyme.append(main_dic_for_rhyme[j][i])
    rhyme.append(" ")



### rhyme deciding ends



sum_of_log = 0
total_pred = 0

for i in rhyme:
    if i!= " ":
        j = (i.split())[0:2]
        ### last word prob ###
        deno = len(dict2["<end>"])
        num = dict2["<end>"].count(j[1])
        print(math.log(num/deno))
        sum_of_log -= math.log(num/deno)
        total_pred += 1
        ### second last word prob ###
        deno = len(dict3[tuple([j[1],"<end>"])])
        num = dict3[tuple([j[1],"<end>"])].count(j[0])
        print(math.log(num/deno))
        sum_of_log -= math.log(num/deno)
        total_pred += 1

print(math.exp(sum_of_log/total_pred))


### perplex for rhyme ending ends ###


sent_sum_of_log = 0
sent_total_pred = 0

poem = []
final = []
for i in rhyme:
    if i==" ":
        poem.append(" ")
    else:
        while(True):
            if len(final)>5 and len(final)<11:
                poem.append( (" ").join(final) )
                final = []
                sum_of_log -= sent_sum_of_log 
                total_pred += sent_total_pred 
                break
            else:
                sent_sum_of_log = 0
                sent_total_pred = 0
                previous = (i.split())[0:2]
                final = previous
                # print(previous[0],previous[1], end=" ")
                predicted = ""
                check= []
                while(True):
                    if predicted == "<start>":
                        break
                    if tuple(previous) in dict3.keys():
                        # print(3,end=" ") 
                        predicted = random.choice(dict3[tuple(previous)])
                        # print("tri")
                        deno = len(dict3[tuple(previous)])
                        num = dict3[tuple(previous)].count(predicted)
                        print(math.log(num/deno))
                        sent_sum_of_log += math.log(num/deno)
                        sent_total_pred += 1
                    elif previous[1] in dict2.keys():
                        # print(2,end=" ")
                        predicted = random.choice(dict2[previous[1]])
                        # print("bi")
                    else:
                        # print(1,end=" ")
                        predicted = random.choice(dict1["TOKENS"])
                        # print("uni")
                    # print(predicted, end=" ")
                    check=check+[previous]
                    previous = [predicted , previous[0]]
                    final = [predicted] + final
                # print("\n - final line ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----")
            

for i in poem:
    print(i) 


print(" Perplexity of Song:- ")
print(math.exp(sum_of_log/total_pred))