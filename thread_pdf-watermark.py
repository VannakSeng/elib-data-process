import os
import threading
from watermark import pdf_set_watermark, pdf_set_watermark_JBIG2Decode

class PdfWatermark(threading.Thread):
    def __init__(self, input_path, output_path, isJBIG2Decode=False):
        super().__init__()
        self.input_path = input_path
        self.output_path = output_path
        self.isJBIG2Decode = isJBIG2Decode

    def run(self):
        if self.isJBIG2Decode is True:
            pdf_set_watermark_JBIG2Decode(self.input_path, self.output_path)
        else:
            pdf_set_watermark(self.input_path, self.output_path)

def watermarkPdfsInDirectory(folder: str, isJBIG2Decode):
    if not os.path.exists(f'{folder}/output'):
        os.makedirs(f'{folder}/output')
    pdfs_path = [pdf for pdf in os.listdir(folder) if not pdf.startswith('.')]
    pdfs_path.sort()
    pdfs_path.remove('output')
    threads = []

    for path in pdfs_path:
        input_path = f'{folder}/{path}'
        output_path = f'{folder}/output/{path}'
        thread = PdfWatermark(input_path, output_path, isJBIG2Decode)
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print('Completed PDFxWatermark...')


if __name__ == "__main__":
    dir = "data"
    watermarkPdfsInDirectory(dir, isJBIG2Decode=False)

