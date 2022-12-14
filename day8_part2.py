# data = []
# fileobj=open("day8_input.txt")
# data=fileobj.read().split('\n')
 
# tree_rows = []
 
# for item in data:
#   row_list = []
#   for char in item:
#     row_list.append(int(char))
#   tree_rows.append(row_list) 

# print(len(tree_rows))

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
 
current_index = 1
scenic_scores = []
 
while current_index < len(tree_rows[0]) - 1:
  current_row_number = 1
  for row in tree_rows[1:len(tree_rows) - 1]:
    tree_to_check = row[current_index]
    print("Tree to check: " + str(tree_to_check))
    print("Current index: " + str(current_index))
    print("Current row number: " + str(current_row_number))
    print("Current column: " + str(tree_columns[current_index]))

    column = tree_columns[current_index]
   
    #Check left
    print("Left side: " + str(row[0:current_index]) )
    left_total = 0
    left_split = list(reversed(row[0:current_index]))
    for tree in left_split:
        if tree < tree_to_check:
            left_total += 1
        else:
            left_total += 1
            break
   
    #Check right
    print("Right side: " + str(row[current_index + 1:len(row)]))
    right_total = 0
    right_split = row[current_index + 1:len(row)]
    for tree in right_split:
        if tree < tree_to_check:
            right_total += 1
        else:
            right_total += 1
            break
   
    #Check above
    print("Top side: " + str(column[:current_row_number]))
    top_total = 0
    top_split = list(reversed(column[0:current_row_number]))
    for tree in top_split:
        if tree < tree_to_check:
            top_total += 1
        else:
            top_total += 1
            break
   
    #Check below
    print("Bottom side: " + str(column[current_row_number + 1:len(column)]))
    bottom_total = 0
    bottom_split = column[current_row_number + 1:len(column)]
    for tree in bottom_split:
        if tree < tree_to_check:
            bottom_total += 1
        else:
            bottom_total += 1
            break
    
    print("Right total: " + str(right_total))
    print("Left total: " + str(left_total))
    print("Top total: " +str(top_total))
    print("Bottom total: " + str(bottom_total))
    
    scenic_score = right_total * left_total * top_total * bottom_total
    print("Scenic score: " + str(scenic_score))
    scenic_scores.append(scenic_score)
   
    current_row_number += 1
 
  current_index += 1

print("Checking the perimeter...")

print("Checking the top row...")
#Check top row
top_row_current_index = 0
for tree in tree_rows[0]:
    tree_to_check = tree
    bottom_total = 0
    right_total = 0
    left_total = 0
    top_row_scenic_score = 0

    print("Tree to check: " + str(tree_to_check))

    column = tree_columns[top_row_current_index]
    
    #Check below
    print("Bottom side: " + str(column[1:len(column)]))
    bottom_total = 0
    bottom_split = column[1:len(column)]
    for tree in bottom_split:
        if tree < tree_to_check:
            bottom_total += 1
        else:
            bottom_total += 1
            break

    print("Bottom total: " + str(bottom_total))
    
    if top_row_current_index != len(tree_rows[0]) - 1:
        #Check right
        print("Right side: " + str(tree_rows[0][top_row_current_index + 1:len(tree_rows[0])]))
        right_total = 0
        right_split = tree_rows[0][top_row_current_index + 1:len(tree_rows[0])]
        for tree in right_split:
            if tree < tree_to_check:
                right_total += 1
            else:
                right_total += 1
                break
        
        print("Right total: " + str(right_total))
    
    if top_row_current_index != 0:
        #Check left
        print("Left side: " + str(tree_rows[0][0:top_row_current_index]))
        right_total = 0
        left_split = tree_rows[0][0:top_row_current_index]
        for tree in left_split:
            if tree < tree_to_check:
                left_total += 1
            else:
                left_total += 1
                break
        
        print("Left total: " + str(left_total))
    
    top_row_current_index += 1

    if left_total == 0:
        top_row_scenic_score = bottom_total * right_total
    elif right_total == 0:
        top_row_scenic_score = bottom_total * left_total
    else:
        top_row_scenic_score = bottom_total * right_total * left_total
    
    print("Scenic score: " + str(top_row_scenic_score))
    scenic_scores.append(top_row_scenic_score)

