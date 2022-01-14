#TODO: Create a letter using starting_letter.txt
with open("./Input/Names/invited_names.txt", newline="\n") as names_file:
    names = names_file.read().split()
with open("./Input/Letters/starting_letter.txt", newline="\n") as starting_letter:
    sample_letter = starting_letter.read()
# for each name in invited_names.txt
for name in names:
    #Save the letters in the folder "ReadyToSend".
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", "w") as output:
        #Replace the [name] placeholder with the actual name.
        output.write(sample_letter.replace("[name]", name))


