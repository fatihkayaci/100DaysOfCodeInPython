clear_characters = []
with open("/Users/pc/Desktop/100daysofcode/100DaysOfCodeInPython/24-)day24/Mail Merge Project Start/Input/Names/invited_names.txt") as names:
    name_list = names.readlines()
    for name in name_list:
        clear_characters.append(name.strip())

with open("/Users/pc/Desktop/100daysofcode/100DaysOfCodeInPython/24-)day24/Mail Merge Project Start/Input/Letters/starting_letter.txt") as start_text:
    text = start_text.read()
    for name in clear_characters:
        x = text.replace("[name]", name)
        file = open(f"/Users/pc/Desktop/100daysofcode/100DaysOfCodeInPython/24-)day24/Mail Merge Project Start/Output/ReadyToSend/letter_for_{name}.txt", "w")
        file.write(x)
