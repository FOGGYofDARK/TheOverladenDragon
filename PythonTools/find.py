import os

files = os.listdir()
s = input("name?")
flag = -1
for d in range(0,len(files)):
    if (files[d])[-3:] == 'txt':
        with open(files[d], 'r' , encoding = "utf-8") as f1:
            text = f1.read()
            flag = text.find(s)
        if flag != -1:
            print(files[d])
            break
if flag == -1:
    print("not found")
