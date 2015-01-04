filename = 'menu.py'
with open(filename) as in_file:
    text = [line.rstrip() + '\n' for line in in_file.readlines()]
with open(filename, 'w') as out_file:
    out_file.writelines(text)
