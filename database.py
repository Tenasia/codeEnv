import tkinter as tk
import mysql.connector
from tkinter import messagebox, PhotoImage
from tkinter.ttk import *
import turtle
import random

class DataBaseGUI:
    
    X_SIZE_WINDOW = 400
    Y_SIZE_WINDOW = 400

    def __init__(self):
        
        # INITIALIZED VARIABLES
        self.window = tk.Tk()

        # VARIABLES
        self.login_frame, self.login_button, self.username, self.password = self.create_login_frame()

    def create_login_frame(self):
        
        # INITIALIZE VARIABLES
        self.window.resizable(False, False)
        self.window.bind('<Return>', self.login)
        self.img = PhotoImage(file='pupicon.png')
        self.window.iconphoto(False, self.img)
        self.window.geometry(f'{DataBaseGUI.X_SIZE_WINDOW}x{DataBaseGUI.Y_SIZE_WINDOW}')
        self.window.title('CARE-M Login Page')

        self.center(self.window)
        # FRAMES
        login_frame = tk.Frame(self.window, width=600, height=600)
        login_frame.grid(row=0, column=0, ipadx=500)
        
        title_label= tk.Label(login_frame, text="CARE-M DATABASE")
        title_label.config(font=('Helvetica Bold', 16))
        title_label.grid(row=0, columnspan=4, pady=50, ipadx=100, sticky=tk.N+tk.S+tk.W+tk.E)

        username_label = tk.Label(login_frame, text="USERNAME: ")
        username_label.config(font=('Helvetica Bold', 16))
        username_label.grid(row=1, column=0, padx=10, pady=10)
        
        username_info = tk.Entry(login_frame, width=35)
        username_info.grid(row=1, column=1, padx=10, pady=10)

        password_label = tk.Label(login_frame, text="PASSWORD: ")
        password_label.config(font=('Helvetica Bold', 16))
        password_label.grid(row=2, column=0, padx=10, pady=10)
    
        password_info = tk.Entry(login_frame, width=35, show="*")
        password_info.grid(row=2, column=1, padx=10, pady=10)

        login_button = tk.Button(login_frame, text="LOGIN")
        login_button.config(font=('Helvetica Bold', 16))
        login_button.grid(row=3, columnspan=2, padx=10, pady=(25, 0))
        login_button['command'] = self.login

        return login_frame, login_button, username_info, password_info

    def login(self, event=None):

        username = self.username.get()
        password = self.password.get()


        self.login_to_db(username, password)
    def login_to_db(self, username, password):
        
        self.username = username
        self.password = password

        if password:
            db = mysql.connector.connect(host='localhost', user=username, password=password, db='college')
            cursor = db.cursor()
        else:

            messagebox.showinfo('Invalid', 'Input Invalid')

            db = mysql.connector.connect(host='localhost', user=username, db='college')
            cursor = db.cursor()

        try:  
            self.login_frame.destroy()
            self.serial_id, self.first_name, self.last_name, self.remarks, self.location= self.create_database_frame() 
            print("Successfully Logged In")
        except:
            print("Error occured")
            db.rollback()
            
        # finally:
        #     if db.is_connected():
        #         cursor.close()
        #         db.close()
        #         print("MySQL connection is closed.")
    
    def submit(self, event=None):
        
        serial_id = self.serial_id.get()
        surname = self.last_name.get()
        first_name = self.first_name.get()
        remarks = self.remarks.get()
        location = self.location.get()

        db = mysql.connector.connect(host='localhost', user=self.username, password=self.password, db='college')
        cursor = db.cursor()    
        try:
            query = 'INSERT INTO `tb_carem` (`SERIAL_ID`, `SURNAME`, `FIRST_NAME`,`REMARKS`, `LOC`) VALUES (%s, %s, %s, %s, %s);'
            values = (serial_id, surname, first_name, remarks, location)
            cursor.execute(query, values)
            db.commit()
            
            messagebox.showinfo('Successful', 'Inserted Data Successfully.')
            self.serial_id.delete(0, tk.END)
            self.last_name.delete(0, tk.END)
            self.first_name.delete(0, tk.END)
            self.remarks.delete(0, tk.END)
            self.location.delete(0, tk.END)

            self.serial_id.focus_set()
        except Exception as e:
            print(e)
            db.rollback()
            db.close()



        # Deleting the forms after submitting
        


    def create_database_frame(self):
        self.window.title("Database Table")
        self.window.geometry(f'{600}x{400}')
        self.window.bind('<Return>', self.submit)

        database_frame = tk.Frame(self.window)
        database_frame.grid(row=0, column=0, padx=10, pady=10)
        
        # LABELS
        serial_id_label = tk.Label(database_frame, text='Serial ID')
        serial_id_label.grid(row=0, column=0, pady=10, padx=10)
        serial_id_label.config(font=('Helvetica Bold', 10))

        first_name_label = tk.Label(database_frame, text='First Name')
        first_name_label.grid(row=1, column=0, pady=10, padx=10)
        first_name_label.config(font=('Helvetica Bold', 10))

        surname_label = tk.Label(database_frame, text='Last Name')
        surname_label.grid(row=2, column=0, pady=10, padx=10)
        surname_label.config(font=('Helvetica Bold', 10))
        
        remarks_label = tk.Label(database_frame, text='Remarks')
        remarks_label.grid(row=3, column=0, pady=10, padx=10)
        remarks_label.config(font=('Helvetica Bold', 10))

        location_label = tk.Label(database_frame, text='Location')
        location_label.grid(row=4, column=0, pady=10, padx=10)
        location_label.config(font=('Helvetica Bold', 10))

        # FORMS

        serial_id = tk.Entry(database_frame, width=30)
        serial_id.grid(row=0, column=1)

        first_name = tk.Entry(database_frame, width=30)
        first_name.grid(row=1, column=1)

        surname = tk.Entry(database_frame, width=30)
        surname.grid(row=2, column=1)

        remarks = tk.Entry(database_frame, width=30)
        remarks.grid(row=3, column=1)
        
        location = tk.Entry(database_frame, width=30)
        location.grid(row=4, column=1)
        # BUTTONS
        submit_button = tk.Button(database_frame, text='ADD')
        submit_button.grid(row=0, column=2, padx=25, pady=10, ipadx=25)
        submit_button['command'] = self.submit
        
        graph_button = tk.Button(database_frame, text='SHOW GRAPH')
        graph_button.grid(row=0, column=3, padx=25, pady=10, ipadx=25)
        graph_button['command'] = self.graphPoints

        return serial_id, first_name, surname, remarks, location
    def graphPoints(self):

        # SETUP
        turtle.title('PUP MAIN MAP')

        # img = PhotoImage(file='pupicon.png')
        # turtle._Screen._root.iconphoto(True, img)

        wn = turtle.Screen()
        t = turtle.Turtle()

        # t.shape('circle')
        t.shapesize(0.5, 0.5)

        
        
        wn.bgpic('pup.png')
        wn.update()
        
        wn.setworldcoordinates(-250, -250, 250, 250)
        
    

        random_locations = []
        for i in range(10):
            random_x = random.randrange(-250, 250)
            random_y = random.randrange(-250, 250)

            random_locations.append((random_x, random_y))


        # DRAWING

        t.left(90)

        for i in random_locations:
            
            t.penup()
            t.goto(i)
            t.write(i, align='center')
            t.stamp()
            t.pendown()

            if i[0] >= 0 and i[1] >= 0:
                print('First Quadrant')
            elif i[0] <= 0 and i[1] >= 0:
                print('Second Quadrant')
            elif i[0] <= 0 and i[1] <= 0:
                print('Third Quadrant')
            elif i[0] >= 0 and i[1] <= 0:
                print('Fourth Quadrant')

        wn.exitonclick()

    def center(self, win):

        win.update_idletasks()
        width = win.winfo_width()
        frm_width = win.winfo_rootx() - win.winfo_x()
        win_width = width + 2 * frm_width
        height = win.winfo_height()
        titlebar_height = win.winfo_rooty() - win.winfo_y()
        win_height = height + titlebar_height + frm_width

        x = win.winfo_screenwidth() // 2 - win_width // 2
        y = win.winfo_screenheight() // 2 - win_height // 2

        win.geometry('{}x{}+{}+{}'.format(width, height, x, y))


        win.deiconify()

    

def main():
    program = DataBaseGUI()

    program.window.mainloop()

if __name__ == '__main__':
    main()


