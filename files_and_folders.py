import os

# improvement liberally borrowed from:
# https://forum.omz-software.com/topic/2784/feature-request-pythonista-built-in-file-picker


def files_and_folders(dir_path="."):
    """Return a dict containing a sorted tuple of files and a sorted
    tuple of folders.
    """
    f_and_f = os.listdir(dir_path)
    folders = [f for f in f_and_f if os.path.isdir(os.path.abspath(f))]
    files = set(f_and_f) - set(folders)
    return {
        "files": tuple(sorted(files, key=str.lower)),
        "folders": tuple(sorted(folders, key=str.lower)),
    }


def old_files_and_folders(dir_path="."):
    files = []
    folders = []
    for filename in sorted(os.listdir(dir_path)):
        if os.path.isdir(os.path.join(dir_path, filename)):
            folders.append(filename)
        else:
            files.append(filename)
    return tuple(files), tuple(folders)


print(files_and_folders())
