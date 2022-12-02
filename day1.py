from functools import reduce

data = []
fileobj=open("day1_input.txt")
data=fileobj.read().split('\n')

size = len(data)
idx_list = [idx + 1 for idx, val in
            enumerate(data) if val == '']
  
  
list_of_sublists = [data[i: j] for i, j in
        zip([0] + idx_list, idx_list + 
        ([size] if idx_list[-1] != size else []))] 

cleaned_data = []

for list in list_of_sublists:
    for item in list:
        if item == '':
            list.remove(item)
    cleaned_data.append(list) 

list_totals = []

for list in cleaned_data:
    total = 0
    for item in list:
        value_to_add = int(item)
        total += value_to_add
    list_totals.append(total)

sorted_list = sorted(list_totals)

print(sorted_list)

index1 = len(sorted_list) - 1
index2 = len(sorted_list) - 2
index3 = len(sorted_list) - 3

end_total = (sorted_list[index1] + sorted_list[index2] + sorted_list[index3])
print(end_total)