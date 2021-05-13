from os import walk, makedirs
from os.path import getmtime, join, exists, basename
from time import localtime
from shutil import copyfile


def __group_files_by_date(directory):
    res = {}
    for (dirpath, dirnames, filenames) in walk(directory):
        print(dirpath)
        print(dirnames)
        print(filenames)
        for file in filenames:
            # return (dirnames, filenames)
            date = localtime(getmtime(join(dirpath, file)))
            print(str(date.tm_mon).rjust(2, '0'))
            key = str(join(str(date.tm_year), str(date.tm_mon).rjust(2, '0')))
            print(key)
            if (key in res):
                res[key].append(join(dirpath, file))
            else:
                res[key] = [join(dirpath, file)]
    return res


def __copy_to_folder(rootPath, folder, files):
    dest = join(rootPath, 'parDate', folder)
    if (not exists(dest)):
        makedirs(dest)
    for file in files:
        print(file)
        print(dest)
        copyfile(file, join(dest, basename(file)))
