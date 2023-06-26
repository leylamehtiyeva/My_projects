text = "g i i v e t h h i i s m a a a n a g u u n"

split_text = text.split()
print(split_text)
res = []
for i, simbol in enumerate(split_text):
    if i == 0:
        res.append([simbol])
        continue
    if split_text[i] == split_text[i-1]:
        res[len(res)-1].append(simbol)
    else:
        res.append([simbol])

print(res)



print(res)
