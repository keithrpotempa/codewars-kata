# https://www.codewars.com/kata/585d7d5adb20cf33cb000235

def find_uniq(arr):
    for val in set(arr):
        if arr.count(val) == 1:
            return val