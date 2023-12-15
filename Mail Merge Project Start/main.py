# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
with open("./Input/Names/invited_names.txt") as file:
    names = file.readlines()

print(names)

with open("./Input/Letters/starting_letter.txt") as file:
    letter = file.read()

for name in names:
    name = name.strip("\n")
    letter_to_write = letter.replace("[name]", name)
    letter_file = f"letter_to_{name}.txt"
    with open(f"./Output/ReadyToSend/{letter_file}", mode="w") as file:
        file.write(letter_to_write)

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
