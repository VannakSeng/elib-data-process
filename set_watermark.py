import os
import shutil
import uuid
from PIL import Image, ImageDraw, ImageFont
from PyPDF2 import PdfWriter, PdfReader
import basic

def image_to_pdf_with_watermark(source: str, target: str, target_size: int = None):
    print(f'start process {source}')
    if not os.path.isdir(source):
        print(f"Error not a folder of {source}")
        return
    if not os.path.exists(source):
        print(f"Error file not found of {source}")
        return
    os.makedirs('temp', exist_ok=True)
    target_pdf = PdfWriter()
    temp_filename = f'temp/{uuid.uuid4()}.png'
    images = [image for image in os.listdir(source) if
              image.endswith('.tif') or image.endswith('.jpg') or image.endswith('.png')]
    images.sort()

    for image in images:
        shutil.copyfile(f'{source}/{image}', temp_filename)
        if target_size is not None:
            basic.reduce_size(temp_filename, target_size)

        # Add watermark to the image
        watermarkImage(temp_filename, temp_filename, "www.elibraryofcambodia.org")

        pdf_page = PdfReader(open(temp_filename, 'rb')).getPage(0)
        target_pdf.addPage(pdf_page)

    with open(target + ".pdf", "wb") as output_stream:
        target_pdf.write(output_stream)

    print(f'finished process {source}')
    os.remove(temp_filename)


def watermarkImage(image_path, output_path, text):
    base_image = Image.open(image_path)
    width, height = base_image.size

    text_color = (222, 222, 222)
    font_style = "font/Calibri Regular.ttf"
    font_size = int(width * 0.0248)

    transparent = Image.new('RGBA', (width, height), (255, 255, 255, 0))
    transparent.paste(base_image, (0, 0))
    draw = ImageDraw.Draw(transparent)

    font = ImageFont.truetype(font_style, font_size)
    text_bbox = draw.textbbox((0, 0), text, font)
    text_width, text_height = text_bbox[2], text_bbox[3]

    text_position = ((width - text_width) // 2, (height - text_height) // 2)

    text_image = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    text_draw = ImageDraw.Draw(text_image)
    text_draw.text(text_position, text, fill=(text_color[0], text_color[1], text_color[2], 128), font=font)
    transparent = Image.alpha_composite(transparent, text_image)
    transparent.convert('RGB').save(output_path)




image_to_pdf_with_watermark('data1/file2', 'data1', )
