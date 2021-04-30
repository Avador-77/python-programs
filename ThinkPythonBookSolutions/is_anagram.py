def is_anagram(st1, st2):
    match = ""
    for w in st1:
        ind = st2.find(w)
        match += st2[ind]
    if match == st1:
        return True
    else:
        return False

print(is_anagram('part','earth'))