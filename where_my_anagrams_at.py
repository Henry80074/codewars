def anagrams(word, words):
    solved = []
    for i in words: 
        sort = sorted(i)
        if sort == sorted(word):
            solved.append(i)
    return solved
