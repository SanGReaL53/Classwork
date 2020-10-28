def remove_palindroms(spells):
    bw = []
    for x in spells:
        word = x.replace(' ', '')
        word = word.lower()
        if word == word[::-1]:
            bw.append(x)
    for word in bw:
        spells.remove(word)
        
