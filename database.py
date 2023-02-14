import tkinter as tk
import mysql.connector
from tkinter import messagebox, PhotoImage
from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import turtle
import random
import numpy as np

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
        try:
            if password:
                db = mysql.connector.connect(host='localhost', user=username, password=password, db='college')
                cursor = db.cursor()
            else:

                messagebox.showinfo('Invalid', 'Input Invalid')

                db = mysql.connector.connect(host='localhost', user=username, db='college')
                cursor = db.cursor()

        except mysql.connector.Error as error:
            
            if error.errno == 1045:
                messagebox.showinfo('Invalid', 'Input Invalid')
                
                db = mysql.connector.connect(host='localhost', user=username, db='college')
                cursor = db.cursor()

        try:  
            self.login_frame.destroy()
            self.serial_id, self.first_name, self.last_name, self.remarks, self.x_coordinate, self.y_coordinate= self.create_database_frame() 
            print("Successfully Logged In")
        except:
            print("Error occured")
            db.rollback()

    def create_database_frame(self):
        
        # menu_bar = tk.Menu(self.window)
        # menu = tk.Menu(menu_bar, tearoff=0)
        # # menu_bar.add_command(label='Open Turtle Window', command=self.graphPoints)
        # # menu_bar.add_command(label='Graph Points', command=self.graphPoints)
        # # menu_bar.add_command(label='Show Statistics', command=self.graphPoints)
        # self.window.config(menu=menu_bar)

        self.window.title("Database Table")
        self.window.geometry(f'{800}x{550}')
        self.window.bind('<Return>', self.submit)

        self.center(self.window)

        database_frame = tk.Frame(self.window)
        database_frame.grid(row=0, column=0, padx=10, pady=10)
        
        # LABELS
        serial_id_label = tk.Label(database_frame, text='Serial ID', width=15, height=2)
        serial_id_label.grid(row=0, column=0, pady=10, padx=10)
        serial_id_label.config(font=('Helvetica Bold', 10))

        first_name_label = tk.Label(database_frame, text='First Name', width=15, height=2)
        first_name_label.grid(row=1, column=0, pady=10, padx=10)
        first_name_label.config(font=('Helvetica Bold', 10))

        surname_label = tk.Label(database_frame, text='Last Name', width=15, height=2)
        surname_label.grid(row=2, column=0, pady=10, padx=10)
        surname_label.config(font=('Helvetica Bold', 10))
        
        remarks_label = tk.Label(database_frame, text='Remarks', width=15, height=2)
        remarks_label.grid(row=3, column=0, pady=10, padx=10)
        remarks_label.config(font=('Helvetica Bold', 10))

        location_x = tk.Label(database_frame, text='Location: X', width=15, height=2)
        location_x.grid(row=4, column=0, pady=10, padx=10)
        location_x.config(font=('Helvetica Bold', 10))

        location_y = tk.Label(database_frame, text='Location: Y', width=15, height=2)
        location_y.grid(row=4, column=2, pady=10, padx=10)
        location_y.config(font=('Helvetica Bold', 10))

        # FORMS

        serial_id = tk.Entry(database_frame, width=30)
        serial_id.grid(row=0, column=1)

        first_name = tk.Entry(database_frame, width=30)
        first_name.grid(row=1, column=1)

        surname = tk.Entry(database_frame, width=30)
        surname.grid(row=2, column=1)

        remarks = tk.Entry(database_frame, width=30)
        remarks.grid(row=3, column=1)
        

        x_coordinate = tk.Entry(database_frame, width=30)
        x_coordinate.grid(row=4, column=1)

        y_coordinate = tk.Entry(database_frame, width=30)
        y_coordinate.grid(row=4, column=3)

        # CRUD BUTTONS
        submit_button = tk.Button(database_frame, text='ADD', width=15, height=2)
        submit_button.grid(row=0, column=2, padx=25, pady=10, ipadx=25)
        submit_button['command'] = self.submit
        
        update_button = tk.Button(database_frame, text='UPDATE', width=15, height=2)
        update_button.grid(row=1, column=2, padx=25, pady=10, ipadx=25)
        update_button['command'] = self.update

        delete_button = tk.Button(database_frame, text='DELETE', width=15, height=2)
        delete_button.grid(row=2, column=2, padx=25, pady=10, ipadx=25)
        delete_button['command'] = self.delete

        self.graph_button = tk.Button(database_frame, text='SHOW GRAPH', width=15, height=2)
        self.graph_button.grid(row=0, column=3, padx=25, pady=10, ipadx=25)
        self.graph_button['command'] = self.graphPoints

        clear_button = tk.Button(database_frame, text='CLEAR FORMS', width=15, height=2)
        clear_button.grid(row=1, column=3, padx=25, pady=10, ipadx=25)
        clear_button['command'] = self.clear_entries

        # matplot_button = tk.Button(database_frame, text='GRAPH POINTS', width=15, height=2)
        # matplot_button.grid(row=2, column=3, padx=25, pady=10, ipadx=25)
        # matplot_button['command'] = self.show_graph

        
        self.matplot_button = tk.Button(database_frame, text='GRAPH POINTS', width=15, height=2)
        self.matplot_button.grid(row=2, column=3, padx=25, pady=10, ipadx=25)
        self.matplot_button['command'] = self.show_graph
        # self.show()

        # show_button = tk.Button(database_frame, text='SHOW TABLE')
        # show_button.grid(row=1, column=3, padx=25, pady=10, ipadx=25)
        # show_button['command'] = self.show
        # TABLE
        
        
        self.create_tree()
        self.tree.bind('<<TreeviewSelect>>', self.update_entry)

        return serial_id, first_name, surname, remarks, x_coordinate, y_coordinate

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
            
            x_coordinate = self.x_coordinate.get()
            y_coordinate = self.y_coordinate.get()

            location = f'{x_coordinate}, {y_coordinate}'
            
            if not serial_id or not surname or not first_name or not remarks or not x_coordinate or not y_coordinate:
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
                self.x_coordinate.delete(0, tk.END)
                self.y_coordinate.delete(0, tk.END)

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
        x_coordinate = self.x_coordinate.get()
        y_coordinate = self.y_coordinate.get()

        location = f'{x_coordinate}, {y_coordinate}'

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

                        db.commit()

                        messagebox.showinfo('Update Successful', f'Item with the ID: {id} was updated.')
                        
                        self.serial_id.delete(0, tk.END)
                        self.last_name.delete(0, tk.END)
                        self.first_name.delete(0, tk.END)
                        self.remarks.delete(0, tk.END)
                        self.x_coordinate.delete(0, tk.END)
                        self.y_coordinate.delete(0, tk.END)

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
        
        # self.graph_button.config(state=tk.DISABLED)
        # SETUP
        try: 
            
            
            turtle.title('PUP MAIN MAP')

            # img = PhotoImage(file='pupicon.png')
            # turtle._Screen._root.iconphoto(True, img)

            wn = turtle.Screen()
            t = turtle.Turtle()
            t.speed(0)

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
            
        
        except turtle.Terminator:
            self.graphPoints()

        

        
        
    def show_graph(self):

        self.matplot_button.config(state=tk.DISABLED)


        
        img = mpimg.imread('C:\Downloads\codeEnv-main (3)\codeEnv-main\pup_map.png')

        locations = self.get_column_as_a_list('LOC')

        x_coordinates = []
        y_coordinates = []

        quadrant_1 = []
        quadrant_2 = []
        quadrant_3 = []
        quadrant_4 = []
        
        for i in locations:
                
            coordinate = i.split(', ')
            x = float(coordinate[0])
            y = float(coordinate[1])

            # x = random.randint(-350, 350)
            # y = random.randint(-350, 350)

            x_coordinates.append(x)
            y_coordinates.append(y)

            if x >= 0 and y >= 0:
                print('First Quadrant')
                quadrant_1.append((x, y))
            elif x <= 0 and y >= 0:
                print('Second Quadrant')
                quadrant_2.append((x, y))
            elif x <= 0 and y <= 0:
                print('Third Quadrant')
                quadrant_3.append((x, y))
            elif x >= 0 and y <= 0:
                print('Fourth Quadrant')
                quadrant_4.append((x, y))
            else:
                pass

        print(x_coordinates)
        print(y_coordinates)

        fig, ax = plt.subplots()





        ax.imshow(img, extent=[-1024, 1024, -672, 672])
        ax.scatter(x_coordinates, y_coordinates, c='black')
        ax.set_xlim(-350, 350)
        ax.set_ylim(-350, 350)
        ax.axhline(y=0, color='gray', linestyle='--')
        ax.axvline(x=0, color='gray', linestyle='--')

        # for i, label in enumerate(locations):
            
        #     ax.annotate(label, (x_coordinates[i], y_coordinates[i]))

        plt.show()

        self.matplot_button.config(state=tk.NORMAL)
        
    def clear_all(self):

        for item in self.tree.get_children():
            self.tree.delete(item)
    
    def clear_entries(self):

        self.serial_id.delete(0, tk.END)
        self.first_name.delete(0, tk.END)
        self.last_name.delete(0, tk.END)
        self.x_coordinate.delete(0, tk.END)
        self.y_coordinate.delete(0, tk.END)
        self.remarks.delete(0, tk.END)

    def update_entry(self, event):
        selected_item = self.tree.focus()
        print(selected_item)

        serial_id = self.tree.item(selected_item)['values'][1]
        first_name = self.tree.item(selected_item)['values'][2]
        surname = self.tree.item(selected_item)['values'][3]
        location = self.tree.item(selected_item)['values'][5]
        remarks = self.tree.item(selected_item)['values'][6]

        coordinates = location.split(', ')
        print(coordinates)
        x_coordinate = coordinates[0]
        y_coordinate = coordinates[1]


        
        self.serial_id.delete(0, tk.END)
        self.first_name.delete(0, tk.END)
        self.last_name.delete(0, tk.END)
        self.x_coordinate.delete(0, tk.END)
        self.y_coordinate.delete(0, tk.END)
        self.remarks.delete(0, tk.END)
        
        self.serial_id.insert(0, serial_id)
        self.first_name.insert(0, first_name)
        self.last_name.insert(0, surname)
        self.x_coordinate.insert(0, x_coordinate)
        self.y_coordinate.insert(0, y_coordinate)
        self.remarks.insert(0, remarks)

  



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


