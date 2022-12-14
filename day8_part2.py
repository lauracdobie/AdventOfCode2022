data = []
fileobj=open("day8_input.txt")
data=fileobj.read().split('\n')
 
tree_rows = []
 
for item in data:
  row_list = []
  for char in item:
    row_list.append(int(char))
  tree_rows.append(row_list) 
 
column_index = 0
 
tree_columns = []
 
while column_index < len(tree_rows[0]):
  column_list = []
  for row in tree_rows:
    column_list.append(row[column_index])
 
  tree_columns.append(column_list)
  column_index += 1 
 
current_index = 1
scenic_scores = []
 
while current_index < len(tree_rows[0]) - 1:
  current_row_number = 1
  for row in tree_rows[1:len(tree_rows) - 1]:
    tree_to_check = row[current_index]

    column = tree_columns[current_index]
   
    #Check left
    left_total = 0
    left_split = list(reversed(row[0:current_index]))
    for tree in left_split:
        if tree < tree_to_check:
            left_total += 1
        else:
            left_total += 1
            break
   
    #Check right
    right_total = 0
    right_split = row[current_index + 1:len(row)]
    for tree in right_split:
        if tree < tree_to_check:
            right_total += 1
        else:
            right_total += 1
            break
   
    #Check above
    top_total = 0
    top_split = list(reversed(column[0:current_row_number]))
    for tree in top_split:
        if tree < tree_to_check:
            top_total += 1
        else:
            top_total += 1
            break
   
    #Check below
    bottom_total = 0
    bottom_split = column[current_row_number + 1:len(column)]
    for tree in bottom_split:
        if tree < tree_to_check:
            bottom_total += 1
        else:
            bottom_total += 1
            break
    
    scenic_score = right_total * left_total * top_total * bottom_total
    scenic_scores.append(scenic_score)
   
    current_row_number += 1
 
  current_index += 1
 
descending_order_scenic_scores = list(reversed(sorted(scenic_scores))) 
result = descending_order_scenic_scores[0]
print("Result: " + str(result))