print("Checking the bottom row...")
#Check bottom row
bottom_row_current_index = 0
print("Bottom row: " + str(tree_rows[len(tree_columns) - 1]))
for tree in tree_rows[len(tree_columns) - 1]:
    tree_to_check = tree
    bottom_total = 0
    right_total = 0
    left_total = 0
    bottom_row_scenic_score = 0

    print("Tree to check: " + str(tree_to_check))

    column = tree_columns[bottom_row_current_index]
    
    #Check above
    print("Top side: " + str(column[:len(tree_columns) - 1]))
    top_total = 0
    top_split = list(reversed(column[0:len(tree_columns) - 1]))
    for tree in top_split:
        if tree < tree_to_check:
            top_total += 1
        else:
            top_total += 1
            break
    print("Top total: " + str(top_total))
    
    if bottom_row_current_index != len(tree_rows[0]) - 1:
        #Check right
        print("Right side: " + str(tree_rows[len(tree_columns) - 1][bottom_row_current_index + 1:len(tree_rows[0])]))
        right_total = 0
        right_split = tree_rows[len(tree_columns) - 1][bottom_row_current_index + 1:len(tree_rows[0])]
        for tree in right_split:
            if tree < tree_to_check:
                right_total += 1
            else:
                right_total += 1
                break
        print("Right total: " + str(right_total))

    if  bottom_row_current_index != 0:
        #Check left
        print("Left side: " + str(tree_rows[len(tree_columns) - 1][0:bottom_row_current_index]))
        right_total = 0
        left_split = tree_rows[len(tree_columns) - 1][0:bottom_row_current_index]
        for tree in left_split:
            if tree < tree_to_check:
                left_total += 1
            else:
                left_total += 1
                break
        
        print("Bottom total: " + str(bottom_total))
    
    bottom_row_current_index += 1

    if left_total == 0:
        bottom_row_scenic_score = top_total * right_total
    elif right_total == 0:
        bottom_row_scenic_score = top_total * left_total
    else:
        bottom_row_scenic_score = top_total * right_total * left_total
    
    print("Scenic score: " + str(bottom_row_scenic_score))
    scenic_scores.append(bottom_row_scenic_score)
   
print("Checking the leftmost column...")
#Check leftmost column
left_row_number = 1

for tree in tree_columns[0][1:len(tree_rows) - 1]:
    tree_to_check = tree
    bottom_total = 0
    right_total = 0
    left_side_scenic_score = 0

    print("Tree to check: " + str(tree_to_check))

    #Check right
    print("Right side: " + str(tree_rows[left_row_number][1:len(tree_rows[0])]))
    right_total = 0
    right_split = tree_rows[left_row_number][1:len(tree_rows[0])]
    for tree in right_split:
        if tree < tree_to_check:
            right_total += 1
        else:
            right_total += 1
            break
    
    print("Right total: " + str(right_total))
    
    #Check above
    print("Top side: " + str(tree_columns[0][0:left_row_number]))
    top_total = 0
    top_split = list(reversed(column[0:left_row_number]))
    for tree in top_split:
        if tree < tree_to_check:
            top_total += 1
        else:
            top_total += 1
            break
    
    print("Top total: " + str(top_total))

    #Check below
    print("Bottom side: " + str(tree_columns[0][left_row_number:len(tree_columns[0])]))
    bottom_total = 0
    bottom_split = tree_columns[0][left_row_number:len(tree_columns[0])]
    for tree in bottom_split:
        if tree < tree_to_check:
            bottom_total += 1
        else:
            bottom_total += 1
            break
    
    print("Bottom total: " + str(bottom_total))
    
    left_side_scenic_score = top_total * bottom_total * right_total
    print("Scenic score: " + str(left_side_scenic_score))
    scenic_scores.append(left_side_scenic_score)

print("Checking the rightmost column...")
#Check rightmost column
right_row_number = 1
for tree in tree_columns[len(tree_columns) - 1][1:len(tree_rows) - 1]:
    tree_to_check = tree
    bottom_total = 0
    left_total = 0
    right_side_scenic_score = 0

    print("Tree to check: " + str(tree_to_check))

    #Check left
    print("Left side: " + str(tree_rows[right_row_number][0:len(tree_rows[0]) - 1]))
    left_total = 0
    left_split = tree_rows[right_row_number][0:len(tree_rows) - 1]
    for tree in left_split:
        if tree < tree_to_check:
            left_total += 1
        else:
            left_total += 1
            break
    print("Lefttotal: " + str(left_total))
    
    #Check above
    print("Top side: " + str(tree_columns[len(tree_columns) - 1][0:right_row_number]))
    top_total = 0
    top_split = list(reversed(tree_columns[len(tree_columns) - 1][0:right_row_number]))
    for tree in top_split:
        if tree < tree_to_check:
            top_total += 1
        else:
            top_total += 1
            break
    print("Top total: " + str(top_total))

    #Check below
    print("Bottom side: " + str(tree_columns[len(tree_columns) - 1][right_row_number + 1:len(tree_columns[0])]))
    bottom_total = 0
    bottom_split = tree_columns[0][left_row_number + 1:len(tree_columns[0])]
    for tree in bottom_split:
        if tree < tree_to_check:
            bottom_total += 1
        else:
            bottom_total += 1
            break
    
    print("Bottom total: " + str(bottom_total))
    
    right_row_number += 1

    right_side_scenic_score = top_total * bottom_total * left_total
    print("Scenic score: " + str(right_side_scenic_score))
    scenic_scores.append(right_side_scenic_score)

 
descending_order_scenic_scores = list(reversed(sorted(scenic_scores))) 
print("Descending order scenic scores: " + str(descending_order_scenic_scores))
result = descending_order_scenic_scores[0]
print("Result: " + str(result))