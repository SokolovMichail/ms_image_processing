from PIL import Image, ImageCms
import os

class ImageManager:
    @staticmethod
    def open_image(file_path):
        im = Image.open(file_path)
        return im

    @staticmethod
    def transform_image(image_path, resolution: (int, int), color_profile, jpeg_quality, out_file, icc_profile,
                        keep_aspect_ratio=True):
        image = ImageManager.open_image(image_path)
        if (keep_aspect_ratio):
            image.thumbnail(resolution)
        else:
            image = image.resize(resolution)
        if (color_profile == 'Grayscale'):
            image_res = image.convert('L')
        else:
            image_res = image
        profile = ImageCms.getOpenProfile(icc_profile)
        image_res.save(out_file, "JPEG", quality=jpeg_quality, optimize=True, progressive=True,
                       icc_profile=profile.tobytes())
        return image_res
