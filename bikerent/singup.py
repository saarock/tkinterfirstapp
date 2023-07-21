#login
from tkinter import*
import tkinter.font as font 
#This library allows you to work with fonts in your tkinter-based GUI application. 
#It provides a way to create, customize, and use different fonts for text elements such as labels, buttons, and text boxes in your application's user interface. 
from PIL import ImageTk, Image
# it allows you to work with images in the Python Imaging Library (PIL) using the tkinter library.
from re import A
#allows you to import the 'A' constant from the 're' module in Python.
import sqlite3
#allows you to use the sqlite3 module, which provides functionality for working with SQLite databases.
from tkinter import messagebox
#which provides functionality for working with SQLite databases.
from functools import partial
import mysql.connector
from PIL import Image, ImageTk
from database import *


# from validate_email import validate_email 
# import valid

# Let's used the mysql
# import
window= Tk()
window.title("Singup")
window.configure(bg="#FFFF7F")
window.geometry("900x600")
font1=font.Font(family='Georgia')
font2=font.Font(family="Georgia", size=8)
window.resizable(0,0)

frame=Frame(window,width=400,height=550,bg='#fff', borderwidth=3)
frame.place(x=50,y=20)




# Load the image
image = Image.open("l.png")

# Resize the image
new_width = 400
new_height = 310
resized_image = image.resize((new_width, new_height), Image.ANTIALIAS)

tk_image = ImageTk.PhotoImage(resized_image)

image_label = Label(window, image=tk_image,bg="#FFFF7F")
image_label.place(x=462, y=75)


global variables
fname=1
uname = 1
password = 1
repassword = 1
femail = 1


def opensignup():
    window.destroy()  #refers to the tkinter window object that you want to close. 
    import login

# OPen the dashn  after the login complete
def opendash():
    window.destroy()
    import dash
    

# Check there is table or not if not then create the table
def create_tabel():
    mycuror.execute("SHOW TABLES LIKE 'users'")
    table_exist = mycuror.fetchone()
    print(table_exist, 'This is herer message of the tabel exisst ot not')
    # mycuror.execute(create_table_query)
    print(mycuror, 'HAHA')
    if(not table_exist):
        tb = f"""
      CREATE TABLE users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        fullname VARCHAR(255),
        email VARCHAR(255),
        password VARCAHR(255),
        repassword VARCHAR(255),
        username VARCHAR(255)
    )
"""   
        mycuror.execute(tb)
        mydb.commit()
        mycuror.close()
        mydb.close()





# Connect to the database
def store_data():
    mydb = mysql.connector.connect(
     host = 'localhost',
     user = 'root',
     password= 'Aayush888999',
     database = 'BIKE'
)

# Check the table is already exist or not
    mycuror = mydb.cursor()
    print(mycuror, 'HAHA')
    query = "INSERT INTO users (fullname, email, password, repassword, username) VALUES (%s, %s, %s, %s, %s)"
    # Get all the data from the Entry that we want to store in the data base
    fullname = Fullname.get()
    email = Email.get()
    password = Password.get()
    repassword = Repassword.get()
    username = Username.get()
    print(fullname, email, password, repassword, username)
    # Check if email already exists in the database
    existing_email_query = "SELECT COUNT(*) FROM users WHERE email = %s OR  username = %s"
    mycuror.execute(existing_email_query, (email,username))
    # get all the email and the username that already exist in the database
    email_count = mycuror.fetchone()[0]

    # Check the email is None or what in the froentend
    if not email or email== 'Email':
        print('Please provide the valid informations!')
        email_invalid= Label(window, text="Please provide the email!",font=('Gabriola','14','bold'), bg='white', fg='red')
        email_invalid.place(x=139,y=499)
        return
    

    # Check the username in the froentend
    if not username or username == 'uinque username':
        username_invalid= Label(window, text="Please provide the username!",font=('Gabriola','14','bold'), bg='white', fg='red')
        username_invalid.place(x=139,y=499)
        return



        # Check the password and the reapassword are None or?
    if not password or password == 'Password' or repassword == 'Repassword':
          password_invalid= Label(window, text="Please provide the password or repassowrd!",font=('Gabriola','14','bold'), bg='white', fg='red')
          password_invalid.place(x=139,y=499)
          return




    if(email_count==0 or email_count<0):
      if(repassword==password):
      
        print('yes password match')
        values = (fullname, email, password, repassword, username)
        try:
            # Executed the provided value with the given datas
            mycuror.execute(query, values)

            # Commit the changes  to the databse
            mydb.commit()
            opensignup()

        except mysql.connector.Error as error:
            messagebox.showerror("Pleased Singin with valid datas")
            print(error)
   
            
      else:
        print('password dnont mathch')
    else:
       email_invalid= Label(window, text="Email or username already exist!",font=('Gabriola','14','bold'), bg='white', fg='red')
       email_invalid.place(x=139,y=499)
       print('EMAIL ALREASDY EXIST')

