# https://www.codewars.com/kata/552c028c030765286c00007d

def iq_test(numbers):
    num_list = numbers.split(" ")
    evens = []
    odds = []
    for num in num_list:
        if int(num) % 2 == 0:
            evens.append(num)
        else:
            odds.append(num)
    if len(evens) == 1:
        return num_list.index(evens[0]) + 1
    else:
        return num_list.index(odds[0]) + 1