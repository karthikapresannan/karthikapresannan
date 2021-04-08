names=["ram","raju","ravi"]
upper_name=list(map(lambda name:name.upper(),names))
print(upper_name)

######

players=[
    {"names":"sachin","matches":500,"rank":11},
    {"names":"aravind","matches":450,"rank":1},
    {"names":"raju","matches":250,"rank":52},
    {"names":"anoop","matches":360,"rank":7},
]

players_name=list(map(lambda dict:dict["names"],players))
print(players_name)

players_rank=list(map(lambda dict:dict["rank"],players))
print(players_rank)

above_300=list(filter(lambda dict:dict["matches"]>300,players))
print(above_300)

max_name=list(map(lambda dict:dict["names"],above_300))
print(max_name)
