# https://www.codewars.com/kata/517abf86da9663f1d2000003

def to_camel_case(text):
    lst = list(text)
    for letter in lst:
        if letter == "-" or letter == "_":
            lst[lst.index(letter)+1] = lst[lst.index(letter)+1].upper()
            lst.remove(letter)
    text = "".join(lst)
    return text