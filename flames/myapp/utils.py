def flames(name1,name2):
    name1 = name1.lower().replace(" ","")
    name2 = name2.lower().replace(" ","")
    letters = set(name1) | set(name2)
    count_name = len(name1) + len(name2) -2*len(letters)
    Flames=["friends","love","affection","marriage","enemy","sister"]
    return Flames[count_name%len(Flames)]