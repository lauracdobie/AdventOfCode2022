test_data = ["vJrwpWtwJgWrhcsFMMfFFhFp",
"jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
"PmmdzqPrVvPwwTWBwg",
"wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
"ttgJtRGJQctTZtZT",
"CrZsJsPPZsGzwwsLwLmpwMDw"]

data = []
fileobj=open("day3_input.txt")
data=fileobj.read().split('\n')

priorities = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26,
    "A": 27,
    "B": 28,
    "C": 29,
    "D": 30,
    "E": 31,
    "F": 32,
    "G": 33,
    "H": 34,
    "I": 35,
    "J": 36,
    "K": 37,
    "L": 38,
    "M": 39,
    "N": 40,
    "O": 41,
    "P": 42,
    "Q": 43,
    "R": 44,
    "S": 45,
    "T": 46,
    "U": 47,
    "V": 48,
    "W": 49,
    "X": 50,
    "Y": 51,
    "Z": 52,
}

total = 0

for item in data:
    midpoint = int(len(item)/2)
    s1 = item[0:midpoint]
    s2 = item[midpoint: int(len(item))]
    common_letter_list=list(set(s1)&set(s2))
    number_to_add = priorities[common_letter_list[0]]

    total += number_to_add

print(total)

new_total = 0

list_of_lists = []

for i in range(0, len(data), 3):
    list_of_lists.append(data[i:i+3])

for item in list_of_lists:
    common_letter_list = list(set(item[0])&set(item[1])&set(item[2]))
    number_to_add = priorities[common_letter_list[0]]

    new_total += number_to_add

print(new_total)

test_data = ["vJrwpWtwJgWrhcsFMMfFFhFp",
"jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
"PmmdzqPrVvPwwTWBwg"]

test_letter_list = list(set(test_data[0])&set(test_data[1])&set(test_data[2]))

print(priorities[test_letter_list[0]])

test_data_2 = ["wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
"ttgJtRGJQctTZtZT",
"CrZsJsPPZsGzwwsLwLmpwMDw"]

test_letter_list_2 = list(set(test_data_2[0])&set(test_data_2[1])&set(test_data_2[2]))

print(priorities[test_letter_list_2[0]])


