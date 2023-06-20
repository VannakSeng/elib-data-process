import os

import basic

path = '/Volumes/Docker/Elib/1_Fonds_Periodicques_Khmer_PDF'
files = basic.browse_files(path)

basic.get_cover_pdf(files[0])
# for f in files:
#     if '..tif' not in f:
#         # try:
#         #     os.remove(f)
#         # except:
#             print(f)