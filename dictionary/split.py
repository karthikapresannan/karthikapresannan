f=open("words", "r")
lst=[]
for lines in f:
    words=lines.rstrip("\n").split(" ")
    for word in words:
     lst.append(word)
for word in lst:
    print(word)
