
def largeGroupPositions(s):
    res = []
    hash_char = {}
    i = 0
    start = 0
    end = 1
    while end < len(s):
        if s[end] == s[start]:
            end += 1
        if end - start >= 2:
            res.append([start, end])
        start = end
        end += 1
    return res


s = "abbxxxxzzy"

print(largeGroupPositions(s))


