import tkinter as tk
import mysql.connector
from tkinter import messagebox, PhotoImage
from tkinter.ttk import *
import turtle

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
        
        if password:
            db = mysql.connector.connect(host='localhost', user=username, password=password, db='college')
            cursor = db.cursor()
        else:

            messagebox.showinfo('Title', 'Input Invalid')

            db = mysql.connector.connect(host='localhost', user=username, db='college')
            cursor = db.cursor()

        save_query = "SELECT * FROM STUDENTS"

        try: 
            cursor.execute(save_query)
            my_result = cursor.fetchall()

            for i in my_result:
                print(i)
            
            self.login_frame.destroy()

            self.create_database_frame()
            
            print("Query Executed Successfully")
        except:
            print("Error occured")
            db.rollback()
            
        
        finally:
            if db.is_connected():
                cursor.close()
                db.close()
                print("MySQL connection is closed.")

    def create_database_frame(self):
        self.window.title("Database Table")
        self.window.geometry(f'{600}x{400}')

        database_frame = tk.Frame(self.window)
        database_frame.grid(row=0, column=0, padx=10, pady=10)
        
        # LABELS
        student_id_label = tk.Label(database_frame, text='Student ID')
        student_id_label.grid(row=0, column=0, pady=10, padx=10)
        student_id_label.config(font=('Helvetica Bold', 10))

        first_name_label = tk.Label(database_frame, text='First Name')
        first_name_label.grid(row=1, column=0, pady=10, padx=10)
        first_name_label.config(font=('Helvetica Bold', 10))

        last_name_label = tk.Label(database_frame, text='Last Name')
        last_name_label.grid(row=2, column=0, pady=10, padx=10)
        last_name_label.config(font=('Helvetica Bold', 10))
        
        course_label = tk.Label(database_frame, text='Course')
        course_label.grid(row=3, column=0, pady=10, padx=10)
        course_label.config(font=('Helvetica Bold', 10))

        

        # FORMS
        student_id = tk.Entry(database_frame, width=30)
        student_id.grid(row=0, column=1,)

        first_name = tk.Entry(database_frame, width=30)
        first_name.grid(row=1, column=1)

        last_name = tk.Entry(database_frame, width=30)
        last_name.grid(row=2, column=1)

        course = tk.Entry(database_frame, width=30)
        course.grid(row=3, column=1)

        
        submit_button = tk.Button(database_frame, text='ADD')
        submit_button.grid(row=0, column=2, padx=25, pady=10, ipadx=35)

        edit_button = tk.Button(database_frame, text='DELETE')
        edit_button.grid(row=0, column=3, padx=25, pady=10, ipadx=35)
        # submit_button['command'] = self.submit
        # submit_button.config(font=('Helvetica Bold', 16))


    
        # edit_button = tk.Button(database_frame, text='EDIT')
        # edit_button.grid(row=7, column=0, padx=10, pady=10, ipadx=50)
        # edit_button['command'] = self.submit
        # edit_button.config(font=('Helvetica Bold', 16))

        # delete_button = tk.Button(database_frame, text='DELETE')
        # delete_button.grid(row=7, column=1, padx=10, pady=10, ipadx=50)
        # delete_button['command'] = self.submit
        # delete_button.config(font=('Helvetica Bold', 16))
        # spacer = tk.Label(database_frame, text='')
        # spacer.grid(row=0, column = 0,columnspan=2)

        

        # username_label = tk.Button(database_frame, text="REMOVE")
        # username_label.config(font=('Helvetica Bold', 16))
        # username_label.grid(row=1, column=3, padx=(40, 0), pady=50)
    
    def drawATriangle(self):

        # SETUP
        turtle.title('PUP MAIN MAP')
        # img = PhotoImage(file='pupicon.png')
        # turtle._Screen._root.iconphoto(True, img)
        wn = turtle.Screen()
        t = turtle.Turtle()

        t.shape('circle')
        t.shapesize(0.5, 0.5)
        wn.bgpic('pup.png')
        wn.update
        
        locations = [(266, 176), (172, 200), (156, 210), (280, 120), (124, 180)]
        coordinate = t.xcor(), t.ycor()
        for i in locations:
            t.penup()
            t.goto(i)
            t.stamp()
            t.penup()
    

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
