import io
import os
import re
import uuid

import fitz
from PIL import Image


def browse_files(path: str, endswith: str, is_full_path: bool = True) -> list[str]:
    files = []
    for file in os.listdir(path):
        if file.endswith(endswith):
            if is_full_path:
                files.append(f'{path}/{file}')
            else:
                files.append(file)
    return files


def browse_folders(path: str, is_full_path: bool = True) -> list[str]:
    folders = []
    for dir_name in os.listdir(path):
        full_path = f'{path}/{dir_name}'
        if os.path.isdir(full_path):
            if is_full_path:
                folders.append(f'{path}/{dir_name}')
            else:
                folders.append(dir_name)
    return folders


def get_file_extension(file_path: str) -> str:
    _, file_extension = os.path.splitext(file_path)
    return file_extension


def get_name_file(filename: str) -> str:
    name = os.path.splitext(os.path.basename(filename))[0]
    return name


def reduce_size(filename: str, target_size: int = 1000000):
    img = Image.open(filename)
    quality = 90
    image_size = 0
    while True:
        image_buffer = io.BytesIO()
        img.save(image_buffer, format='JPEG', quality=quality)
        size = image_buffer.tell()
        if image_size != size:
            image_size = size
        else:
            break
        if image_size <= target_size:
            break
        quality -= 10
    img.save(filename, format='JPEG', quality=quality)


def get_path(filename: str) -> str:
    return os.path.dirname(os.path.abspath(filename))


def save_pdf_cover(filename: str, page_index: int = 0) -> str:
    doc = fitz.open(filename)
    pix = doc[page_index].get_pixmap(
        matrix=fitz.Identity,
        dpi=None,
        colorspace=fitz.csRGB,
        clip=None,
        alpha=True,
        annots=True)
    # new_filename = filename.replace('.pdf', '.png')
    os.makedirs('temp', exist_ok=True)
    new_filename = f'temp/{uuid.uuid4()}.png'
    pix.save(new_filename)
    return new_filename


def read_file(file_name: str) -> [str]:
    with open(file_name) as f:
        return f.readlines()


def write_file(file_name: str, text: str):
    with open(file_name, "a") as my_file:
        my_file.write(text)

# path = "/Users/stone-wh/Library/CloudStorage/OneDrive-RoyalUniversityofPhnomPenh/e-library of cambodia/Backup/1_Fonds_Periodicques_Khmer_PDF/Ready"
# text = ''
# var = 0
# jpg = 0
# all = 0
# for dir_name in os.listdir(path):
#     filename = f'{path}/{dir_name}'
#     all +=1
#     if (dir_name.endswith('.bmp')):
#         reduce_size(filename)
#         new_file = filename.replace('.bmp', '.jpg')
#         os.rename(filename, new_file)
#     elif (dir_name.endswith('.png')):
#         new_file = filename.replace('.png', '.jpg')
#         os.rename(filename, new_file)
#     elif (dir_name.endswith('.jpg')):
#         jpg += 1
#     elif (dir_name.endswith('.pdf')):
#         img_file = filename.replace('.pdf', '.jpg')
#         if os.path.isfile(img_file):
#             print('check_file')
#             var += 1
# print(var)
# print(jpg)
# print(all)
# text = f"{text}{filename.replace('/', ',')}\n"
# # save_pdf_cover(filename)
# post_newspaper(filename)
# post_newspaper('/Volumes/Docker/Elib/1_Fonds_Periodicques_Khmer_PDF/35. Lami de lecole de pali 1ans3.pdf')
# write_file('/Users/stone-wh/Library/CloudStorage/OneDrive-RoyalUniversityofPhnomPenh/e-library of cambodia/publish.csv', text)
