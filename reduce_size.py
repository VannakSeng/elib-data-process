import os
import threading
from pdf_compressor import compress

class PdfCompressorThread(threading.Thread):
    def __init__(self, input_path, output_path):
        super().__init__()
        self.input_path = input_path
        self.output_path = output_path

    def run(self):
        compress(self.input_path, self.output_path, power=3)

def compressPdfsInDirectory(folder: str):
    if not os.path.exists(f'{folder}/output'):
        os.makedirs(f'{folder}/output')
    pdfs_path = [pdf for pdf in os.listdir(folder) if not pdf.startswith('.')]
    pdfs_path.sort()
    pdfs_path.remove('output')
    threads = []

    for path in pdfs_path:
        input_path = f'{folder}/{path}'
        output_path = f'{folder}/output/{path}'
        thread = PdfCompressorThread(input_path, output_path)
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == '__main__':
    dir = 'data'
    compressPdfsInDirectory(dir)
