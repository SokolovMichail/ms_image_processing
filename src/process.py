import os

from src.file_manager import FileManager
from src.image_manager import ImageManager


def process_single_file(file, cfg):
    # widget_dict['progressbar']['value'] += addition
    ImageManager.transform_image(file,
                                 (cfg['image_settings']['width'], cfg['image_settings']['height']),
                                 cfg['image_settings']['conversion'],
                                 cfg['image_settings']['compression'],
                                 os.path.join(cfg['pathes']['out_folder'], FileManager.get_filename_jpg(file)),
                                 cfg['pathes']['icc_profile'],
                                 cfg['image_settings']['aspect_ratio'])
