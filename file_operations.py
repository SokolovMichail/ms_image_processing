import os

def list_all_files_dir(path):
    res = []
    for file in os.listdir(path):
        if (file.endswith(".tiff") or file.endswith(".png") or file.endswith(".bmp")):
            res.append(os.path.join(path, file))
    return res

def get_filename_jpg(path):
    return os.path.basename(path).split('.')[0] + ".jpg"

