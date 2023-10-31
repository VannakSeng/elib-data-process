import io
import os
import shutil
from datetime import datetime
from PIL import Image
from PyPDF2 import PageObject, PdfReader, PdfWriter
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import utils
from pdf2image import convert_from_path
import uuid
import basic


def __watermark(w: float, h: float) -> PageObject:
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=(w, h))
    can.setFillColorRGB(10, 10, 10, 0.6)
    can.setFontSize(w * 0.0248)
    can.drawString(w / 2 - (w * 0.1865), h / 2, "www.elibraryofcambodia.org")
    can.save()
    packet.seek(0)
    result = PdfReader(packet).pages[0]
    return result


def pdf_set_watermark(source: str, target: str, target_size: int = None):
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%b-%d %I:%M%p")
    print(f'{formatted_datetime} : start process {source}')
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

    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%b-%d %I:%M%p")
    print(f'{formatted_datetime} : finished process {source} at ')
    os.remove(temp_filename)


def pdf_set_watermark_JBIG2Decode(source: str, target: str, target_size: int = None):
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%b-%d %I:%M%p")
    print(f'{formatted_datetime} : start process {source}')
    if not source.endswith('.pdf'):
        print(f"Error not a PDF file: {source}\n")
        return
    if not os.path.exists(source):
        print(f"Error file not found: {source}")
        return

    source_pdf = PdfReader(open(source, "rb"), strict=False)
    target_pdf = PdfWriter()
    os.makedirs('temp', exist_ok=True)
    watermark_page = None

    for page_number, page in enumerate(source_pdf.pages, start=1):
        if '/Resources' in page and '/XObject' in page['/Resources']:
            xobject = page['/Resources']['/XObject'].get_object()
            if xobject is not None:
                for obj in xobject:
                    x_object = xobject[obj]
                    if '/Filter' in x_object.get_object() and x_object.get_object()['/Filter'] == '/JBIG2Decode':
                        continue  # Skip pages with unsupported filter

        temp_filename = f'temp/{uuid.uuid4()}.png'

        # Convert the page to an image (PNG) using pdf2image
        images = convert_from_path(source, first_page=page_number, last_page=page_number)
        if images:
            images[0].save(temp_filename, 'PNG')

        if target_size is not None:
            basic.reduce_size(temp_filename, target_size)

        width, height = Image.open(temp_filename).size
        watermark_page = __watermark(width, height)
        new_page = new_page_image(width, height, temp_filename)
        new_page.merge_page(watermark_page)
        target_pdf.add_page(new_page)

    with open(target, "wb") as output_stream:
        target_pdf.write(output_stream)

    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%b-%d %I:%M%p")
    print(f'{formatted_datetime} : finished process {source} at ')
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
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%b-%d %I:%M%p")
    print(f'{formatted_datetime} : start process {source}')

    if not os.path.isdir(source):
        print(f"Error not a folder of {source}")
        return
    if not os.path.exists(source):
        print(f"Error file not found of {source}")
        return

    target_pdf = PdfWriter()
    watermark_page = None
    temp_filename = f'temp/{uuid.uuid4()}.png'
    images = [image for image in os.listdir(source) if image.endswith('.tif') or image.endswith('.jpg') or image.endswith('.png')]
    images.sort()

    for image in images:
        shutil.copyfile(f'{source}/{image}', temp_filename)

        if target_size is not None:
            basic.reduce_size(temp_filename, target_size)
        img = utils.ImageReader(temp_filename)
        width, height = img.getSize()
        img_width = 595
        img_height = height * img_width / width
        watermark_page = __watermark(img_width, img_height)
        new_page = new_page_image(img_width, img_height, temp_filename)
        new_page.merge_page(watermark_page)
        target_pdf.add_page(new_page)

    with open(target + ".pdf", "wb") as output_stream:
        target_pdf.write(output_stream)

    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%b-%d %I:%M%p")
    print(f'{formatted_datetime} : finished process {source} at ')
    os.remove(temp_filename)

if __name__ == "__main__":
    image_to_pdf_with_watermark('data1', 'output_.pdf')
