import tkinter as tk
import mysql.connector
from tkinter import messagebox, PhotoImage
from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
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
        # self.img = PhotoImage(file='pupicon.png')
        # self.window.iconphoto(False, self.img)
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
        
        self.username1 = username
        self.password1 = password

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

    def create_database_frame(self):

        self.window.title("Database Table")
        self.window.geometry(f'{800}x{500}')
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

        location_label =  tk.Label(database_frame, text='Location')
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

        # CRUD BUTTONS
        submit_button = tk.Button(database_frame, text='ADD')
        submit_button.grid(row=0, column=2, padx=25, pady=10, ipadx=25)
        submit_button['command'] = self.submit
        
        update_button = tk.Button(database_frame, text='UPDATE')
        update_button.grid(row=1, column=2, padx=25, pady=10, ipadx=25)
        update_button['command'] = self.update

        delete_button = tk.Button(database_frame, text='DELETE')
        delete_button.grid(row=2, column=2, padx=25, pady=10, ipadx=25)
        delete_button['command'] = self.delete

        graph_button = tk.Button(database_frame, text='SHOW GRAPH')
        graph_button.grid(row=0, column=3, padx=25, pady=10, ipadx=25)
        graph_button['command'] = self.graphPoints

        # self.show()

        # show_button = tk.Button(database_frame, text='SHOW TABLE')
        # show_button.grid(row=1, column=3, padx=25, pady=10, ipadx=25)
        # show_button['command'] = self.show
        # TABLE
        
        self.create_tree()

        return serial_id, first_name, surname, remarks, location

    def create_tree(self):

        columns = ('ID', 'SERIAL_ID', 'FIRST_NAME', 'SURNAME', 'DATE_TIME', 'LOC', 'REMARKS')
        
        self.tree = ttk.Treeview(self.window, columns=columns, show='headings')

        scrollbar = ttk.Scrollbar(self.window, orient='vertical', command=self.tree.yview)

        self.tree.configure(yscrollcommand=scrollbar.set)

        for column in columns:
            self.tree.heading(column, text=column)
            if column == 'DATE_TIME':
                self.tree.column(str(column), width=150)
            else:
                self.tree.column(str(column), width=100)
        
        self.tree.grid(row=5, column=0, sticky=tk.NSEW, padx=(25, 0))

        scrollbar.grid(row=5, column=7, sticky=tk.N + tk.S)

        self.show()
    
    def show(self):

        # Clears the table
        self.clear_all()

        db = mysql.connector.connect(host='localhost', user=self.username1, password=self.password1, db='college')
        cursor = db.cursor()    

        try:
            query = 'SELECT ID,SERIAL_ID,FIRST_NAME,SURNAME,DATE_TIME,LOC,REMARKS FROM tb_carem'
            cursor.execute(query)
            records = cursor.fetchall()

            for info in records:
                self.tree.insert('', tk.END, values=info)
        
        except Exception as e:
            print(e)
            db.rollback()
            db.close()

    def submit(self, event=None):

        db = mysql.connector.connect(host='localhost', user=self.username1, password=self.password1, db='college')
        cursor = db.cursor()    
        try:
            serial_id = int(self.serial_id.get())
            surname = self.last_name.get()
            first_name = self.first_name.get()
            remarks = self.remarks.get()
            location = self.location.get()

            if not serial_id or not surname or not first_name or not remarks or not location:
                messagebox.showerror('Submit Invalid', 'Please Fill in all the fields.')
            else:
                duplicate = self.check_duplicate(serial_id)
                if duplicate:
                    messagebox.showerror("Error", "Duplicate 'Serial ID' Value Entered, Please Enter A Different Value.")

                query = 'INSERT INTO `tb_carem` (`SERIAL_ID`, `SURNAME`, `FIRST_NAME`,`REMARKS`, `LOC`) VALUES (%s, %s, %s, %s, %s);'
                values = (serial_id, surname, first_name, remarks, location)
                cursor.execute(query, values)

                query_1 = 'SELECT ID,SERIAL_ID,FIRST_NAME,SURNAME,DATE_TIME,LOC,REMARKS FROM tb_carem'
                cursor.execute(query_1)
                records = cursor.fetchall()
               
                self.clear_all()
                
                for info in records:
                    self.tree.insert('', 0, text='new item.', values=info)
                db.commit()
                
                messagebox.showinfo('Successful', 'Inserted Data Successfully.')
                self.serial_id.delete(0, tk.END)
                self.last_name.delete(0, tk.END)
                self.first_name.delete(0, tk.END)
                self.remarks.delete(0, tk.END)
                self.location.delete(0, tk.END)

                self.serial_id.focus_set()
   
        except mysql.connector.Error as error:
            print("Failed to retrieve column: {}".format(error))

            if error.errno == 1062:
                messagebox.showerror('Adding Invalid', 'Duplicate Serial ID')
            if error.errno == 1416:
                messagebox.showerror('Adding Invalid', 'Serial ID Cannot Contain String')
        finally:
            if db.is_connected():
                cursor.close()
                db.close()
    
    def update(self):
        
        
        serial_id = self.serial_id.get()
        surname = self.last_name.get()
        first_name = self.first_name.get()
        remarks = self.remarks.get()
        location = self.location.get()
    
        item = self.tree.item(self.tree.focus())

        id = item['values'][0]

        date = item['values'][4]
        db = mysql.connector.connect(host='localhost', user=self.username1, password=self.password1, db='college')
        cursor = db.cursor() 

        
        
        try:
            if not serial_id or not surname or not first_name or not remarks or not location:
                messagebox.showerror('Update Invalid', 'Please Fill in all the fields.')
            else:

                result = messagebox.askyesno("Warning", "Are you sure you want to update this item?")
                if result:
                    if item:
                        
                        query_1 = "UPDATE tb_carem SET SERIAL_ID=%s, FIRST_NAME=%s, SURNAME=%s, LOC=%s, REMARKS=%s WHERE id=%s"
                        values = (serial_id, first_name, surname, location, remarks, id)
                        cursor.execute(query_1, values)

                        query_2 = 'SELECT ID,SERIAL_ID,FIRST_NAME,SURNAME,DATE_TIME,LOC,REMARKS FROM tb_carem'
                        
                        cursor.execute(query_2)
                        records = cursor.fetchall()

                        self.clear_all()
                        for info in records:
                            self.tree.insert('', tk.END, values=info)

                        messagebox.showinfo('Update Successful', f'Item with the ID: {id} was updated.')
                        
                        db.commit()

                        # Update the Treeview with the new data
                        self.tree.item(item, values=(id, serial_id, first_name, surname, date, location, remarks))
                
        except mysql.connector.Error as error:
            print("Failed to retrieve column: {}".format(error))

            if error.errno == 1062:
                messagebox.showerror('Update Invalid', 'Duplicate Serial ID')
            if error.errno == 1416:
                messagebox.showerror('Update Invalid', 'Serial ID Cannot Contain String')

        # except tk.TclError:
        #     # Show an error message or do something else
            
        finally:
            if db.is_connected():
                cursor.close()
                db.close()
        

    
    def delete(self):
        
        item = self.tree.selection()[0]
        print(item)
        data = self.tree.item(item)['values']
        print(data)
        
        id = data[0]

        db = mysql.connector.connect(host='localhost', user=self.username1, password=self.password1, db='college')
        cursor = db.cursor() 

        try:
            result = messagebox.askyesno("Warning", "Are you sure you want to delete this item?")

            if result:
                cursor.execute("DELETE FROM tb_carem WHERE ID=%s", (id,))
                db.commit()
                self.tree.delete(item)
                messagebox.showinfo('Delete Successful', f'Item with the ID: {id} was deleted')
            else:
                pass

        except:
            print('Something gone wrong.')

        finally:
            if db.is_connected():
                cursor.close()
                db.close()
        

    def graphPoints(self):

        # SETUP
        turtle.title('PUP MAIN MAP')

        # img = PhotoImage(file='pupicon.png')
        # turtle._Screen._root.iconphoto(True, img)

        wn = turtle.Screen()
        t = turtle.Turtle()

        # t.shape('circle')
        t.shapesize(0.5, 0.5)

        
        
        wn.bgpic('C:\Downloads\codeEnv-main (3)\codeEnv-main\pup.png')
        wn.update()
        
        wn.setworldcoordinates(-250, -250, 250, 250)
        
    

        locations = self.get_column_as_a_list('LOC')
      


        # DRAWING

        t.left(90)

        for i in locations:
            
            coordinate = i.split(', ')
            x = float(coordinate[0])
            y = float(coordinate[1])
            

            t.penup()
            t.goto(x, y)
            t.write(i, align='center')
            t.stamp()
            t.pendown()

            if x >= 0 and y >= 0:
                print('First Quadrant')
            elif x <= 0 and y >= 0:
                print('Second Quadrant')
            elif x <= 0 and y <= 0:
                print('Third Quadrant')
            elif x >= 0 and y <= 0:
                print('Fourth Quadrant')

        wn.exitonclick()

    def clear_all(self):

        for item in self.tree.get_children():
            self.tree.delete(item)
    
    def check_duplicate(self, value):
        try:
            # Connect to the database
            mydb = mysql.connector.connect(
                host="localhost",
                user=self.username1,
                password=self.password1,
                database='college'
            )
            mycursor = mydb.cursor()
            
            # check if value already exists in the table
            sql = "SELECT 1 FROM tb_carem WHERE SERIAL_ID = %s"
            mycursor.execute(sql, (value))
            result = mycursor.fetchone()
            
            if result:
                return True
            else:
                return False

        except mysql.connector.Error as error:
            print("Failed to check duplicate value: {}".format(error))

        finally:
            if mydb.is_connected():
                mycursor.close()
                mydb.close()

    def get_column_as_a_list(self, column):
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user=self.username1,
                password=self.password1,
                database='college'
            )
            mycursor = mydb.cursor()
            
            # Retrieve the specified column from the table
            sql = "SELECT {} FROM tb_carem".format(column)
            mycursor.execute(sql)
            result = mycursor.fetchall()

            # Convert the result to a list
            column_list = [row[0] for row in result]


            return column_list

        except mysql.connector.Error as error:
            print("Failed to retrieve column: {}".format(error))
        finally:
            if mydb.is_connected():
                mycursor.close()
                mydb.close()

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


