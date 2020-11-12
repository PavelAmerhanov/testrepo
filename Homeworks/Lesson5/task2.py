with open("5-2.txt", encoding="utf-8") as f_obj:
    i = 0
    for line in f_obj:
        i += 1
        print(len([x for x in line.split()]))
print(i)
