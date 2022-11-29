import tkinter as tk
from tkinter import ttk, PhotoImage, messagebox
from random import randint

class WhackAMole:

    MOLES_IN_THE_GRID = 3
    STATUS_BACKGROUND = 'white'

    MIN_TIME_DOWN = 1000
    MAX_TIME_DOWN = 5000
    MIN_TIME_UP = 1000
    MAX_TIME_UP = 3000
    def __init__(self):
        self.window = tk.Tk()
        self.mole_frame, self.status_frame = self.create_frames()
        
        self.mole_photo = PhotoImage(file='D:\Downloads\codeEnv\ch15\mole.png')
        self.mole_cover_photo = PhotoImage(file='D:\Downloads\codeEnv\ch15\mole_cover.png')

        self.mole_labels = self.create_moles()
        self.label_timers = {}

        self.hit_counter, self.miss_counter, self.start_button, self.quit_button = self.create_status_widgets()
       
        self.set_callbacks()

        self.game_is_running = False

    def create_frames(self):
        mole_frame = tk.Frame(self.window, bg='red', width=300, height=300)
        mole_frame.grid(row=0, column=0)

        status_frame = tk.Frame(self.window, bg='green', width=150, height=300)
        status_frame.grid(row=0, column=1, sticky=tk.N + tk.S + tk.E + tk.W)


        return mole_frame, status_frame
    def create_moles(self):

        mole_buttons = []
        for row in range(WhackAMole.MOLES_IN_THE_GRID):
            row_of_buttons = []
            for col in range(WhackAMole.MOLES_IN_THE_GRID):
                mole_button = tk.Button(self.mole_frame, image=self.mole_photo)
                mole_button.grid(row=row, column=col, padx=8, pady=8)

                row_of_buttons.append(mole_button)
            
            mole_buttons.append(row_of_buttons)
            
        return mole_buttons
    
    def create_status_widgets(self):
        
        self.spacer()

        hit_label = tk.Label(self.status_frame, text='Number of hits', bg=WhackAMole.STATUS_BACKGROUND)
        hit_label.pack(side='top', fill=tk.Y, expand=True)

        hit_counter = tk.Label(self.status_frame, text='0', bg=WhackAMole.STATUS_BACKGROUND)
        hit_counter.pack(side='top', fill=tk.Y, expand=True)

        miss_label = tk.Label(self.status_frame, text='Number of misses', bg=WhackAMole.STATUS_BACKGROUND)
        miss_label.pack(side='top', fill=tk.Y, expand=True)

        miss_counter = tk.Label(self.status_frame, text='0', bg=WhackAMole.STATUS_BACKGROUND)
        miss_counter.pack(side='top', fill=tk.Y, expand=True)

        self.spacer()

        start_button = tk.Button(self.status_frame, text='Start', bg=WhackAMole.STATUS_BACKGROUND)
        start_button.pack(side='top', fill=tk.Y, expand=True)

        self.spacer()

        quit_button = tk.Button(self.status_frame, text='Quit', bg=WhackAMole.STATUS_BACKGROUND)
        quit_button.pack(side='top', fill=tk.Y, expand=True)

        self.spacer()

        return hit_counter, miss_counter, start_button, quit_button
    
    def spacer(self):
        spacer = tk.Label(self.status_frame, text='', bg=WhackAMole.STATUS_BACKGROUND)
        spacer.pack(side='top', fill=tk.Y, expand=True)

    def set_callbacks(self):
        for row in range(WhackAMole.MOLES_IN_THE_GRID):
            for col in range(WhackAMole.MOLES_IN_THE_GRID):
                self.mole_labels[row][col].bind("<ButtonPress-1>", self.mole_hit)
        self.start_button['command'] = self.start
        self.quit_button['command'] = self.quit   

    def mole_hit(self, event):
        if self.game_is_running:
            hit_label = event.widget
            if hit_label['image'] == self.mole_cover_photo.name:
                self.miss_counter['text'] = str(int(self.miss_counter['text']) + 1)
            else: 
                self.hit_counter['text'] = str(int(self.hit_counter['text']) + 1 )
                self.put_down_mole(hit_label, False)

    def start(self):
        if self.start_button['text'] == 'Start':
            for row in range(WhackAMole.MOLES_IN_THE_GRID):
                for col in range(WhackAMole.MOLES_IN_THE_GRID):
                    the_label = self.mole_labels[row][col]
                    the_label['image'] = self.mole_cover_photo
                    
                    time_down = randint(WhackAMole.MIN_TIME_DOWN, WhackAMole.MAX_TIME_DOWN)
                    timer_object = the_label.after(time_down, self.pop_up_mole, the_label)

                    self.label_timers[id(the_label)] = timer_object

            self.game_is_running = True
            self.start_button['text'] = 'Stop'
            
            self.hit_counter['text'] = '0'
            self.miss_counter['text'] = '0'

        else:
            for row in range(WhackAMole.MOLES_IN_THE_GRID):
                for col in range(WhackAMole.MOLES_IN_THE_GRID):
                    the_label = self.mole_labels[row][col]

                    the_label['image'] = self.mole_photo

                    the_label.after_cancel(self.label_timers[id(the_label)])

            self.game_is_running = False
            self.start_button['text'] = 'Start'
    
    def put_down_mole(self, the_label, timer_expired):
        if self.game_is_running:
            if timer_expired:
                self.miss_counter['text'] = str(int(self.miss_counter['text']) + 1)
            else:
                the_label.after_cancel(self.label_timers[id(the_label)])
            
            the_label['image'] = self.mole_cover_photo

            time_down = randint(WhackAMole.MIN_TIME_DOWN, WhackAMole.MAX_TIME_DOWN)
            timer_object = the_label.after(time_down, self.pop_up_mole, the_label)

            self.label_timers[id(the_label)] = timer_object

    def pop_up_mole(self, the_label):
        the_label['image'] = self.mole_photo

        if self.game_is_running:
            time_up = randint(WhackAMole.MIN_TIME_UP, WhackAMole.MAX_TIME_UP)
            timer_object = the_label.after(time_up, self.put_down_mole, the_label, True)
            self.label_timers[id(the_label)] = timer_object

    def quit(self):
        really_quit = messagebox.askyesno("Quitting?", "Are you really quitting?")
        if really_quit:
            self.window.destroy
def main():
    program = WhackAMole()

    program.window.mainloop()

if __name__ == '__main__':
    main()