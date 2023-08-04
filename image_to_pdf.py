import os
import shutil

from PIL import Image
from fpdf import FPDF
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Image
import basic


def image_to_pdf(folder: str, resize: bool = False, target_size: int = 1000000):
    images = basic.browse_files(folder)
    images.sort()
    pdf = FPDF()
    for image_path in images:
        if resize:
            basic.reduce_size(image_path, target_size)
        pdf.add_page()
        pdf.image(image_path, 0, 0, 210, 297)
    pdf.output(f'{folder}.pdf')


path = '/Users/stone-wh/Library/CloudStorage/OneDrive-RoyalUniversityofPhnomPenh/e-library of cambodia/Backup'
folder = "P_Revue de l'adoca"
for dir in os.listdir(f'{path}/{folder}'):
    full_path = f'{path}/{folder}/{dir}'
    if os.path.isdir(full_path):
        image_to_pdf(full_path, resize=True)
        shutil.rmtree(full_path)

