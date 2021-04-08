import json
f=open("covid_19","reg")
dict={}
for lines in f:
    words=lines.rstrip("\n").split(",")
    state=words[3]
    confirmed=int(words[-1])
    deaths=int(words[-2])
    dict[state]={'state':state,'confirmed':confirmed}
    print(json.dumps(json.dumps(dict,indent=4)))
    print(dict['kerala'])