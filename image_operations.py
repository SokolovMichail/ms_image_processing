from PIL import Image, ImageCms
import os

def open_image(file_path):
    im = Image.open(file_path)
    return im

def transform_image(image:Image,resolution:(int,int),color_profile,jpeg_quality,out_file):
    image.thumbnail(resolution,Image.ANTIALIAS)
    if (color_profile == 'grayscale'):
        image_res = image.convert('L')
    else:
        image_res = image
    profile = ImageCms.getOpenProfile("Adobe98.icc")
    image_res.save(out_file, "JPEG", quality=jpeg_quality, optimize=True, progressive=True,icc_profile = profile.tobytes())
    return image_res