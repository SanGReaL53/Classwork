def remove_palindroms(spells):
    for x in spells:
        z = x
        z = z.lower()
        z = z.replace(' ','')
        if z == z[::-1]:
            spells.remove(x)
