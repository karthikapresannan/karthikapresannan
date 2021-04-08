from re import *
pattern="ab"
source="ababababaabba"
matcher=finditer(pattern,source)
cnt=0
for match in matcher:
    print(match.start()) #means stating postion 0
    print(match.group()) #grouping pattern "ab"
    cnt+=1
print(cnt)
#



from re import *
pattern="ab"
#pattern= "\W" #special charcater
#from re import *
#pattern='[ab]'
#pattern='[abc]'
# pattern='[a-z]' #checking the lower case
# pattern='[A-Z]' #checking the upper case
# pattern='[a-zA-Z]'#checking the upper and lower case
# pattern='[0-9]' #checking the digits
# pattern='[a-zA-Z0-9]' #upper,lower,digit
#pattern='[^0-9]' #expect 0 to 9
# pattern="[^0-9a-zA-Z]" #for fnding special symbols
# pattern="\s" #space
# pattern='\d'#checking digits
#pattern="\D " #[^0-9]
# pattern= "\w" #[a-zA-Z0-9] All words

source="a2@_12k"
matcher=finditer(pattern,source)
cnt=0
for match in matcher:
    print(match.start()) #means stating postion 0
    print(match.group()) #grouping pattern "ab"
    cnt+=1
print(cnt)
