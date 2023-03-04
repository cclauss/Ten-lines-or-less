import clipboard

filename = "pyui_from_clipboard.pyui"  # edit this line BEFORE running
assert clipboard.get(), "There is no text on the clipboard!"
with open(filename, "w") as out_file:
    out_file.write(clipboard.get())
print(f"The contents of the clipboard are now on file {filename}.")
