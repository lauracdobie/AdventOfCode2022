total = 0

test_data = ["2-4,6-8",
"2-3,4-5",
"5-7,7-9",
"2-8,3-7",
"6-6,4-6",
"2-6,4-8"]

for item in test_data:
    lists = item.split(",")

    list_1 = lists[0]
    list_2 = lists[1]

    new_list_1 = []
    new_list_2 = []

    for i in range(int(list_1[0]), int(list_1[2]) +1):
        new_list_1.append(i)

    print(new_list_1)

    for i in range(int(list_2[0]), int(list_2[2]) +1):
        new_list_2.append(i)

    print(new_list_2)

    if new_list_1[len(new_list_1) - 1] >= new_list_2[len(new_list_2) -1] and new_list_1[0] <= new_list_2[0]:
        print("One list contains the other")
        total += 1

    elif new_list_2[len(new_list_2) - 1] >= new_list_1[len(new_list_1) -1] and new_list_2[0] <= new_list_1[0]:
        print("One list contains the other - second statement")
        total += 1

    else:
        print("One list does not contain the other")

print("End total: " + str(total))
