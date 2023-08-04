import os

import basic

path = "/Users/stone-wh/Library/CloudStorage/OneDrive-RoyalUniversityofPhnomPenh/e-library of cambodia/Backup/1_Fonds_Periodicques_Khmer_PDF"
all_files = basic.browse_files(path)
for file in all_files:
    name = basic.get_name_file(file)
    newName = name.replace('Revue amicale des ecoles de pali ', 'មិត្តសាលាបាលី ឆ្នាំទី')
    # newName = name.replace('Lami de lecole de pali ', 'មិត្តសាលាបាលី ឆ្នាំទី')
    # newName = name.replace('Revue de Instituteur Khmer ', 'សម្រាប់គ្រូបង្រៀន ឆ្នាំទី')ពន្លឺពុទ្ធចក្រ
    # newName = name.replace('LEtude association des anciens ', 'វិជ្ជា ឆ្នាំទី')
    # newName = name.replace('La lumiere bouddhique V', 'ពន្លឺពុទ្ធចក្រ លេខ')LEtude association des anciens
    # newName = name.replace('Le Lycee Bouddhique V', 'ពុទ្ធិកវិទ្យាល័យ លេខ')
    # newName = name.replace('មិត្ដសាលាបាលី ឆ្នាំទី', 'សាស្រ្ដាចារ្យ ឆ្នាំទី')
    # newName = newName.replace('ans', ' លេខ')
    newFile = file.replace(name, newName)
    os.rename(file, newFile)

    # newName = newName.replace('_', '')
    # newName = newName.replace(' ', '')
    # newName = newName.replace('.', '')
    # newFile = file.replace(name, newName)
    # print(file)
    # print(newFile)
    # os.rename(file, newFile)
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