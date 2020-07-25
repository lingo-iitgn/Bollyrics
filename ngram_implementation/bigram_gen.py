import random, json

with open('dict_2.json', 'r') as fp:
    dict = json.load(fp)

predicted = "<s>"
print(predicted, end=" ")
while(True):
    if predicted == r"<\s>":
        break
    predicted = random.choice(dict[predicted])
    print(predicted, end=" ")