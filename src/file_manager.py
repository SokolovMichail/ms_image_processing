from pathlib import Path


class FileManager():

    @staticmethod
    def list_all_files_dir(path):
        res = []

        for file in Path(path).glob(r'\S*\.(tiff|bmp)'):
            res.append(Path(path)/file)
        return res

    @staticmethod
    def get_filename_jpg(path):
        return Path(path).rename(Path(path).with_suffix('jpg'))