def Search(l, x):
    pos = 0
    found = False
    
    while pos < len(l) and not found:
        if l[pos] == x:
            found = True
        else:
            pos = pos + 1
    
    return found, pos

print(Search([11,23,58,31,56,77,43,12,65,19],31))
