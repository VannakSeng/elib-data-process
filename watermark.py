import io
import multiprocessing
import os
import time

from PIL import Image
from PyPDF2 import PageObject, PdfFileReader, PdfFileWriter
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas

import basic


def watermark(w: float, h: float) -> PageObject:
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=(w, h))
    can.setFillColorRGB(10, 10, 10, 0.4)
    can.setFontSize(w * 0.0248)
    can.drawString(w / 2 - (w * 0.1865), h / 2, "www.elibraryofcambodia.org")
    can.save()
    packet.seek(0)
    result = PdfFileReader(packet).pages[0]
    return result


def new_page_image(w: float, h: float, path: str) -> PageObject:
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=(w, h))
    img = ImageReader(path)
    can.drawImage(img, 0, 0, w, h)
    can.save()
    packet.seek(0)
    result = PdfFileReader(packet).pages[0]
    return result


def set_watermark(path: str, filename: str):
    print(f'start {filename}')
    target_path = f'{path}_Watermarks'
    input_file = f'{path}/{filename}'
    temp_filename = f'{target_path}/temp_{time.time()}.png'
    if not os.path.exists(target_path):
        os.mkdir(target_path)
    existing_pdf = PdfFileReader(open(input_file, "rb"), strict=False)
    output = PdfFileWriter()
    watermark_page = None
    for page in existing_pdf.pages:
        with open(temp_filename, "wb") as output_stream:
            output_stream.write(page.images[0].data)
        basic.reduce_size(temp_filename, 200000)
        im = Image.open(temp_filename)
        width, height = im.size
        if watermark_page is None:
            watermark_page = watermark(width, height)
        new_page = new_page_image(width, height, temp_filename)
        new_page.merge_page(watermark_page)
        output.add_page(new_page)
    output_file = f'{target_path}/{filename}'
    with open(output_file, "wb") as output_stream:
        output.write(output_stream)
    print(f'finished {filename}')
    os.remove(temp_filename)
    return temp_filename


if __name__ == '__main__':
    root_path = '/Users/stone-wh/Library/CloudStorage/OneDrive-RoyalUniversityofPhnomPenh/e-library of cambodia/Backup/1_Fonds_Periodicques_Khmer_PDF'
    path = f"{root_path}/Ready"
    dirs = os.listdir(path)
    start = time.time()
    with multiprocessing.Pool() as pool:
        items = [(path, dir_name) for dir_name in dirs if dir_name.endswith('.pdf')]
        for result in pool.starmap(set_watermark, items):
            print(result)
    end = time.time()
    print(end - start)