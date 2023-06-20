from __future__ import annotations

import io
import os
from PIL import Image

import basic


def reduce_size(
        filename, directory: None | str = None,
        name: str | None = None,
        ext: str | None = None,
        delete: bool = False):
    image = Image.open(filename)
    target_size = 1000000

    quality = 90
    while True:
        image_buffer = io.BytesIO()
        image.save(image_buffer, format='JPEG', quality=quality)
        image_size = image_buffer.tell()
        if image_size <= target_size:
            break
        quality -= 10

    if directory is None:
        directory = os.path.dirname(filename)
        delete = True

    if name is None:
        name = basic.get_name_file(filename)
        delete = True

    if ext is None:
        ext = basic.get_file_extension(filename)
        delete = True

    image.save(f'{directory}/{name}{ext}', format='JPEG', quality=quality)
    if delete:
        os.remove(filename)

#
# path = 'C:\\Users\\MSI\\Documents\\tmt-model-managment\\src\\assets\\images'
# files = browse_files(path)
# print(len(files))
# for f in files:
#     print(f)
#     file_extension = get_file_extension(f)
#     if file_extension.lower() == '.tif':
#         reduce_size(f, ext='jpg')
#     else:
#         print(f)