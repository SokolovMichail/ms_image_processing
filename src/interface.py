import multiprocessing
import tkinter as tk
from tkinter import filedialog as fd

from src.config import GlobalConfig
from src.file_manager import FileManager
from src.process import process_single_file


class Interface:

    def __init__(self):
        self.cfg = GlobalConfig()
        self.elements_dict = {
            'labels': {},
            'inputs': {},
            'buttons': {}
        }
        self._window = self.__generate_window()
        if self.cfg['image_settings']['aspect_ratio'] is not None:
            self.checkbox_var.set(self.cfg['image_settings']['aspect_ratio'])

    def __generate_window(self):
        # General
        window = tk.Tk()
        window.title("Converter v 0.4.0")
        window.geometry("500x500")
        self.checkbox_var = tk.IntVar()
        self.__place_icc(window)
        self.__place_in_folder(window)
        self.__place_out_folder(window)
        self.__place_width(window)
        self.__place_height(window)
        self.__place_compression(window)
        self.__place_conversion(window)
        self.__place_aspectratio(window)
        self.__place_start_button(window)
        return window

    @property
    def window(self):
        return self._window

    def handle_icc_profile_selection(self):
        self.cfg['pathes']['icc_profile'] = fd.askopenfilename()
        label = self.elements_dict['labels']['icc_profile']
        label['text'] = 'Current icc profile: ' + self.cfg['pathes']['icc_profile']

    def handle_input_folder_selection(self):
        self.cfg['pathes']['in_folder'] = fd.askdirectory()
        label = self.elements_dict['labels']['in_folder']
        label['text'] = 'Current input folder: ' + self.cfg['pathes']['in_folder']

    def handle_output_folder_selection(self):
        self.cfg['pathes']['out_folder'] = fd.askdirectory()
        label = self.elements_dict['labels']['out_folder']
        label['text'] = 'Current output folder: ' + self.cfg['pathes']['out_folder']

    def fill_state(self):
        width = int(self.elements_dict['inputs']['width'].get())
        height = int(self.elements_dict['inputs']['height'].get())
        self.cfg['image_settings']['width'] = width
        self.cfg['image_settings']['height'] = height
        self.cfg['image_settings']['conversion'] = \
            self.elements_dict['inputs']['conversion'].get(
                self.elements_dict['inputs']['conversion'].curselection())
        self.cfg['image_settings']['compression'] = int(self.elements_dict['inputs']['compression'].get())
        self.cfg['image_settings']['aspect_ratio'] = self.checkbox_var.get()
        self.cfg.dump()

    def run_execution_process(self):
        self.fill_state()
        all_files = FileManager.list_all_files_dir(self.cfg['pathes']['in_folder'])
        prepared_args = []
        for f in all_files:
            prepared_args.append((f, self.cfg))
        # widget_dict['progressbar']['value'] = 0
        with multiprocessing.Pool(multiprocessing.cpu_count() - 1) as p:
            # the interface is just a dummy app, it does not make conversions.
            p.starmap(process_single_file, prepared_args)

    # SERVICE
    def __place_icc(self, window):
        # ICC Profile Selection
        label_icc = tk.Label(window,
                             text="Current .icc profile: None")
        label_icc.pack()
        self.elements_dict['labels']['icc_profile'] = label_icc
        button_icc = tk.Button(window,
                               command=lambda: self.handle_icc_profile_selection(),
                               text="Select .icc profile",
                               width=35,
                               height=3
                               )
        button_icc.pack()
        self.elements_dict['buttons']['icc_profile'] = button_icc
        if self.cfg['pathes']['icc_profile'] is not None:
            label_icc['text'] = self.cfg['pathes']['icc_profile']

    def __place_in_folder(self, window):
        # InputFolder Selection
        label_cif = tk.Label(window,
                             text="Current input folder: None")
        label_cif.pack()
        self.elements_dict['labels']['in_folder'] = label_cif

        button_input = tk.Button(window,
                                 command=lambda: self.handle_input_folder_selection(),
                                 text="Select folder with files to be converted",
                                 width=35,
                                 height=3
                                 )
        button_input.pack()
        self.elements_dict['buttons']['in_folder'] = button_input
        if self.cfg['pathes']['in_folder'] is not None:
            label_cif['text'] = self.cfg['pathes']['in_folder']

    def __place_out_folder(self, window):
        # OutputFolder Selection
        key = 'out_folder'
        label_cof = tk.Label(window,
                             text="Current output folder: None")
        label_cof.pack()
        self.elements_dict['labels']['out_folder'] = label_cof

        button_output = tk.Button(window,
                                  command=lambda: self.handle_output_folder_selection(),
                                  text="Select folder where to store converted files",
                                  width=35,
                                  height=3
                                  )
        button_output.pack()
        self.elements_dict['buttons']['out_folder'] = button_output
        if self.cfg['pathes']['out_folder'] is not None:
            label_cof['text'] = self.cfg['pathes']['out_folder']

    def __place_width(self, window):
        label_width = tk.Label(window,
                               text="Input width(integer value) below")
        label_width.pack()
        self.elements_dict['labels']['width'] = label_width
        entry_width = tk.Entry(window)
        entry_width.pack()
        self.elements_dict['inputs']['width'] = entry_width
        if self.cfg['image_settings']['width'] is not None:
            entry_width.delete(0, tk.END)
            entry_width.insert(0, self.cfg['image_settings']['width'])

    def __place_height(self, window):
        label_height = tk.Label(window,
                                text="Input height(integer value) below")
        label_height.pack()
        self.elements_dict['labels']['height'] = label_height

        entry_height = tk.Entry()
        entry_height.pack()
        self.elements_dict['inputs']['height'] = entry_height
        if self.cfg['image_settings']['height'] is not None:
            entry_height.delete(0, tk.END)
            entry_height.insert(0, self.cfg['image_settings']['height'])

    def __place_compression(self, window):
        label_compression = tk.Label(window,
                                     text="Input quality value(1 is lowest, 100 is highest) below")
        label_compression.pack()
        self.elements_dict['labels']['compression'] = label_compression

        entry_comp = tk.Entry()
        entry_comp.pack()
        self.elements_dict['inputs']['compression'] = entry_comp
        if self.cfg['image_settings']['compression'] is not None:
            entry_comp.delete(0, tk.END)
            entry_comp.insert(0, self.cfg['image_settings']['compression'])

    def __place_conversion(self, window):
        OPTIONS = [
            "aRGB",
            "Grayscale",
        ]  # etc

        label_conv = tk.Label(window, text="Select conversion")
        label_conv.pack()
        self.elements_dict['labels']['conversion'] = label_conv

        listbox_conversion = tk.Listbox(selectmode='SINGLE', height=2)
        i = 0
        for opt in OPTIONS:
            listbox_conversion.insert(i, opt)
            i += 1
        listbox_conversion.pack()
        if self.cfg['image_settings']['conversion'] is not None:
            if self.cfg['image_settings']['conversion'] == 'aRGB':
                listbox_conversion.select_set(0)
            else:
                listbox_conversion.select_set(1)
        self.elements_dict['inputs']['conversion'] = listbox_conversion

    def __place_aspectratio(self, window):
        checkbox_aspectratio = tk.Checkbutton(window,
                                              text="Keep aspect ratio?", variable=self.checkbox_var,
                                              onvalue=1, offvalue=0)
        checkbox_aspectratio.pack()
        self.elements_dict['inputs']['aspect_ratio'] = checkbox_aspectratio
        if self.cfg['image_settings']['aspect_ratio']:
            checkbox_aspectratio.select()
        x = self.checkbox_var.get()

    def __place_start_button(self, window):
        button_start = tk.Button(window,
                                 command=lambda: self.run_execution_process(),
                                 text="Start conversion",
                                 width=35,
                                 height=3
                                 )
        button_start.pack()
        self.elements_dict['buttons']['start'] = button_start
