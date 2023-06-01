import os

import basic

path = "/Users/stone-wh/Library/CloudStorage/GoogleDrive-vannakseng1996@gmail.com/My Drive/E-Library of Cambodia/Elib-duplicated/Done Rename"
all_files = basic.browse_files(path)
for file in all_files:
    name = basic.get_name_file(file)
    newName = name.replace('​', '')
    newName = newName.replace('_', '')
    newName = newName.replace(' ', '')
    newName = newName.replace('.', '')
    newFile = file.replace(name, newName)
    print(file)
    print(newFile)
    os.rename(file, newFile)
# i = 0
# for f in all_files:
#     i = i + 1
    # ext = get_file_extension(f)
    # try:
        # n = f.replace('Watermark - ', '')
        # os.rename(f, n)
        # name = get_name_file(f)
        # ext = get_file_extension(f)
        # ext = f[-3:]
        # n = f.replace('.', '')
        # os.rename(f, f'{f[:-3]}.{f[-3:]}')
    # except:
    #     print(f)

    # ext = basic.get_file_extension(f)
    # os.rename(f, f'{path}\\{i:06}{ext}')