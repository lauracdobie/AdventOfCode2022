data = ""
fileobj=open("day6_input.txt")
data=fileobj.read()

marker_list = []
 
string = "mjqjpqmgbljsphdztnvjfqwrcgsmlb" #Result should be 7
string1 = "bvwbjplbgvbhsrlpgdmjqwftvncz" #Result should be 5
string2 = "nppdvjthqldpwncqszvftbrmjlhg" #Result should be 6
string3 = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg" #Result should be 10
string4 = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw" #Result should be 11
 
list = []
 
for char in data:
  list.append(char)
 
start_index = 0
end_index = 14

block_to_check = list[start_index:end_index]

found = False

while found == False:
    for letter in block_to_check:
        if letter not in marker_list:
            marker_list.append(letter)
        if len(marker_list) == 14 :
            print("Result is: " + str(end_index))
            found = True
    marker_list = []
    start_index += 1
    end_index += 1
    block_to_check = list[start_index:end_index]
 
