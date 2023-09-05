import os
import basic
import base64
import requests


def get_header():
    credentials = 'seng.vannak:kXhe Acl0 isu6 UzK5 3Al8 yPY4'
    token = base64.b64encode(credentials.encode()).decode('utf-8')
    header_json = {'Authorization': f'Basic {token}'}
    return header_json


def post_media(filename: str) -> any:
    url = 'https://www.elibraryofcambodia.org/wp-json/wp/v2/media'
    header_json = get_header()
    name = basic.get_name_file(filename)
    media = {'file': open(filename, "rb"), 'caption': name, 'title': name}
    res = requests.post(url, headers=header_json, files=media)
    if res.ok:
        body = res.json()
        return {
            'id': body['id'],
            'render': body['guid']['rendered']
        }


def post_newspaper(source: str):
    name = basic.get_name_file(source)
    print(f"start {name}")
    cover = basic.save_pdf_cover(source)
    url = 'https://www.elibraryofcambodia.org/wp-json/wp/v2/document'
    header_json = get_header()
    media = post_media(cover)['id']
    os.remove(cover)
    pdf = post_media(source)
    content = f'[pdfjs-viewer url="{pdf["render"]}" attachment_id="{pdf["id"]}" viewer_width=100% viewer_height=800px fullscreen=true download=true print=true]'
    document = {
        'title': name,
        'content': content,
        'featured_media': media,
        'status': 'publish',
    }
    res = requests.post(url, headers=header_json, data=document)
    print(f'finished f{name} with Id: {res.json()["id"]}')
