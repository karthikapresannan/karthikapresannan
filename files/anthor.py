ft=open("teams","r")
fd=open("drops")
def get_team_set(f):
    st=set()
    for lines in f:
        st.add(lines.rstrip("\n"))
    return st
st1=get_team_set(ft)
st2=get_team_set(fd)

qualifier=st1-st2
print(qualifier)