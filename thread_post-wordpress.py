import os
import threading
from posting_wp import post_newspaper

class postWordPressThread(threading.Thread):
    def __init__(self, file_path):
        super().__init__()
        self.file_path = file_path

    def run(self):
        post_newspaper(self.file_path)

def postWordPressInFolder(folder: str):
    pdfs_path = [pdf for pdf in os.listdir(folder) if not pdf.startswith('.')]
    threads = []

    for path in pdfs_path:
        input_path = f'{folder}/{path}'
        thread = postWordPressThread(input_path)
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print('Completed Post to Wordpress...')

if __name__ == '__main__':
    dir = 'data1/output'
    postWordPressInFolder(dir)
