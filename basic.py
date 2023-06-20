import os
import fitz
import base64, requests, json


def browse_files(path: str, current: bool = False) -> list[str]:
    files = []
    for (dirs, dir_names, filenames) in os.walk(path):
        for filename in filenames:
            files.append(f'{dirs}/{filename}')
        if current:
            return files
        for dir_name in dir_names:
            sub_files = browse_files(f'{dirs}/{dir_name}')
            files = files + sub_files
    return files


def get_file_extension(file_path: str) -> str:
    _, file_extension = os.path.splitext(file_path)
    return file_extension


def get_name_file(filename: str) -> str:
    name = os.path.splitext(os.path.basename(filename))[0]
    return name


def get_path(filename: str) -> str:
    return os.path.dirname(os.path.abspath(filename))


def save_pdf_cover(filename: str):
    doc = fitz.open(filename)
    pix = doc[0].get_pixmap(
        matrix=fitz.Identity,
        dpi=None,
        colorspace=fitz.csRGB,
        clip=None,
        alpha=True,
        annots=True)
    path = get_path(filename)
    name = get_name_file(filename)
    pix.save(f"{path}/{name}.png")


def get_header():
    credentials = 'seng.vannak:kXhe Acl0 isu6 UzK5 3Al8 yPY4'
    token = base64.b64encode(credentials.encode()).decode('utf-8')
    header_json = {'Authorization': f'Basic {token}'}
    return header_json


def post_media(filename: str) -> any:
    url = 'https://www.elibraryofcambodia.org/wp-json/wp/v2/media'
    header_json = get_header()
    name = get_name_file(filename)
    media = {'file': open(filename, "rb"), 'caption': name, 'title': name}
    res = requests.post(url, headers=header_json, files=media)
    if res.ok:
        body = res.json()
        return {
            'id': body['id'],
            'render': body['guid']['rendered']
        }


def post_newspaper(filename: str):
    url = 'https://www.elibraryofcambodia.org/wp-json/wp/v2/document'
    header_json = get_header()
    name = get_name_file(filename)
    media = post_media(filename.replace('.pdf', '.png'))['id']
    pdf = post_media(filename)
    content = f'[pdfjs-viewer url="{pdf["render"]}" attachment_id="{pdf["id"]}" viewer_width=100% viewer_height=800px fullscreen=true download=true print=true]'
    document = {
        'title': name,
        'content': content,
        'featured_media': media,
        'status': 'publish',
        "meta": {
            "document-types": [609]
        }
    }
    res = requests.post(url, headers=header_json, data=document)
    print(f'finished {res.json()["id"]}')


path = '/Volumes/Docker/Elib/1_Fonds_Periodicques_Khmer_PDF'
for dir_name in os.listdir(path):
    if (dir_name.endswith('.pdf')):
        filename = f'{path}/{dir_name}'
        # basic.save_pdf_cover(filename)
        post_newspaper(filename)
# post_newspaper('/Volumes/Docker/Elib/1_Fonds_Periodicques_Khmer_PDF/35. Lami de lecole de pali 1ans3.pdf')