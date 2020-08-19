# https://www.codewars.com/kata/546e2562b03326a88e000020

def square_digits(num):
    squared_digits = ""
    for digit in str(num):
        squared_digits += str(int(digit)**2)
    return int(squared_digits)