
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
    # Set the target file size in bytes (2 MB = 2,000,000 bytes)
    target_size = 2000000

    # Iterate and reduce the image quality until the target size is reached
    quality = 90  # Initial quality value
    while True:
        # Create a buffer to hold the resized image
        image_buffer = io.BytesIO()
        # Save the image with the current quality value to the buffer
        image.save(image_buffer, format='JPEG', quality=quality)

        # Get the size of the image buffer
        image_size = image_buffer.tell()

        # If the size is within the target range, break the loop
        if image_size <= target_size:
            break

        # Reduce the quality by 10% for the next iteration
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

    # Save the final resized image to a files
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