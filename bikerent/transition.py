from tkinter import*
from PIL import Image,ImageTk
from tkinter import messagebox
from database import *
# from usergets import kepthe_usermoney

import pickle
file = 'pa.pkl'
read_userdata = open(file, 'rb')
readusermoney = open('money.pkl', 'rb')
usermoney = pickle.load(readusermoney)
userpas = pickle.load(read_userdata)
# Lets depickel the foreginkey

file = 'username.pkl'
read_userdata = open(file, 'rb')
my_userid = pickle.load(read_userdata)
print(my_userid,'THIS IS MY USER ID')
read_userdata.close()
readusermoney.close()
read_userdata.close()

    # pass
root=Tk()
root.geometry('900x500')
root.title("BikreFreez Banking")

root.configure(bg="#ADD8E6")
root.resizable(False,False)



root.configure(bg="#ADD8E6")
root.resizable(False,False)
# img = PhotoImage(file="l.png")
# label = Label( image=img)
# label.place(x=0, y=0)

frame=Frame(root,width=350,height=350,bg='#fff')
frame.place(x=500,y=90)
heading=Label(frame,text="Banking",fg='red',bg='white',font=('Gabriola','25','bold'),bd=0)
heading.place(x=130,y=0)


passw = ''
fBikeid = 1
fownerid = 1
fPrice = 1
fPassword = 1
fmessage = 1

def openlogin():
    root.destroy()
    import login



def send_money():
    print('Ok i am running')
    bike_id = Bikeid.get()
    price_ = Price.get()
    owner_id= ownerid.get()
    mess_age = message.get()
    pss_word =Password.get()
    if(not price_.isdigit()):
        messagebox.showerror('error', 'Pleased provide valid informations.')
        return
    send_price = int(price_)
    current_money = int(usermoney)


# This is because a user can't send the money to himself
    if( owner_id == my_userid):
        return
# Check the userinput  is valid integer or not
    if(price_.isdigit() and pss_word == userpas):
        print('Print both Condition matched')




# Check the bike available or not
        print('OK I AM STILL RUNNING')
        query = "SELECT * FROM uploadedbikes WHERE userid = %s AND id = %s"
        print(1)
        try:
           print(owner_id,'THIS IS VALID OR NOT')
           mycuror.execute(query, (owner_id, bike_id))
           print(2)
           ownerbike = mycuror.fetchall()
           print(ownerbike)
           print(ownerbike,'This is the owner bike')
           if(not int(ownerbike[0][9])== send_price ):

             messagebox.showerror('error','Pleased look at the money!')
             return
           else:
               print('Welldone')
               

           
           if(ownerbike[0][8] == 'NO'):
               messagebox.showerror('alert','Bike is not available for now')
               return
        except Exception as e:
              print(e, 'THisis the error')

        # Check the user have sufficient balance or not
        if(send_price<= current_money):
         mycuror.execute("SHOW TABLES LIKE 'banking'")  
         exist=mycuror.fetchone()
         print(exist, 'THISTHISHTISHTISSHTI')
         if(exist):
             print('yes tabel is exist')
             pass
         else:
          print('Tabel is not exist')
          query = "SELECT money FROM usersmoney WHERE userid = %s"
          print(owner_id, 'THIS IS ALSO CHEKC')
          mycuror.execute(query, (owner_id,))
          ownermoney = mycuror.fetchone()
          print(ownermoney,'THIS IS OWNER MONEY')
          if(not ownermoney):
              print('User is not exist')
              messagebox.showerror('error', 'Pleased input valid information.')
              return
          print(my_userid,'THIS IS WHAT CHECK THE FIRST')
          mycuror.execute(query,(my_userid[0],))
          sendermoney = mycuror.fetchone()
          print(sendermoney,'THIS IS THE SENDER MONEY') 
          omoney = int(ownermoney[0])
          smoney = int(sendermoney[0])
          print(omoney, 'HELLO WORLD')
        #   query = "SELECT * FROM uploadedbikes WHERE userid = %s AND id = %s"
        #   mycuror.execute(query, (owner_id,bike_id))
        #   ownerbike = mycuror.fetchall()
        #   print(ownerbike,'This is the owner bike')
          
        #   Update usermoney or let's  manage the consistencey
          update_query = "UPDATE usersmoney SET money = %s WHERE userid = %s"
          new_money_fo_the_owner  = omoney+send_price
          print(new_money_fo_the_owner,owner_id, 'CHECK111')
          mycuror.execute(update_query, (new_money_fo_the_owner, owner_id))
          mydb.commit()
        #   update sender money
          update_sender_money = "UPDATE usersmoney SET money = %s WHERE userid = %s"
          new_money_fo_the_sender  = smoney-send_price
          print(new_money_fo_the_sender, my_userid)

          mycuror.execute(update_sender_money, (new_money_fo_the_sender, my_userid[0]))
          mydb.commit()

        #   Let'supdate the bike available if the user book the bike
         query_foravai = "UPDATE uploadedbikes SET available = %s WHERE userid= %s"
         avai ='NO'
         mycuror.execute(query_foravai,(avai, owner_id))
         mydb.commit()
         messagebox.showerror('sucess', 'sendSucessfull')
         root.destroy()








