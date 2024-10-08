import clipboard

filename = "put_your_filename_here.pyui"  # edit this line before running
with open(filename) as in_file:
    clipboard.set(in_file.read())
print(f"The contents of {filename} are now on the clipboard.")
