import re,json
file = open('outALL.txt','r')
lines = file.read().split("\n")
file.close()

lst = []
for i in lines:
    match = re.search(r'(.{5}) <end>',i)
    word = re.search(r'([^\s]* [^\s]*) <end>',i)
    try:
        lst.append([match.group(1), word.group(1)])
    except:
        pass

diction = {}
for i in lst:
    if i[0] not in diction.keys():
        diction[i[0]] = [0,[]]
    diction[i[0]][0]+=1
    diction[i[0]][1].append(i[1])

out = []



imp = {}
for i in sorted(list(set([z[0] for z in diction.values()]))):
    if i>400:
        for j in diction.keys():
            if diction[j][0]==i:
                imp[j] = diction[j]
# print(imp)

temp_list={}

for i in imp.keys():
    temp_list[i] = []    
    sett = sorted(list(set(imp[i][1])))
    if i!=' mein' and i!=' main':
        temp_list[i] = [(j+" _ "+str(diction[i][1].count(j))) for j in sett if diction[i][1].count(j)>39]

sett = sorted(list(set(imp[" main"][1])))
temp_list["ME"] = [(j+" _ "+str(diction[' main'][1].count(j))) for j in sett if diction[' main'][1].count(j)>39]
sett = sorted(list(set(imp[" mein"][1])))
temp_list["ME"] = temp_list["ME"] + [(j+" _ "+str(diction[' mein'][1].count(j))) for j in sett if diction[' mein'][1].count(j)>39]

f = open('rhymes.json','w+',encoding='utf-8')
json.dump(temp_list, f, indent=4)
f.close()