# Save the text of the current the Pythonista Editor into a
# separate file with a similar name with a timestamp added.
# It is meant to be added to the editor's action menu.
# inspired by: http://omz-forums.appspot.com/pythonista/post/5903756180848640

import datetime, editor, os, sys  # noqa

text = editor.get_text()
if not text:
    sys.exit('No text in the Editor.')
root, ext = os.path.splitext(editor.get_path())
filename = '{}_{:%Y_%m_%d_%H_%M_%S}{}'.format(root, datetime.datetime.now(),
                                              ext)
with open(filename, 'w') as out_file:
    out_file.write(text)
print('{} bytes successfully written to {}.'.format(len(text), filename))
