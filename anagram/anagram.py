def find_anagrams(word, candidates):
    res = []
    for item in candidates:
        if set(item) == set(word):
            res.append(item)
    return res