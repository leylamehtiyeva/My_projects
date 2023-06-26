def chunked(text: str, n: str):
    text = text.split()
    n = int(n)
    res = [[]]
    length_of_res = len(res)
    for simbol in text:
        while length_of_res <= n:
            res.append([simbol])


