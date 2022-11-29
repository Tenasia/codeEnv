
import tkinter as tk
from tkinter import ttk


class View:
    def __init__(self):
        self.window = tk.Tk()
        self.create_frames()
    def create_frames(self):
        mole_frame = tk.Frame(self.window, bg='red', width=300, height=300)
        mole_frame.grid(row=0, column=0)

        status_frame = tk.Frame(self.window, bg='green', width=150, height=300)
        status_frame.grid(row=0, column=1)
    
def main():
    program = View()

    program.window.mainloop()


if __name__ == '__main__':
    main()