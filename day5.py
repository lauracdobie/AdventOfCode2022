moves = ["move 1 from 2 to 1",
"move 3 from 1 to 3",
"move 2 from 2 to 1",
"move 1 from 1 to 2"]
 
one=["Z", "N"]
two=["M", "C", "D"]
three=["P"]
 
lists = {"1": one, "2": two, "3": three}
 
def move_crates(number_to_move, from_list, to_list):
  while number_to_move > 0:
    item = from_list[len(from_list) - 1]
    to_list.append(item)
    from_list.pop(len(from_list) - 1)
    number_to_move -= 1
 
for move in moves:
  move_list = move.split(" ")
  move_crates(int(move_list[1]), lists[move_list[3]], lists[move_list[5]])
 
print(one)
print(two)
print(three)

result = one[len(one) - 1] + two[len(two) -1] + three[len(three) - 1]

print(result)