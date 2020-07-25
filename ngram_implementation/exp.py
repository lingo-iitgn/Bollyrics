import json
import random

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

stanza = 4              ##### stanza length #####
r_scheme = input("Input rhyme scheme:- ")
print(r_scheme)

types = list(set(i for i in r_scheme))


### rhyme deciding start


temp_list = []
fp = open("rhymes.json","r")
# str_dict = fp.read()
temp_list = json.load(fp)
print("RHYMES loaded")
fp.close()

new_keys = [i for i in temp_list.keys() if len(temp_list[i])>=stanza]
print("c1")
print(new_keys)
print("check2")
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
    for j in types:
        rhyme.append(main_dic_for_rhyme[j][i])

#### ends ####

print(rhyme)