import os
import threading
from watermark import image_to_pdf_with_watermark

class ImagePdfWatermark(threading.Thread):
    def __init__(self, input_path, output_path):
        super().__init__()
        self.input_path = input_path
        self.output_path = output_path

    def run(self):
        image_to_pdf_with_watermark(self.input_path, self.output_path)

def watermarkImagePdfsInDirectory(folder: str):
    if not os.path.exists(f'{folder}/output'):
        os.makedirs(f'{folder}/output')
    pdfs_path = [pdf for pdf in os.listdir(folder) if not pdf.startswith('.')]
    pdfs_path.sort()
    pdfs_path.remove('output')
    threads = []

    for path in pdfs_path:
        input_path = f'{folder}/{path}'
        output_path = f'{folder}/output/{path}'
        thread = ImagePdfWatermark(input_path, output_path)
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print('Completed Image2Pdf-Watermark..')


if __name__ == "__main__":
    dir = "data1"
    watermarkImagePdfsInDirectory(dir)