#     email = email
    # Close the cursor and the database connection
    mycuror.close()
    mydb.close()





def enter(event):
    global fname
    if (fname == 1):
        if(Fullname.get() == "Fullname"):
            Fullname.delete(0,END)
            return
        fname = 2
def leave(event):
    if Fullname.get()=='':
        Fullname.insert(0,"Fullname")
    # lname = 1
Fullname=Entry(frame,width=25,bd=5,font= ("Arial",15,"bold"))
Fullname.place(x=50,y=129)
Fullname.insert(1,'Fullname')
Fullname.bind("<FocusIn>",enter)      
Fullname.bind('<FocusOut>',leave) 
heading=Label(frame,text="Singup",fg='red',bg='white',font=('Gabriola','25','bold'))
heading.place(x=155,y=9)


def enter(event):
    global femail
    if (femail == 1):
        if(Email.get() == "Email"):
            Email.delete(0,END)
            return
        femail = 2
def leave(event):
    if Email.get()=='':
        Email.insert(0,"Email")
Email=Entry(frame,width=25,bd=5,font= ("Arial",15,"bold"))
Email.place(x=50,y=75)
Email.insert(1,"Email")
Email.bind('<FocusIn>',enter) #that it becomes the active element that can receive user input.
Email.bind('<FocusOut>',leave) #meaning that it is no longer the active element that can receive user input.




# For use name
def enter(event):
    global uname
    if uname==1:
        if(Username.get() == 'uinque username'):
            Username.delete(0, END)
            return
        uname = 2



def leave(event):
    global uname    
    if Username.get() == '':
        Username.insert(0, 'uinque username' )
        # uname = 1
# For the username entry
Username=Entry(frame,width=25,bd=5, font= ("Arial",15,"bold"))#font=('Comic Sans MS',15,'bold'),
Username.place(x=50,y=187)
Username.insert(1,'uinque username')
Username.bind("<FocusIn>",enter)      
Username.bind('<FocusOut>',leave) 
heading = Label(frame,text="Singup",fg='red',bg='white',font=('Gabriola','25','bold'))
heading.place(x=155,y=9)



# For password entry
def enter(event):
    global password
    if password==1:
        if(Password.get() == 'Password'):
            Password.delete(0, END)
            return
        password = 2



def leave(event):
    global password
    if Password.get() == '':
        Password.insert(0, 'Password')
        # uname = 1
# For the username entry
Password=Entry(frame,width=23,bd=5,font=('Comic Sans MS',15,'bold'), show='*')
Password.place(x=50,y=240)
Password.insert(1,'Password')
Password.bind("<FocusIn>",enter)      
Password.bind('<FocusOut>',leave) 
heading = Label(frame,text="Singup",fg='red',bg='white',font=('Gabriola','25','bold'))
heading.place(x=155,y=9)








# For repassword entry

def enter(event):
    global repassword
    if repassword==1:
        if(Repassword.get() == 'Repassword'):
            Repassword.delete(0, END)
            return
        repassword = 2



def leave(event):
    global password
    if Repassword.get() == '':
        Repassword.insert(0, 'Repassword')
        # uname = 1
# For the username entry
Repassword=Entry(frame,width=23,bd=5,font=('Comic Sans MS',15,'bold'), show='*')
Repassword.place(x=50,y=295)
Repassword.insert(1,'Repassword')
Repassword.bind("<FocusIn>",enter)      
Repassword.bind('<FocusOut>',leave) 
heading = Label(frame,text="Singup",fg='red',bg='white',font=('Gabriola','25','bold'))
heading.place(x=155,y=9)









#login button
bt1=Button(frame,text="SINGUP", font=('Comic Sans MS',10,'bold'),fg='white',bg="#338bd7",width=15,height=2,cursor='hand2', command= store_data)
bt1.place(x=117,y=370)
btn2=Button(frame,text="Signin",font=('Comic Sans MS',10,'bold'),bd=0,fg="blue",bg="white", command= opensignup).place(x=190,y=431)
signup_label= Label(window, text="Already have Account?",font= font2,bg='white' )
signup_label.place(x=99,y=459)
window.mainloop()






    
