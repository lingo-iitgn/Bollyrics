f = open("dict_3_standard.json","r")
str_f = f.read()
f.close()

str_f = str_f.replace("\'","\"")

# print(type(str_f))

f = open("dict_3_double.json", "w")
f.write(str_f)
f.close()