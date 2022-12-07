levels = {
    "1": ["a", "d"],
    "2": ["e"]
}

contents = {
    "a": ["dir e", "29116 f", "2557 g", "62596 h.lst"],
    "d": ["4060174 j", "8033020 d.log", "5626152 d.ext", "7214296 k"],
    "e": ["584 i"]
}

totals = {}

level_keys = list(levels.keys())

reversed_levels = list(reversed(level_keys))

for level in reversed_levels:
    level_list = levels[level]
    for directory in level_list:
        total = 0
        for file in contents[directory]:
            file_name = file.split(" ")
            if file_name[0] == "dir":
                total += totals[file_name[1]]
            else:
                total += int(file_name[0])
        totals[directory] = total

print("Totals: " + str(totals))

final_total = 0

for key in totals:
    if totals[key] < 100000:
        final_total += totals[key]

print("Final total: " + str(final_total)) 

