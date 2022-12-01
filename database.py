import tkinter as tk
import mysql.connector
from tkinter import *
from tkinter.ttk import *

class DataBaseGUI:
    
    X_SIZE_WINDOW = 680
    Y_SIZE_WINDOW = 480

    def __init__(self):

        self.window = tk.Tk()
        self.login_frame, self.login_button, self.username, self.password = self.create_login_frame()
        
        # self.window.resizable(False, False)

    def create_login_frame(self):

        

        self.window.geometry(f'{DataBaseGUI.X_SIZE_WINDOW}x{DataBaseGUI.Y_SIZE_WINDOW}')
        self.window.title('CARE-M Login Page')

        login_frame = tk.Frame(self.window, width=400, height=400)
        login_frame.grid(row=0, column=0)
        
        title_label= tk.Label(login_frame, text="CARE-M DATABASE")
        title_label.config(font=('Helvetica Bold', 16), pady=50)
        title_label.grid(row=0, columnspan=2)

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
        login_button.grid(row=3, columnspan=2, padx=10, pady=10)
        login_button['command'] = self.submit_act



        return login_frame, login_button, username_info, password_info
    def submit_act(self, event=None):
        
        username = self.username.get()
        password = self.password.get()
        
        
        self.login_to_db(username, password)

    def login_to_db(self, username, password):

        # if password:
        #     db = mysql.connector.connect(host='localhost', user=username, password=password, db='college')
        #     cursor = db.cursor()
        # else:
        #     db = mysql.connector.connect(host='localhost', user=username, db='college')
        #     cursor = db.cursor()
        
        # save_query = "SELECT * FROM STUDENTS"

        try: 
            # cursor.execute(save_query)
            # my_result = cursor.fetchall()

            # for i in my_result:
            #     print(i)
            
            
            self.login_frame.destroy()


            self.create_database_frame()
            
            print("Query Executed Successfully")
        except:
            # db.rollback()
            print("Error occured")
        
        finally:
            print('Stuff')
            # if db.is_connected():
            #     cursor.close()
            #     db.close()
            #     print("MySQL connection is closed.")

    def create_database_frame(self):
        self.window.title("Database Table")
        self.window.geometry(f'{DataBaseGUI.X_SIZE_WINDOW}x{DataBaseGUI.Y_SIZE_WINDOW}')

        login_frame = tk.Frame(self.window, width=400, height=400)
        login_frame.grid(row=0, column=3, columnspan=4)
        
        spacer = tk.Label(login_frame, text='')
        spacer.grid(row=0, column = 0,columnspan=2)

        title_label= tk.Button(login_frame, text="ADD")
        title_label.config(font=('Helvetica Bold', 16), anchor='NE')
        title_label.grid(row=1, column=2, padx=0, pady=50)

        username_label = tk.Button(login_frame, text="REMOVE")
        username_label.config(font=('Helvetica Bold', 16), anchor='NE')
        username_label.grid(row=1, column=3, padx=0, pady=50)
        
        # username_info = tk.Entry(login_frame, width=35)
        # username_info.grid(row=1, column=1, padx=10, pady=10)

        # password_label = tk.Label(login_frame, text="PASSWORD: ")
        # password_label.config(font=('Helvetica Bold', 16))
        # password_label.grid(row=2, column=0, padx=10, pady=10)
    
        # password_info = tk.Entry(login_frame, width=35, show="*")
        # password_info.grid(row=2, column=1, padx=10, pady=10)    
        
def main():
    program = DataBaseGUI()

    program.window.mainloop()

if __name__ == '__main__':
    main()
