data = []
fileobj=open("day2_input.txt")
data=fileobj.read().split('\n')

list_of_lists = []

for item in data:
    list = []
    list.append(item[0])
    list.append(item[2])
    list_of_lists.append(list)

 
def calculate_score(p1, p2):
    score = 0
   
    if p2 == "X":
        score += 1
    if p2 == "Y":
        score += 2
    if p2 == "Z":
        score += 3
       
    if p2 == "X" and p1 == "A":
        score += 3
   
    if p2 == "X" and p1 == "C":
        score += 6
       
    if p2 == "Y" and p1 == "A":
        score += 6
   
    if p2 == "Y" and p1 == "B":
        score += 3
   
    if p2 == "Z" and p1 == "B":
        score += 6
   
    if p2 == "Z" and p1 == "C":
        score += 3
       
    return score

def calculate_new_score(p1, p2):
    score = 0
       
    if p2 == "X" and p1 == "A":
        score += 3
    
    if p2 == "X" and p1 == "B":
        score += 1
    
    if p2 == "X" and p1 == "C":
        score += 2
       
    if p2 == "Y" and p1 == "A":
        score += 4
   
    if p2 == "Y" and p1 == "B":
        score += 5

    if p2 == "Y" and p1 == "C":
        score += 6
    
    if p2 == "Z" and p1 == "A":
        score += 8 
    
    if p2 == "Z" and p1 == "B":
        score += 9
   
    if p2 == "Z" and p1 == "C":
        score += 7
       
    return score
 
final_score = 0
 
for list in list_of_lists:
    result = calculate_score(list[0], list[1])
    final_score += result
   
print(final_score)

test_data = ["A", "Y", "B", "X", "C", "Z"]
n = 2

test_list_of_lists = [test_data[i * n:(i + 1) * n] for i in range((len(test_data) + n - 1) // n )]

new_final_score = 0

for list in test_list_of_lists:
    result = calculate_new_score(list[0], list[1])
    new_final_score += result
   
print(new_final_score)