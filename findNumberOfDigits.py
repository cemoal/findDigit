# Basamak sayısını bulan fonksiyon(function to find the number of digits)
import math
from math import log10
def findDigit(number):
    if number == 0:
        return 1
    elif number < 0:
        return findDigit(-number)
    else:
        return int(log10(number)) + 1



print("Please enter a number to find its digit count:")
sayi = int(input())
print("digit count:")
print(findDigit(sayi))  # Calling the function to find the digit count

