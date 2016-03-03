def sortByFavorite(s, fav):
    def comparator(a, b):
        i, j = 0, 0
        while i < len(a) and j < len(b):
            c1, c2 = a[i], b[i]
            if c1 in fav and c2 not in fav:
                return -1
            elif c1 not in fav and c2 in fav:
                return 1
            elif c1 not in fav and c2 not in fav:
                if c1 > c2:
                    return 1
                elif c1 < c2:
                    return -1
                else:
                    i += 1
                    j += 1
            else:
                if fav.index(c1) < fav.index(c2):
                    return -1
                elif fav.index(c1) > fav.index(c2):
                    return 1
                else:
                    j += 1
                    i += 1
        if len(a) == len(b):
            return 0
        elif len(a) < len(b):
            return 1
        else:
            return -1

    return sorted(s, cmp=comparator)

strings = ['animal','duck','snake','zebra','horse','mouse']
favorite = 'zh'

print sortByFavorite(strings, favorite)