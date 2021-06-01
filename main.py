import os
from pathlib import Path

from file_operations import list_all_files_dir,get_filename_jpg
from image_operations import transform_image

def process_all_files_in_dir(path,resolution,color_profile,jpeg_quality,out_dir):
    files = list_all_files_dir(path)
    for file in files:
        try:
            transform_image(file,
                            resolution,
                            color_profile,
                            jpeg_quality,
                            os.path.join(out_dir,get_filename_jpg(file)))
        finally:
            pass

process_all_files_in_dir("in_folder",(200,200),'aRGB',100,"out_folder")