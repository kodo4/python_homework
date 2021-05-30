src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# result = [23, 1, 3, 10, 4, 11]
tmp = set()
for i in src:
    if i not in tmp:
        tmp.add(i)
    else:
        tmp.discard(i)
unigue_src = [i for i in src if i in tmp]
print(unigue_src)
