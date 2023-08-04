import io
import os

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


def set_watermark(target_path: str, source_path: str, filename: str):
    input_file = f'{source_path}/{filename}'
    existing_pdf = PdfFileReader(open(input_file, "rb"), strict=False)
    output = PdfFileWriter()
    watermark_page = None
    for page in existing_pdf.pages:
        with open(f'{target_path}/temp.png', "wb") as output_stream:
            output_stream.write(page.images[0].data)
        basic.reduce_size(f'{target_path}/temp.png', 200000)
        im = Image.open(f'{target_path}/temp.png')
        width, height = im.size
        if watermark_page is None:
            watermark_page = watermark(width, height)
        new_page = new_page_image(width, height, f'{target_path}/temp.png')
        new_page.merge_page(watermark_page)
        output.add_page(new_page)
    output_file = f'{target_path}/{filename}'
    with open(output_file, "wb") as output_stream:
        output.write(output_stream)


root_path = '/Users/stone-wh/Library/CloudStorage/OneDrive-RoyalUniversityofPhnomPenh/e-library of cambodia/Backup/1_Fonds_Periodicques_Khmer_PDF'
path = f"{root_path}/Ready"
target_path = f"{root_path}/Watermarks"
for dir_name in os.listdir(path):
    if dir_name.endswith('សាស្រ្ដាចារ្យ ឆ្នាំទី7 លេខ20.pdf'):
        set_watermark(target_path, path, dir_name)


# import pdfkit
#
#
# def compress_pdf(input_file, output_file):
#     options = {
#         "compress": True,
#         "dpi": 150,
#     }
#     pdfkit.from_file(input_file, output_file, options=options)
#
#
# in_file = f'{root_path}/Ready/80.សាស្រ្ដាចារ្យ ឆ្នាំទី7 លេខ20.pdf'
# out_file = f'{root_path}/Watermarks/80.សាស្រ្ដាចារ្យ ឆ្នាំទី7 លេខ20.pdf'
# # compress_pdf(in_file, out_file)
# pdfkit.from_url('http://google.com', './out.pdf');
