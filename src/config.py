from pathlib import Path

import yaml
from easydict import EasyDict


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


# This class is essentially the same in all of its instances.
class GlobalConfig(metaclass=SingletonMeta):
    def __init__(self):
        self.path = Path('config.yaml')
        self.options = {}
        self.reset()

    def reset(self):
        if self.path.exists():
            with open(self.path, 'r') as f:
                tmp_dict = yaml.safe_load(f)
        else:
            tmp_dict = {
                'pathes':
                    {
                        'icc_profile': None,
                        'in_folder': None,
                        'out_folder': None,
                    },
                'image_settings':
                    {
                        'width': None,
                        'height': None,
                        'compression': None,
                        'conversion': None,
                        'keep_ar': None
                    }

            }
        self.options = tmp_dict

    def dump(self):
        with open(self.path, 'w') as f:
            yaml.safe_dump(self.options, f)

    def __getitem__(self, item):
        return self.options[item]