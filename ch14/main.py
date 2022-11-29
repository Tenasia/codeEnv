import tkinter as tk
from tkinter import ttk, PhotoImage, messagebox
from random import randint

class WhackAMole:
    STATUS_BACKGROUND = "white"
    NUM_MOLES_ACCROSS = 3

    MIN_TIME_DOWN = 1000
    MAX_TIME_DOWN = 5000

    MIN_TIME_UP = 1000
    MAX_TIME_UP = 3000

    def __init__(self):
        self.window = tk.Tk()

        self.mole_frame, self.status_frame = self.create_frames()
        
        self.mole_photo = PhotoImage(file='D:\Downloads\codeEnv\ch14\mole.png')
        self.mole_cover_photo = PhotoImage(file='D:\Downloads\codeEnv\ch14\mole_cover.png')

        self.label_timers = {}
        self.mole_buttons = self.create_moles()
        
        self.hit_counter, self.miss_counter, self.start_button, self.quit_button = self.create_status_widgets()

        self.set_callbacks()

        self.game_is_running = False

    def create_frames(self):
        mole_frame = tk.Frame(self.window, bg='maroon', width=300, height=300)
        mole_frame.grid(row=0, column=0)

        status_frame = tk.Frame(self.window, bg='darkgreen', width=100, height=300, )
        status_frame.grid(row=0, column=1, sticky=tk.N + tk.S)

        return mole_frame, status_frame

    def create_moles(self):
        mole_buttons = []

        for column in range(WhackAMole.NUM_MOLES_ACCROSS):
            row_of_buttons = []
            for row in range(WhackAMole.NUM_MOLES_ACCROSS):
                mole_button = tk.Button(self.mole_frame, image=self.mole_photo)
                mole_button.grid(row=row, column=column, padx=8, pady=8)

                row_of_buttons.append(mole_button)

            mole_buttons.append(row_of_buttons)
        return mole_buttons
    
    def create_status_widgets(self):

        self.spacer()  

        hit_label = tk.Label(self.status_frame, text="Number of Hits", bg=WhackAMole.STATUS_BACKGROUND)
        hit_label.pack(side="top", fill=tk.Y, expand=True)

        hit_counter = tk.Label(self.status_frame, text="0", bg=WhackAMole.STATUS_BACKGROUND)
        hit_counter.pack(side="top", fill=tk.Y, expand=True)

        miss_label = tk.Label(self.status_frame, text="Number of Misses", bg=WhackAMole.STATUS_BACKGROUND)
        miss_label.pack(side="top", fill=tk.Y, expand=True)
        
        miss_counter = tk.Label(self.status_frame, text="0", bg=WhackAMole.STATUS_BACKGROUND)
        miss_counter.pack(side="top", fill=tk.Y, expand=True)

        self.spacer()  

        start_button = tk.Button(self.status_frame, text="Start", bg=WhackAMole.STATUS_BACKGROUND)
        start_button.pack(side="top", fill=tk.Y, expand=True, ipadx=10)

        self.spacer()    

        quit_button = tk.Button(self.status_frame, text="Quit", bg=WhackAMole.STATUS_BACKGROUND)
        quit_button.pack(side="top", fill=tk.Y, expand=True, ipadx=10)

        self.spacer()


        return hit_counter, miss_counter, start_button, quit_button
    
    def spacer(self):
        spacer = tk.Label(self.status_frame, text="", bg=WhackAMole.STATUS_BACKGROUND)
        spacer.pack(side="top", fill=tk.Y, expand=True)

    def set_callbacks(self):
        print(self.mole_buttons)

        for row in range(WhackAMole.NUM_MOLES_ACCROSS):
            for column in range(WhackAMole.NUM_MOLES_ACCROSS):
                self.mole_buttons[row][column].bind("<ButtonPress-1>", self.mole_hit)

        
        self.start_button['command'] = self.start
        self.quit_button['command'] = self.quit

    def mole_hit(self, event):
        
        if self.game_is_running:
            hit_label = event.widget
            if hit_label['image'] == self.mole_cover_photo.name:
                # Missed! now update the miss counter
                self.miss_counter['text'] = str(int(self.miss_counter['text']) + 1)
            else:
                self.hit_counter['text'] = str(int(self.hit_counter['text']) + 1)
                self.put_down_mole(hit_label, False)
    
    def start(self):
        if self.start_button['text'] == 'Start':
            # Change all the mole images to a blank image and
            # set a random time for the moles to re-appear on each label.
            for row in range(WhackAMole.NUM_MOLES_ACCROSS):
                for column in range(WhackAMole.NUM_MOLES_ACCROSS):
                    the_label = self.mole_buttons[row][column]
                    the_label['image'] = self.mole_cover_photo
                    
                    time_down = randint(WhackAMole.MIN_TIME_DOWN, WhackAMole.MAX_TIME_DOWN)
                    timer_object = the_label.after(time_down, self.pop_up_mole, the_label)

                    self.label_timers[id(the_label)] = timer_object

            self.game_is_running = True
            self.start_button['text'] = 'Stop'

            self.hit_counter['text'] = '0'
            self.miss_counter['text'] = '0'

        else:
            # The game is running, so stop the game and reset everything
            # Show every mole and stop all the timers.

            for row in range(WhackAMole.NUM_MOLES_ACCROSS):
                for column in range(WhackAMole.NUM_MOLES_ACCROSS):
                    the_label = self.mole_buttons[row][column]
                    # Show the mole
                    the_label['image'] = self.mole_photo
                    # Delete any timer that is associated with the mole.
                    the_label.after_cancel(self.label_timers[id(the_label)])
            
            self.game_is_running = False
            self.start_button['text'] = 'Start'
    
    def put_down_mole(self, the_label, timer_expired):

        if self.game_is_running:
            if timer_expired:
                # The mole is going down before it was clicked on, so update the miss count
                self.miss_counter['text'] = str(int(self.miss_counter['text']) + 1)
            else:
                # The timer did not expire, so manually stop the timer
                the_label.after_cancel(self.label_timers[id(the_label)])

            # Make the mole invisible
            the_label['image'] = self.mole_cover_photo
            
            # Set a call to pop up the mole in the future
            time_down = randint(WhackAMole.MIN_TIME_DOWN, WhackAMole.MAX_TIME_DOWN)
            timer_object = the_label.after(time_down, self.pop_up_mole, the_label)
            
            # Remember the timer object so it can be canceled later, if need be
            self.label_timers[id(the_label)] = timer_object
    
    def pop_up_mole(self, the_label):
        # Show the mole on the screen

        the_label['image'] = self.mole_photo

        if self.game_is_running:
            # Set a call to make it dissapear in the future
            time_up = randint(WhackAMole.MIN_TIME_UP, WhackAMole.MAX_TIME_UP)
            timer_object = the_label.after(time_up, self.put_down_mole, the_label, True)
        
            self.label_timers[id(the_label)] = timer_object

    def quit(self):
        quit_warning = messagebox.askyesno("Quitting?", "Do you really want to quit?")
        if quit_warning:
            self.window.destroy

def main():
    program = WhackAMole()

    program.window.mainloop()

if __name__ == '__main__':
    main()