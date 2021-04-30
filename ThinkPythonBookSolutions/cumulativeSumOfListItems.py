t = [1,5,3,6,1,2]
res = []
ind = 0
while ind < len(t) - 1:
    for s in t:
        if ind == 0:
            f = t[ind]
            ind += 1
            sec = f
            res.append(sec)
        else:
            sec += t[ind]
            ind += 1
            res.append(sec)
print(res)