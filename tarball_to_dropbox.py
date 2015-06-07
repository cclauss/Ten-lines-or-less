# See: http://omz-forums.appspot.com/pythonista/post/5823162193281024

import dropboxlogin, os, tarfile

tar_file_name = 'my_archive.tar'

with tarfile.open(tar_file_name, 'w') as out_file:
    out_file.add(os.path.basename(__file__))  # add this script at the root of the tarball

with open(tar_file_name) as in_file:
    dropboxlogin.get_client().put_file(tar_file_name, in_file, overwrite=True)
