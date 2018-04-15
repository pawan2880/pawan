def lexicographi(s):
    return sorted(sorted(s), key=str.upper)
print(lexicographi('w3resource'))
