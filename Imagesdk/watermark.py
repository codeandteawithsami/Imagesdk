from PIL import Image
from PIL import ImageDraw, ImageFont

def add_text_watermark(input_path, output_path, text):
    image = Image.open(input_path)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("arial.ttf", size=36)
    draw.text((10, 10), text, fill="white", font=font)
    image.save(output_path)