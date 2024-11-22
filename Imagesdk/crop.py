from PIL import Image

def crop_image(input_path, output_path, crop_area):
    image = Image.open(input_path)
    cropped_image = image.crop(crop_area)
    cropped_image.save(output_path)
