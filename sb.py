dictface = {"j1":1, "j2":2, "j3":3, "j4":4, "j5":5}
print(f"{list(dictface.keys())}")
listish = list(dictface.keys())
output = ""
for i in listish:
    output += i + ", "
output = output[:-2]
print(output)