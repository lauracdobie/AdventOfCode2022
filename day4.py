total = 0

test_data = ["2-4,6-8",
"2-3,4-5",
"5-7,7-9",
"2-8,3-7",
"6-6,4-6",
"2-6,4-8"]

data = []
fileobj=open("day4_input.txt")
data=fileobj.read().split('\n')

for item in data:
    lists = item.split(",")

    list_1 = lists[0].split("-")
    list_2 = lists[1].split("-")

    new_list_1 = []
    new_list_2 = []

    for i in range(int(list_1[0]), int(list_1[1]) +1):
        new_list_1.append(i)

    for i in range(int(list_2[0]), int(list_2[1]) +1):
        new_list_2.append(i)

    if new_list_1[len(new_list_1) - 1] >= new_list_2[len(new_list_2) -1] and new_list_1[0] <= new_list_2[0]:
        total += 1

    elif new_list_2[len(new_list_2) - 1] >= new_list_1[len(new_list_1) -1] and new_list_2[0] <= new_list_1[0]:
        total += 1

print("End total: " + str(total))
