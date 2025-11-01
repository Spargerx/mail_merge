with open("./Input/Letters/starting_letter.txt") as file:
    letter = file.read()
    
with open("./Input/Names/invited_names.txt") as file:
    names_list = file.readlines()
    
for name in names_list:
    
    name = name.strip()
    new_letter = letter.replace("[name]", name)
    
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", "w") as final_letter:
        final_letter.write(new_letter)