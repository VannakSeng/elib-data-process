import os
import shutil
import time
import multiprocessing as mp

from fpdf import FPDF
from fpdf.fpdf import Image
from reportlab.lib.pagesizes import letter
import basic


def image_to_pdf(source: str, resize: bool = False, target_size: int = 1000000):
    images = [image for image in os.listdir(source) if not image.startswith('.')]
    images.sort()
    pdf = FPDF()
    for image_path in images:
        filename = f'{source}/{image_path}'
        new_filename = filename.replace('.tif', '.jpg')
        os.rename(filename, new_filename)
        basic.reduce_size(new_filename, 250000)
        pdf.add_page()

        pdf.image(new_filename, 0, 0, w=210, keep_aspect_ratio = True)
    pdf.output(f'{source}.pdf')


def multi_core(source: str):
    # path = f"{root_path}/សមាគមមិត្តគយនៃកម្ពុជា"
    start = time.time()
    dirs = os.listdir(source)
    dirs.sort()
    for dir in dirs:
        p = mp.Process(target=image_to_pdf, args=(dir,))
        p.start()
    end = time.time()
    print(end - start)

if __name__ == '__main__':
    root_path = r'/Users/stone-wh/Library/CloudStorage/OneDrive-RoyalUniversityofPhnomPenh/e-library of cambodia/Backup'
    folder = r"P_Fonds Periodic Khmer/P-K 000  មាតុភូមិ/Year 2 Nº 8 ( 30-May-1955 )"
    image_to_pdf(f'{root_path}/{folder}')
    # for dir in os.listdir(f'{root_path}/{folder}'):
    #     full_path = f'{root_path}/{folder}/{dir}'
    #     if os.path.isdir(full_path):
    #         image_to_pdf(full_path, resize=True)
    #         shutil.rmtree(full_path)

