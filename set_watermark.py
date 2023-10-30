from PIL import Image, ImageDraw, ImageFont

def watermarkImage(image_path, output_path):
    base_image = Image.open(image_path)
    width, height = base_image.size

    text = "www.elibraryofcambodia.org"
    text_color = (222, 222, 222)
    position = (0, 0)
    font_style = "font/Calibri Regular.ttf"
    font_size = int(width * 0.0248)

    transparent = Image.new('RGBA', (width, height), (255, 255, 255, 0))
    transparent.paste(base_image, position)
    draw = ImageDraw.Draw(transparent)

    font = ImageFont.truetype(font_style, font_size)
    text_bbox = draw.textbbox(position, text, font)
    text_width, text_height = text_bbox[2], text_bbox[3]

    text_position = ((width - text_width) // 2, (height - text_height) // 2)

    text_image = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    text_draw = ImageDraw.Draw(text_image)
    text_draw.text(text_position, text, fill=(text_color[0], text_color[1], text_color[2], 128), font=font)
    transparent = Image.alpha_composite(transparent, text_image)
    transparent.convert('RGB').save(output_path)
