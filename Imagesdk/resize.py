from PIL import Image

def resize_image(input_path, output_path, width, height):
    image = Image.open(input_path)
    resized_image = image.resize((width, height))
    resized_image.save(output_path)
