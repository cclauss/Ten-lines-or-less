filename = "menu.py"
with open(filename) as in_file:
    text = "\n".join([line.rstrip() for line in in_file.readlines()]) + "\n"
with open(filename, "w") as out_file:
    out_file.writelines(text)
