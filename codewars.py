#1 
def dna_to_rna(dna):
    return dna.replace("T", "U")

#2 
def find_average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

#3 
def hero(bullets, dragons):
    return bullets >= dragons * 2

#4 
def square_sum(numbers):
    return sum(x ** 2 for x in numbers)

#5 
def string_to_number(s):
    return int(s)

#6 
def basic_op(operator, value1, value2):
    if operator == '+':
        return value1 + value2
    elif operator == '-':
        return value1 - value2
    elif operator == '*':
        return value1 * value2
    elif operator == '/':
        return value1 / value2

#7 
def count_positives_sum_negatives(arr):
    if not arr:
        return []

    positives = 0
    negatives = 0

    for num in arr:
        if num > 0:
            positives += 1
        elif num < 0:
            negatives += num

    return [positives, negatives]

#8 
def even_or_odd(number):
    return "Even" if number % 2 == 0 else "Odd"

#9 
def better_than_average(class_points, your_points):
    average = (sum(class_points) + your_points) / (len(class_points) + 1)
    return your_points > average

#10 
def maximum(arr):
    return max(arr)

def minimum(arr):
    return min(arr)

#12 
def fake_bin(x):
    result = ""
    for digit in x:
        if int(digit) < 5:
            result += "0"
        else:
            result += "1"
    return result

#13 
def feast(beast, dish):
    return beast[0] == dish[0] and beast[-1] == dish[-1]

#14 
def disemvowel(string):
    result = ""
    for letter in string:
        if letter.lower() not in "aeiou":
            result += letter
    return result

#15 
def count_sheeps(sheep):
    return sheep.count(True)

#16 
def accum(s):
    return "-".join(c.upper() + c.lower() * i for i, c in enumerate(s))

#17 
def get_middle(s):
    mid = len(s) // 2
    if len(s) % 2 == 0:
        return s[mid - 1:mid + 1]
    else:
        return s[mid]

#18 
def are_you_playing_banjo(name):
    if name[0].lower() == "r":
        return name + " plays banjo"
    else:
        return name + " does not play banjo"
