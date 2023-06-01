import os
import shutil

import basic

def production_group():
    path = "/Users/stone-wh/Library/CloudStorage/GoogleDrive-vannakseng1996@gmail.com/My Drive/E-Library of Cambodia/Elib-duplicated/Done Rename/"
    all_files = basic.browse_files(path)
    for file in all_files:
        name = basic.get_name_file(file)
        sub_dir = 'កម្ពុជា'
        os.makedirs(f'{path}/{sub_dir}', exist_ok=True)
        if name.startswith(sub_dir):
            ext = basic.get_file_extension(file)
            new_file = f'{path}/{sub_dir}/{name}{ext}'
            # print(file)
            # print(new_file)
            shutil.move(file, new_file)

def code_group():
    path = "/Users/stone-wh/Library/CloudStorage/GoogleDrive-vannakseng1996@gmail.com/My Drive/E-Library of Cambodia/Elib-duplicated/Done Rename/កម្ពុជា"
    all_files = basic.browse_files(path)
    for file in all_files:
        name = basic.get_name_file(file)
        detector = 'កម្ពុជា-'
        if not name.startswith(detector):
            new_name = name.replace('កម្ពុជា', detector)
            new_file = file.replace(name, new_name)
            os.rename(file, new_file)


code_group()
# Done Rename/កម្ពុជា/ច័ន្ទឆាយា-(C7127B