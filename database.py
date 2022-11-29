import tkinter as tk
import mysql.connector
from tkinter import *

class DataBaseGUI:
    
    def __init__(self):

        self.window = tk.Tk()
        self.login_frame, self.username, self.password = self.create_login_frame()
        
    def create_login_frame(self):

        self.window.geometry('400x400')
        self.window.title('CARE-M Login Page')
        self.window.bind('<Return>', self.submit_act)

        login_frame = tk.Frame(self.window, width=500, height=500)
        login_frame.grid(row=0, column=0)
        
        title_label= tk.Label(login_frame, text="CARE-M DATABASE", anchor='center')
        title_label.config(font=('Helvetica Bold', 16), pady=50)
        title_label.grid(row=0, columnspan=2, sticky=tk.E + tk.W + tk.N + tk.S)

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

        login_button = tk.Button(self.window, text="LOGIN")
        login_button.config(font=('Helvetica Bold', 16))
        login_button.grid(row=3, columnspan=2, padx=10, pady=10)
        login_button['command'] = self.submit_act

        return login_frame, username_info, password_info
    def submit_act(self, event):
        
        username = self.username.get()
        password = self.password.get()
        
        self.login_to_db(username, password)

    def login_to_db(self, username, password):

        if password:
            db = mysql.connector.connect(host='localhost', user=username, password=password, db='college')
            cursor = db.cursor()
        else:
            db = mysql.connector.connect(host='localhost', user=username, db='college')
            cursor = db.cursor()
        
        save_query = "SELECT * FROM STUDENTS"

        try: 
            cursor.execute(save_query)
            my_result = cursor.fetchall()

            for i in my_result:
                print(i)
            
            print("Query Executed Successfully")
        
        except:
            db.rollback()
            print("Error occured")
        
        finally:
            if db.is_connected():
                cursor.close()
                db.close()
                print("MySQL connection is closed.")
        
        
def main():
    program = DataBaseGUI()

    program.window.mainloop()

if __name__ == '__main__':
    main()
