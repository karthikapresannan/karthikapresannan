st={}
print(type(st))

st=()
print(type(st))

st={10,20,"hello",30,40}
print(type(st))

st={10,20,"hello",30,40}
str={100,200}
st.update(str) #adding new numbers in the set
print(st)




st={10,20,30,30,40,40} #duplicate does not print in the set
print(st)

st1={10,11,12,13}
st2={10,11,300}

unionset=st.union(st2)
print(unionset)

intersectionset=st.intersection(st2)
print(intersectionset)

diffset=st.difference(st2)
print(diffset)