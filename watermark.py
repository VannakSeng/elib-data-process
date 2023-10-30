import io
import os
import shutil

from PIL import Image
from PyPDF2 import PageObject, PdfReader, PdfWriter
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas
import uuid
import basic


def __watermark(w: float, h: float) -> PageObject:
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=(w, h))
    can.setFillColorRGB(10, 10, 10, 0.4)
    can.setFontSize(w * 0.0248)
    can.drawString(w / 2 - (w * 0.1865), h / 2, "www.elibraryofcambodia.org")
    can.save()
    packet.seek(0)
    result = PdfReader(packet).pages[0]
    return result


def pdf_set_watermark(source: str, target: str, target_size: int = None):
    print(f'start process {source}')
    if not source.endswith('.pdf'):
        print(f"Error not PDF file of {source}\n")
        return
    if not os.path.exists(source):
        print(f"Error file not found of {source}")
        return
    source_pdf = PdfReader(open(source, "rb"), strict=False)
    target_pdf = PdfWriter()
    os.makedirs('temp', exist_ok=True)
    watermark_page = None
    i = 0
    temp_filename = f'temp/{uuid.uuid4()}.png'
    for page in source_pdf.pages:
        with open(temp_filename, "wb") as output_stream:
            output_stream.write(page.images[i].data)
        if target_size is not None:
            basic.reduce_size(temp_filename, target_size)
        width, height = Image.open(temp_filename).size
        watermark_page = __watermark(width, height)
        new_page = new_page_image(width, height, temp_filename)
        new_page.merge_page(watermark_page)
        target_pdf.add_page(new_page)
        if len(page.images) > 1:
            i += 1
    with open(target, "wb") as output_stream:
        target_pdf.write(output_stream)
    print(f'finished process {source}')
    os.remove(temp_filename)


def new_page_image(w: float, h: float, path: str) -> PageObject:
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=(w, h))
    img = ImageReader(path)
    can.drawImage(img, 0, 0, w, h)
    can.save()
    packet.seek(0)
    return PdfReader(packet).pages[0]

def image_to_pdf_with_watermark(source: str, target: str, target_size: int = None):
    print(f'start process {source}')
    if not os.path.isdir(source):
        print(f"Error not a folder of {source}")
        return
    if not os.path.exists(source):
        print(f"Error file not found of {source}")
        return
    target_pdf = PdfWriter()
    watermark_page = None
    temp_filename = f'temp/{uuid.uuid4()}.png'
    images = [image for image in os.listdir(source) if
              image.endswith('.tif') or image.endswith('.jpg') or image.endswith('.png')]
    images.sort()
    for image in images:
        shutil.copyfile(f'{source}/{image}', temp_filename)
        if target_size is not None:
            basic.reduce_size(temp_filename, target_size)
        width, height = Image.open(temp_filename).size
        watermark_page = __watermark(width, height)
        new_page = new_page_image(width, height, temp_filename)
        new_page.merge_page(watermark_page)
        target_pdf.add_page(new_page)
    with open(target + ".pdf", "wb") as output_stream:
        target_pdf.write(output_stream)
    print(f'finished process {source}')
    os.remove(temp_filename)


if __name__ == "__main__":
    source_file = "data/EFEO B110.VII ភិក្ខុបាដិមោក្ខ.pdf"
    target_file = "output.pdf"
    pdf_set_watermark(source_file, target_file, target_size=None)
