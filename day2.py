data = ["A", "Y", "B", "X", "C", "Z"]
n = 2
 
list_of_lists = [data[i * n:(i + 1) * n] for i in range((len(data) + n - 1) // n )]
print(list_of_lists)
 
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
 
final_score = 0
 
for list in list_of_lists:
    result = calculate_score(list[0], list[1])
    final_score += result
   
print(final_score)