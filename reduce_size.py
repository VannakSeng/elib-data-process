import os
import threading
from pdf_compressor import compress
import datetime
import pandas as pd

# Create an empty DataFrame to store the data
data = {'Date': [], 'Filename': [], 'Original (MB)': [], 'Compressed (MB)': []}
df = pd.DataFrame(data)

def get_file_size(file_path):
    return round(os.path.getsize(file_path) / (1024 * 1024), 2)  # Convert bytes to megabytes

def compressPdf(folder: str, filename):
    try:
        file_size_before = get_file_size(filename)
        compress(folder, filename, power=4)
        file_size_after = get_file_size(filename)

        current_datetime = datetime.datetime.now()
        formatted_datetime = current_datetime.strftime("%Y-%b-%d %I:%M%p")
        print(f'{formatted_datetime} : Converted {filename} to pdf')
    except Exception as e:
        print(f"Compression of {filename} failed: {str(e)}")
    finally:
        df.loc[len(df)] = [filename, file_size_before, file_size_after, formatted_datetime]

def compress_all_pdfs_in_folder(folder):
    if not os.path.exists(f'{folder}/output'):
        os.makedirs(f'{folder}/output')
    pdfs_path = [image for image in os.listdir(folder) if not image.startswith('.')]
    pdfs_path.sort()
    pdfs_path.remove('output')
    threads = []

    for path in pdfs_path:
        folder_path = f'{folder}/{path}'
        output_file = f'{folder_path}/output/{path}'

        thread = threading.Thread(target=compressPdf, args=(folder, output_file))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == '__main__':
    dir = 'data'
    compress_all_pdfs_in_folder(dir)
    df.to_csv('pdf_conversion_log.csv', index=False)
