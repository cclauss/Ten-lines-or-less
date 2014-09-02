import os
def files_and_folders(dir_path='.'):
    files = []
    folders = []
    for filename in sorted(os.listdir(dir_path)):
        if os.path.isdir(os.path.join(dir_path, filename)):
            folders.append(filename)
        else:
            files.append(filename)
    return tuple(files), tuple(folders)
