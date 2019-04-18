def edit_distance(s1, s2):
    time = 0
    if(len(s1) != 0):
        if(s1[0] != s2[0]):
            time += 1
        time += edit_distance(s1[1:], s2[1:])
    return time


def subsequence(s1, s2):
    if(len(s1) == 0):
        result = True
    elif(len(s2) == 0):
        result = False
    else:
        if(s1[0] != s2[0]):
            result = subsequence(s1, s2[1:])
        else:
            result = subsequence(s1[1:], s2[1:])
    return result


def perms(s):
    if(len(s) <= 1):
        result = {s}
    else:
        permutation = perms(s[1:])
        result = set()
        char = s[0]
        for perm in permutation:
            for index in range(len(perm) + 1):
                result.add(perm[:index] + char + perm[index:])
    return result
