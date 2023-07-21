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
# Tkinter images
from PIL import Image, ImageTk





# Let's kepthe user details in the global variables
keep_username = ''
keep_fullname = ''
keep_password = ''
keep_email = ''
# uinqueid = 0






















window= Tk()
window.title("Login")
window.configure(bg="#0B1340")

window.geometry("1000x500")
font1=font.Font(family='Georgia')
font2=font.Font(family="Georgia", size=8)
window.resizable(0,0)

frame=Frame(window,width=400,height=350,bg='#fff', borderwidth=12)

frame.place(x=50,y=70)


# Load the image
image = Image.open("m.png")

# Resize the image
new_width = 400
new_height = 310
resized_image = image.resize((new_width, new_height), Image.ANTIALIAS)

tk_image = ImageTk.PhotoImage(resized_image)

image_label = Label(window, image=tk_image, bg='#0B1340')
image_label.place(x=462, y=75)


femail=1
fpassword=1
def opensignup():
    window.destroy()  #refers to the tkinter window object that you want to close. 
    import singup

def opendash():
    window.destroy()
    import dash

    

invalid_mes=Label(frame,text="Let's Login.",fg='red',bg='white',font=('Gabriola','14','bold'))
invalid_mes.place(x=43,y=289)
# Storing the user valid information to the database
def check_data():
    global invalid_mes




# # Storing the user valid information to the database
#   def check_data():
#     global invalid_mes, uinqueid

# #     mydb = mysql.connector.connect(
# #     host = 'localhost',
# #     user = 'root',
# #     password= 'Aayush888999',
# #     database = 'BIKE'
# # )
    


    # mycuror = mydb.cursor()
    from database import mycuror
    mycuror.execute("SELECT * FROM users")
    datas = mycuror.fetchall()
    
    print(datas)
    email =  Email.get()
    password = Password.get()
    print(email, password)
    if(not email or email=='Email'):
            # invalid_mes=Label(frame,text="Pleased provide email!",fg='red',bg='white',font=('Gabriola','14','bold'))
            # invalid_mes.place(x=48,y=289)
            invalid_mes.config(text='Pleased provide email!')
            return
    

    if(not password or password=='Password'):
            # invalid_mes=Label(frame,text="Pleased provide password!",fg='red',bg='white',font=('Gabriola','14','bold'))
            # invalid_mes.place(x=48,y=289)
            invalid_mes.config(text="Pleased provide password!")
            return

    for i in datas:
        print('I am starting')
        print(i[2])
        if(i[2]==email and i[4] == password):    
                uinqueid = i[0] 
                import pickle
                file = 'useruniqu.pkl'
                fileobj = open(file, 'wb')
                pickle.dump(uinqueid, fileobj)
                fileobj.close()
                # from keepthedata import uinqueid
            
                print(uinqueid, 'WHAT IS YOU FATHER PUT IS YOU NAME')
                opendash()

                # keep_username = i[]
        else:
            invalid_mes.config(text='Pleased input the valid informations!')
            # return



    


      


# Run if user enter for input
def enter(event):
    global femail
    if (femail == 1):
        if(Email.get() == "Email"):
            Email.delete(0,END)
            return
        femail = 1

# Runs when user leaves from the input opposite of the enter function
def leave(event):
  if Email.get()=='':
        Email.insert(0,"Email")


Email=Entry(frame,width=25,bd=5, font= ("Arial",15,"bold"))#font=('Comic Sans MS',15,'bold'),
Email.place(x=50,y=69)
Email.insert(1,"Email")
Email.bind('<FocusIn>',enter) #that it becomes the active element that can receive user input.
Email.bind('<FocusOut>',leave) #meaning that it is no longer the active element that can receive user input.


def enter(evnet):
    global fpassword
    if (fpassword == 1):
        if (Password.get() == "Password"):
            Password.delete(0,END)
            return
        fpassword = 1
def leave(event):
    if Password.get()=="":
        Password.insert(0,"Password")
Password=Entry(frame,width=23,bd=5,font=('Comic Sans MS',15,'bold'), show='*')
Password.place(x=50,y=129)
Password.insert(1,'Password')

# Run if user enter for input
Password.bind("<FocusIn>",enter)    


# Runs when user leave from the input opposite of the enter function
Password.bind('<FocusOut>',leave) 
heading=Label(frame,text="Login",fg='red',bg='white',font=('Gabriola','25','bold'))
heading.place(x=155,y=1)

#login button
bt1=Button(frame,text="LOGIN", font=('Comic Sans MS',10,'bold'),fg='white',bg="#338bd7",width=15,height=2,cursor='hand2', command= check_data)
bt1.place(x=120,y=185)
btn2=Button(frame,text="Signup",bd=0,fg="blue", font=('Comic Sans MS',10,'bold'),bg="white", command= opensignup).place(x=174,y=252)
signup_label= Label(window, text="Create new account?",font= font2,bg='white' )
signup_label.place(x=99,y=340)
window.mainloop()






    
