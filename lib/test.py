def score(o):


    f = s = 0

    # Following formula from Leggio et al., 2008
    for i, n in enumerate(o):
        if n == o[-1]:
            if n == o[i - 1] + 1: s+=1
        elif i == 0:
            if n == o[i + 1] - 1: s+=1
        elif o[i-1] and o[i+1]:
            if n == o[i - 1] + 1 or n == o[i + 1] - 1: s+=1

    for i, n in enumerate(o):
        if o[i] == o[0]:
            pass
        elif i != 5:
            if o[i] == o[i - 1] + 1 and o[i] != o[i + 1] -1:
                f+=1
        elif i == 5 and o[i] == o[i - 1] + 1:
            f+=1
        else:
            pass

    score = float(s - f)/5

    print(score, s, f)

score([4, 2, 3, 1, 6, 5])
