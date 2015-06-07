# See: http://omz-forums.appspot.com/pythonista/post/5823162193281024

import dropboxlogin, tarfile

tar_file_name = 'my_archive.tar'

with open(tar_file_name, 'w') as out_file:
    out_file.write(dropboxlogin.get_client().get_file(tar_file_name).read())
with tarfile.open(tar_file_name) as tar_file:
    tar_file.extractall()
