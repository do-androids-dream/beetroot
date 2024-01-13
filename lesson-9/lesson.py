l = [1, 0, 0, 2, 0, 0, 3, 4, 0, 0, 0, 5]

for i in l:
    print("element", i)
    #print("index", l.index(i))
    if i == 0:

        l.remove(i)
        l.append(i)
    print(l)