name = { "ritik" : 10 , "ankit" : 20 , "sonam" : 30}
surname = { "pandey" : 40 , " dubey " : 50 , " mishra " : 30}

name.update(surname)
print(name)



name.clear()
print(name)



name.pop("ritik")
print(name)


name.popitem()
print(name)


ritik = { "paise" : 10 , "ruppee" : 20}

ritik.update(paise = 20)