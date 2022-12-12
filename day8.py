data = []
fileobj=open("day8_input.txt")
data=fileobj.read().split('\n')
 
data_tree_rows = []
 
for item in data:
  row_list = []
  for char in item:
    row_list.append(int(char))
  data_tree_rows.append(row_list) 
 
tree_rows = [
[3, 0, 3, 7, 3],
[2, 5, 5, 1, 2],
[6, 5, 3, 3, 2],
[3, 3, 5, 4, 9],
[3, 5, 3, 9, 0]]
 
column_index = 0
 
tree_columns = []
 
while column_index < len(tree_rows[0]):
  column_list = []
  for row in tree_rows:
    column_list.append(row[column_index])
 
  tree_columns.append(column_list)
  column_index += 1
 
exterior = (len(tree_rows) * 2) + (len(tree_columns) * 2) - 4
 
current_index = 1
visible_trees = 0
 
while current_index < len(tree_rows[0]) - 1:
  current_row_number = 1
  for row in tree_rows[1:len(tree_rows) - 1]:
    tree_to_check = row[current_index]

    column = tree_columns[current_index]
   
    #Check left
    left_split = sorted(row[0:current_index])
    end_index = left_split[len(left_split) - 1]
    if end_index < tree_to_check:
      visible_trees += 1
      current_row_number += 1
      continue
   
    #Check right
    right_split = list(reversed(sorted(row[current_index + 1:len(row)])))
    start_index = right_split[0]
    if start_index < tree_to_check:
      visible_trees += 1
      current_row_number += 1
      continue
   
    #Check above
    top_split = sorted(column[0:current_row_number])
    end_top_index = top_split[len(top_split) - 1]
    if end_top_index < tree_to_check:
      visible_trees += 1
      current_row_number += 1
      continue
   
    #Check below
    bottom_split = list(reversed(sorted(column[current_row_number + 1:len(column)])))
    start_bottom_index = bottom_split[0]
    if start_bottom_index < tree_to_check:
      visible_trees += 1
      current_row_number += 1
      continue
   
    current_row_number += 1
 
  current_index += 1
 
result = exterior + visible_trees
print(exterior)
print(visible_trees)
print("Result: " + str(result))