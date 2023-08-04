import io
import os
from PIL import Image
# from difPy import dif

from basic import get_file_extension, browse_files

#
# def reduce_size(
#         filename, directory: None | str = None,
#         name: str | None = None,
#         ext: str | None = None,
#         delete: bool = False):
#     image = Image.open(filename)
#     # Set the target file size in bytes (2 MB = 2,000,000 bytes)
#     target_size = 2000000
#
#     # Iterate and reduce the image quality until the target size is reached
#     quality = 90  # Initial quality value
#     while True:
#         # Create a buffer to hold the resized image
#         image_buffer = io.BytesIO()
#         # Save the image with the current quality value to the buffer
#         image.save(image_buffer, format='JPEG', quality=quality)
#
#         # Get the size of the image buffer
#         image_size = image_buffer.tell()
#
#         # If the size is within the target range, break the loop
#         if image_size <= target_size:
#             break
#
#         # Reduce the quality by 10% for the next iteration
#         quality -= 10
#
#     if directory is None:
#         directory = os.path.dirname(filename)
#         delete = True
#
#     if name is None:
#         name = os.path.splitext(os.path.basename(filename))[0]
#         delete = True
#
#     if ext is None:
#         ext = get_file_extension(filename)
#         delete = True
#
#     # Save the final resized image to a files
#     image.save(f'{directory}/{name}.{ext}', format='JPEG', quality=quality)
#     if delete:
#         os.remove(filename)
#
# path = "C:/Users/MSI/OneDrive - Royal University of Phnom Penh/e-library of cambodia\Backup/0Scan/Akthebuy Sasanak Sopheaseth Pesda"
# files = browse_files(path)
# for f in files:
#     file_extension = get_file_extension(f)
#     if file_extension.lower() == '.tif':
#         reduce_size(f, ext='jpg')
#     else:
#         print(f)
#
# # print(len(files))

# search = dif("S:\\Test\\test")
# locations = search.result.values()
# print(locations)
#
# num = 1
# for i in search.result:
#     filename = search.result[i]['location']
#     head, tail = os.path.split(filename)
#     os.makedirs(f'{head}\\{num}')
#     os.rename(filename, f'{head}\\{num}\\{tail}')
#     # print(search.result[i]['location'])
#     for j in search.result[i]['matches']:
#         # print(search.result[i]['matches'][j]['location'])
#         subname = search.result[i]['matches'][j]['location']
#         head, tail = os.path.split(subname)
#         os.rename(subname, f'{head}\\{num}\\{tail}')
#     # print()
#     num = num + 1;
#
# def duplicat():
#     search = dif("S:\Elib")
#     locations = search.result.values()
# with open('result.txt', 'w') as f:
#     f.write('Duplicated files: ' + str(len(locations)) + "\n")
# for location in locations:
#     print('Location: ' + location['location'].replace('/image/', ''))
#     match = location['matches'].values()
#
#     with open('result.txt', 'a') as f:
#         f.write('Location: ' + location['location'].replace('/image/', '') + '\n')
#
#     for m in match:
#         print("Delete: " + m['location'])
#         os.remove(m['location'])
#         with open('result.txt', 'a') as f:
#             f.write('Delete: ' + m['location'].replace('/image/', '') + '\n\n')
#         print('\n')
# print("Done")
# reduce_size('S:\\Elib\\5004\\45_2008A.jpg')
