with open("./Input/Names/invited_names.txt", "r") as names_file:
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as content:
    letter = content.read()
    for name in names:
        name = name.strip()
        invitation = letter.replace("[name]", name)
        with open(f"./Output/ReadyToSend/{name}.txt", "w") as invitation_letter:
            invite = invitation_letter.write(invitation)



