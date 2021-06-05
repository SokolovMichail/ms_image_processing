import os
from tkinter import filedialog as fd

from file_operations import list_all_files_dir, get_filename_jpg
from image_operations import transform_image


def handle_input_folder_selection(state,label):
    state['in_folder'] =  fd.askdirectory()
    label['text'] = 'Current input folder: ' + state['in_folder']

def handle_output_folder_selection(state,label):
    state['out_folder'] =  fd.askdirectory()
    label['text'] = 'Current output folder: ' + state['out_folder']

def fill_state(state,widget_dict):
    width = int(widget_dict['entry_width'].get())
    height = int(widget_dict['entry_height'].get())
    state['new_size'] = (width,height)
    state['conversion'] = widget_dict['listbox_conversion'].get(widget_dict['listbox_conversion'].curselection())
    state['compression'] = int(widget_dict['entry_width'].get())


def run_execution_process(state,widget_dict):
    fill_state(state,widget_dict)
    all_files = list_all_files_dir(state['in_folder'])
    addition = 100 / len(all_files)
    widget_dict['progressbar']['value'] = 0

    for file in list_all_files_dir(state['in_folder']):
        widget_dict['progressbar']['value'] += addition
        transform_image(file,
                        state['new_size'],
                        state['conversion'],
                        state['compression'],
                        os.path.join(state['out_folder'], get_filename_jpg(file)))

