moves = []
fileobj=open("day5_input.txt")
moves=fileobj.read().split('\n')

test_moves = ["move 1 from 2 to 1",
"move 3 from 1 to 3",
"move 2 from 2 to 1",
"move 1 from 1 to 2"]
 
one = ["H", "R", "B", "D", "Z", "F", "L", "S"]
two = ["T", "B", "M", "Z", "R"]
three = ["Z", "L", "C", "H","N", "S"]
four = ["S", "C", "F", "J"]
five = ["P", "G", "H", "W", "R", "Z", "B"]
six = ["V", "J", "Z", "G", "D", "N", "M", "T"]
seven = ["G", "L", "N", "W", "F", "S", "P", "Q"]
eight = ["M", "Z", "R"]
nine = ["M", "C", "L", "G", "V", "R", "T"]
 
lists = {"1": one, "2": two, "3": three, "4": four, "5": five, "6": six, "7": seven, "8": eight, "9": nine}
 
def move_crates(number_to_move, from_list, to_list):
    intermediate_list = []
    while number_to_move > 0:
        item = from_list[len(from_list) - 1]
        intermediate_list.append(item)
        from_list.pop(len(from_list) - 1)
        number_to_move -= 1
  
    for item in list(reversed(intermediate_list)):
        to_list.append(item)
 
for move in moves:
    move_list = move.split(" ")
    move_crates(int(move_list[1]), lists[move_list[3]], lists[move_list[5]])

result = one[len(one) - 1] + two[len(two) -1] + three[len(three) - 1] + four[len(four) - 1] + five[len(five) - 1] + six[len(six) - 1] + seven[len(seven) - 1] + eight[len(eight) - 1] + nine[len(nine) - 1]

print(result)