#          tb = f"""
#       CREATE TABLE {table_name} (
#         id INT AUTO_INCREMENT PRIMARY KEY,
#         userunique_id_for_allthethings VARCHAR(255),
#         bike_name VARCHAR(255),
#         bike_location VARCHAR(255),
#         bike_condition VARCHAR(255),
#         bike_number VARCHAR(255),
#         bike_image VARCHAR(255),
#         userid VARCHAR(255),
#         available VARCHAR(255),
#         bikeprice VARCHAR(255),
#         howmanydays VARCHAR(200),
#         transferdate DATE NOT NULL DEFAULT (CURRENT_DATE())
#     )
# """
        else:
            print('No the money amoutnt in not big')
            print(type(usermoney), type(price_))
    else:
        # print('No')
        messagebox.showerror('error','PLEASED GIVE VALID INFORMATINS!')
        return
# Lets depickel the foreginkey



def enter(event):
    global fBikeid
    if (fBikeid == 1):
        if(Bikeid.get() == "BikeId"):
            Bikeid.delete(0,END)
            return
        fBikeid = 2

def leave(event):
    if Bikeid.get()=='':
        Bikeid.insert(0,"BikeId")
Bikeid=Entry(frame,width=20,bd=5, font= ("Arial",10,"bold"))
Bikeid.place(x=15,y=80)
Bikeid.insert(0,"BikeId")
Bikeid.bind('<FocusIn>',enter)
Bikeid.bind('<FocusOut>',leave)


def enter(event):
    global fPrice
    if (fPrice == 1):
        if(Price.get() == "Price"):
            Price.delete(0,END)
            return
        fPrice = 2
def leave(event):
    if Price.get()=='':
        Price.insert(0,"Price")
Price=Entry(frame,width=30,bd=5, font= ("Arial",10,"bold"))
Price.place(x=60,y=125)
Price.insert(1,"Price")
Price.bind('<FocusIn>',enter)
# Price.bind('<key>',enter)
Price.bind('<FocusOut>',leave)

def enter(event):
    global fPassword
    if (fPassword == 1):
        if(Password.get() == "Password"):
            Password.delete(0,END)
            return
        fPassword = 2

def leave(event):
    if Password.get()=='':
        Password.insert(0,"Password")    
Password=Entry(frame,width=30,bd=5, font= ("Arial",10,"bold"))
Password.place(x=60,y=170)
Password.insert(2,"Password")
Password.bind("<FocusIn>",enter)
Password.bind('<FocusOut>',leave)

def enter(event):
    global fownerid
    if (fownerid == 1):
        if(ownerid.get() == "Ownerid"):
            ownerid.delete(0,END)
            return
        fownerid = 2

def leave(event):
    if ownerid.get()=='':
        ownerid.insert(0,"Ownerid")
ownerid=Entry(frame,width=20,bd=5, font= ("Arial",10,"bold"))
ownerid.place(x=190,y=80)
ownerid.insert(0,"Ownerid")
ownerid.bind('<FocusIn>',enter)
ownerid.bind('<FocusOut>',leave)



def enter(event):
    # p = Password.get()
    # print(p)
    global fmessage
    if (fmessage == 1):
        if(message.get() == "Message"):
            message.delete(0,END)
            return
        fmessage = 2

def leave(event):
    if message.get()=='':
        message.insert(0,"Message")
message=Entry(frame,width=30,bd=5, font= ("Arial",10,"bold"))
message.place(x=60,y=210)
message.insert(3,"Message")
message.bind("<FocusIn>",enter)
message.bind('<FocusOut>',leave) 


signup_btn=Button(frame,text="Send",fg='white', bg='blue',width=15,font=('Roboto','12','bold'),command=send_money)
signup_btn.place(x=90,y=260)
# label=Label(frame,text="I have an account",fg='black',bg='white',font=('Roboto',9))
# label.place(x=85,y=300)

# signin=Button(frame,width=6,text='Sign in',fg='blue',bg='white', bd=0, command= openlogin)
# signin.place(x=190,y=300)


# For image of money
# Load the image
img_money = Image.open('pay.jpg')
hee =203
wii = 304
size =img_money.resize((wii,hee),Image.LANCZOS)
img =ImageTk.PhotoImage(size)
label_image_of_the_money = Label(image=img, bg='skyblue')
label_image_of_the_money.place(x=83,y=145)



root.mainloop()