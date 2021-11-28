import multiprocessing

from src.interface import Interface

interface = Interface()

if __name__ == '__main__':
    multiprocessing.freeze_support()
    interface.window.mainloop()
