from re import*

# pattern ="a+" #checking for one or morethan a

# pattern="a*" #a+ zero number of a

# pattern="a{2}" #maximum two  numbers

pattern="a{2,3}" #minimum 2 and maximum 3


matcher=finditer(pattern,"aaaaacaaaaaaaabbaab")
for match in matcher:
    print(match.start())
    print(match.group())