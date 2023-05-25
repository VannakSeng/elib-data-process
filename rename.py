import os

import basic

path = "S:\\Elib\\5004"
all_files = basic.browse_files(path)
i = 0
for f in all_files:
    i = i + 1
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

    ext = basic.get_file_extension(f)
    os.rename(f, f'{path}\\{i:06}{ext}')