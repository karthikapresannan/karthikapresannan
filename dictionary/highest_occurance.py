dict={"hai":2, "hello":3,"how":2}
words=sorted(dict,key=dict.get,reverse=True)
print("sorted values =",words)
