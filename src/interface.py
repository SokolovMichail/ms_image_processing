import tkinter as tk


class Interface:

    def __init__(self):
        self.elements_dict = {
            'labels': {},
            'inputs': {},
            'buttons': {}
        }
        self.checkbox_var = True
        self.window = self.__generate_window()

    def __generate_window(self):
        # General
        window = tk.Tk()
        window.title("Converter v 0.4.0")
        window.geometry("500x500")

        self.__place_icc(window)
        self.__place_in_folder(window)
        self.__place_out_folder(window)
        self.__place_width(window)
        self.__place_height(window)
        self.__place_compression(window)
        self.__place_conversion(window)
        self.__place_aspectratio(window)
        self.__place_start_button(window)

    @property
    def window(self):
        return self.window

    #SERVICE
    def __place_icc(self, window):
        # ICC Profile Selection
        label_icc = tk.Label(window,
                             text="Current .icc profile: None")
        label_icc.pack()
        self.elements_dict['labels']['icc_profile'] = label_icc
        button_icc = tk.Button(window,
                               command=lambda: handle_icc_profile_selection(state, label_icc),
                               text="Select .icc profile",
                               width=35,
                               height=3
                               )
        button_icc.pack()
        self.elements_dict['buttons']['icc_profile'] = button_icc

    def __place_in_folder(self, window):
        # InputFolder Selection
        label_cif = tk.Label(window,
                             text="Current input folder: None")
        label_cif.pack()
        self.elements_dict['labels']['in_folder'] = label_cif

        button_input = tk.Button(window,
                                 command=lambda: handle_input_folder_selection(state, label_cif),
                                 text="Select folder with files to be converted",
                                 width=35,
                                 height=3
                                 )
        button_input.pack()
        self.elements_dict['buttons']['in_folder'] = button_input

    def __place_out_folder(self, window):
        # OutputFolder Selection
        key = 'out_folder'
        label_cof = tk.Label(window,
                             text="Current output folder: None")
        label_cof.pack()
        self.elements_dict['labels']['out_folder'] = label_cof

        button_output = tk.Button(window,
                                  command=lambda: handle_output_folder_selection(state, label_cof),
                                  text="Select folder where to store converted files",
                                  width=35,
                                  height=3
                                  )
        button_output.pack()
        self.elements_dict['buttons']['out_folder'] = button_output

    def __place_width(self, window):
        label_width = tk.Label(window,
                               text="Input width(integer value) below")
        label_width.pack()
        self.elements_dict['labels']['width'] = label_width

        entry_width = tk.Entry(window)
        entry_width.pack()
        self.elements_dict['inputs']['width'] = entry_width

    def __place_height(self, window):
        label_height = tk.Label(window,
                                text="Input height(integer value) below")
        label_height.pack()
        self.elements_dict['labels']['height'] = label_height


        entry_height = tk.Entry()
        entry_height.pack()
        self.elements_dict['inputs']['height'] = entry_height

    def __place_compression(self, window):
        label_compression = tk.Label(window,
                                     text="Input quality value(1 is lowest, 100 is highest) below")
        label_compression.pack()
        self.elements_dict['labels']['compression'] = label_compression

        entry_comp = tk.Entry()
        entry_comp.pack()
        self.elements_dict['inputs']['compression'] = label_compression

    def __place_conversion(self,window):
        OPTIONS = [
            "aRGB",
            "Grayscale",
        ]  # etc

        label_conv = tk.Label(window,text="Select conversion")
        label_conv.pack()
        self.elements_dict['labels']['conversion'] = label_conv

        listbox_conversion = tk.Listbox(selectmode='SINGLE', height=2)
        i = 0
        for opt in OPTIONS:
            listbox_conversion.insert(i, opt)
            i += 1
        listbox_conversion.pack()
        listbox_conversion.select_set(0)
        self.elements_dict['inputs']['conversion'] = listbox_conversion

    def __place_aspectratio(self,window):
        checkbox_aspectratio = tk.Checkbutton(window,
                                              text="Keep aspect ratio?", variable=self.checkbox_var,
                                              onvalue=True, offvalue=False)
        checkbox_aspectratio.pack()
        self.elements_dict['inputs']['aspectratio']=checkbox_aspectratio

    def __place_start_button(self,window):
        button_start = tk.Button(window,
                                 command=lambda: run_execution_process(state, widgets),
                                 text="Start conversion",
                                 width=35,
                                 height=3
                                 )
        button_start.pack()
        self.elements_dict['buttons']['start'] = button_start

