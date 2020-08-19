# https://www.codewars.com/kata/55b42574ff091733d900002f

def friend(x):
    real_friends = []
    for name in x:
        if len(name) == 4:
            real_friends.append(name)
    return real_friends