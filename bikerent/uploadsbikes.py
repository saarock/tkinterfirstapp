from ast import Pass
import email
from tkinter import*
# from tkinter import messagebox
# from traceback import print_tb
# from turtle import position
from PIL import Image,ImageTk
# from tkinter import Text
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter import messagebox
# from tkinter import messagebox
from database import *
root=Tk()
root.geometry('900x500')
root.title("UPLOAD THE BIKES")
# conn=sqlite3.connect("client.db")
# c=conn.cursor()
# c.execute("""CREATE TABLE users(
#     First_Name text,
#     Last_Name text,
#     Email text PRIMARY KEY,
#     Password text,
#     BikeCondition text,
#     status boolean)""")
# print("Table created successfully")

# #Doping table if already exists
# c.execute("DROP TABLE bookcars")
# print("Table dropped... ")

# #Commit your changes in the database
# conn.commit()

root.configure(bg="#ADD8E6")
root.resizable(False,False)



root.configure(bg="#ADD8E6")
root.resizable(False,False)
# img = PhotoImage(file="l.png")
# label = Label( image=img)
# label.place(x=0, y=0)

frame=Frame(root,width=350,height=350,bg='#fff')
frame.place(x=500,y=90)
heading=Label(frame,text="UPLOAD YOU BIKES.",fg='red',bg='white',font=('Gabriola','25','bold'),bd=0)
heading.place(x=54,y=0)






passw = ''
fBikename = 1
fLastName = 1
fPhonenumber = 1
fBikePikupLocation = 1
fBikeCondition = 1
fbIKEprice = 1






# Lets depickel the foreginkey
import pickle
file = 'useruniqu.pkl'
read_userdata = open(file, 'rb')
userunique_id_for_allthethings = pickle.load(read_userdata)
print(userunique_id_for_allthethings, 'WASDGNALSDJGNSAJKDGAKJDGBKSGBJ,D G')
read_userdata.close()



# LET;S DEPICKEL THE user unique id
file = 'username.pkl'
fileobj = open(file, 'rb')
useruniqueid = pickle.load(fileobj)
fileobj.close()
print(useruniqueid,'THIS IS THE USER UNIQUE ID')


# Global variabletokeepthe bike imagenmae
keep_nameof_bike = ''



# Uploading the bike image
def uploadthebikeimage():
    global Showthebikeimagelabel, keep_nameof_bike
    file = filedialog.askopenfile(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    if(file):
        import os
        try:
          file_name = os.path.basename(file.name)
          print(file_name)
          image_dir = f'bikes/{file_name}'
          keep_nameof_bike = file_name
          print(file_name ,'Thasndkjnasdlk;gnasldkgnmask/ldgnksaldfgnsdlfngskdlfn')
          print(file_name, "This is the real file")
          
          print(1)
          global image
          image = Image.open(file.name)
          height = 193
          width = 350
          bike_image = image.resize((width, height), Image.ANTIALIAS)
          photo = ImageTk.PhotoImage(bike_image)
          Showthebikeimagelabel.config(image=photo)
          Showthebikeimagelabel.image = photo
          print('File is closed')
          bike_image.save(image_dir)
        except IOError as e:
            print(e)
        
        








# Post to the database;
def post():


    print(keep_nameof_bike, 'This is the gllobal')
    # if()
    bike_name = Bikename.get()
    bike_location = BikePikupLocation.get()
    bike_condition = BikeCondition.get()
    bike_number = BikeNumbers.get()
    bike_price = Bikeprice.get()
    print(bike_name, bike_condition, bike_location, bike_number,useruniqueid)
    if(bike_number=='Bike number ' or keep_nameof_bike == '' or  bike_number == ''  or bike_name == 'Bike name' or bike_name=='' or bike_condition == 'Bike Condition'
        or bike_condition=='' or bike_location == 'BikePikupLocation' or bike_location=='' or bike_price == ' ' or bike_price == 'Bike price' or useruniqueid is None or useruniqueid == ''):
        return


    # from database import 
    try:
     howmanydays = 12
     mycuror.execute("SHOW TABLES LIKE 'uploadedbikes'")
     table_exist = mycuror.fetchone()
     print(table_exist, 'This is herer message of the tabel exisst ot not')
     if(not table_exist):
    # get all the email and the username that already exist in the database
         print('table does not exist')
         table_name = "uploadedbikes"
         uploaded_date = "uploadeddate"
         tb = f"""
      CREATE TABLE {table_name} (
        id INT AUTO_INCREMENT PRIMARY KEY,
        userunique_id_for_allthethings VARCHAR(255),
        bike_name VARCHAR(255),
        bike_location VARCHAR(255),
        bike_condition VARCHAR(255),
        bike_number VARCHAR(255),
        bike_image VARCHAR(255),
        userid VARCHAR(255),
        available VARCHAR(255),
        bikeprice VARCHAR(255),
        howmanydays VARCHAR(200),
        {uploaded_date} DATE NOT NULL DEFAULT (CURRENT_DATE())
    )
"""
# Commit the changes
         mycuror.execute(tb)
         mydb.commit()
        #  print()

         datas = '''
    INSERT INTO uploadedbikes (userunique_id_for_allthethings, bike_name, bike_location, bike_condition, bike_number, bike_image, userid, available, bikeprice)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
     '''
        #  print(bike_image)
         print('Does it is')
         ava = 'YES'
         howmanydays = 12
         values = (userunique_id_for_allthethings, bike_name, bike_location, bike_condition, bike_number, keep_nameof_bike, useruniqueid, ava, bike_price, howmanydays)
         print(4,datas, values)
         mycuror.execute(datas, values)
         print(5)
         print('datasaved')
# Commit the changes
         mydb.commit()
 
# Close the cursor and the connection
         mycuror.close()
         mydb.close()
         image.save(f'bikes/{keep_nameof_bike}')
         print('saved')
         print('table is created')
         root.destroy()
     else:
        try:
         sql ='SELECT * FROM uploadedbikes WHERE userid= %s AND userunique_id_for_allthethings = %s '
         mycuror.execute(sql, (useruniqueid[0], userunique_id_for_allthethings))
         dat = mycuror.fetchall()
         print(dat, 'IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII')
         if(len(dat)>3):
             messagebox.showerror('alert', 'Out of Limit youalready posted 4 bikes!')
             root.destroy()
             return;
        except Exception as e:
            print(e)

        print('WHAT IS YOU NAME MYNAME IS AAYUSH BASNET')
        # values   = (userunique_id_for_allthethings, bike_name, bike_location, bike_condition, bike_number, keep_nameof_bike)
        # mycuror.execute(datas, values)
        # print('datasaved')
        # print(1)
        # print('Already exist')
        # print(2)
        datas = '''
        INSERT INTO uploadedbikes (userunique_id_for_allthethings, bike_name, bike_location, bike_condition, bike_number, bike_image, userid, available, bikeprice,howmanydays)
        VALUES (%s, %s, %s, %s, %s, %s,%s,%s, %s,%s)
    '''
        print(bike_image)
        ava = 'YES'
   
        values   = (userunique_id_for_allthethings, bike_name, bike_location, bike_condition, bike_number, keep_nameof_bike, useruniqueid[0], ava, bike_price,howmanydays)
        print(4, userunique_id_for_allthethings, bike_name, bike_location, bike_condition, bike_number, keep_nameof_bike, useruniqueid, ava, bike_price,howmanydays)
        mycuror.execute(datas, values)
        print(5)
        print('datasaved')
        # Commit the changes
        mydb.commit()


    # Close the cursor and the connection
        mycuror.close()
        mydb.close()
        image.save(f'bikes/{keep_nameof_bike}')
        print('saved')
        print('tables is maded')
        root.destroy()
    except Exception as e:
        print(e, 'THIS IS YOU ERRRO')
    finally:
        # pass
       mycuror.close()
       mydb.close()

    #    Tk.destroy()
    



    

def enter(event):
    global fBikename
    if (fBikename == 1):
        if(Bikename.get() == "Bike name"):
            Bikename.delete(0,END)
            return
        fBikename = 2

def leave(event):
    if Bikename.get()=='':
        Bikename.insert(0,"Bike name")
Bikename=Entry(frame,width=20,bd=5, font= ("Arial",10,"bold"))
Bikename.place(x=15,y=60)
Bikename.insert(0,"Bike name")
Bikename.bind('<FocusIn>',enter)
Bikename.bind('<FocusOut>',leave)


def enter(event):
    global fPhonenumber
    if (fPhonenumber == 1):
        if(Phonenumber.get() == "Phonenumber"):
            Phonenumber.delete(0,END)
            return
def leave(event):
    if Phonenumber.get()=='':
        Phonenumber.insert(0,"Phonenumber")
Phonenumber=Entry(frame,width=30,bd=5, font= ("Arial",10,"bold"))
Phonenumber.place(x=60,y=105)
Phonenumber.insert(1,"Phonenumber")
Phonenumber.bind('<FocusIn>',enter)
# Phonenumber.bind('<key>',enter)
Phonenumber.bind('<FocusOut>',leave)

def enter(event):
    global fBikePikupLocation
    if (fBikePikupLocation == 1):
        if(BikePikupLocation.get() == "BikePikupLocation"):
            BikePikupLocation.delete(0,END)
            return

def leave(event):
    if BikePikupLocation.get()=='':
        BikePikupLocation.insert(0,"BikePikupLocation")    
BikePikupLocation=Entry(frame,width=30,bd=5, font= ("Arial",10,"bold"))
BikePikupLocation.place(x=60,y=150)
BikePikupLocation.insert(2,"BikePikupLocation")
BikePikupLocation.bind("<FocusIn>",enter)
BikePikupLocation.bind('<FocusOut>',leave)

def enter(event):
    global fLastName
    if (fLastName == 1):
        if(BikeNumbers.get() == "Bike number"):
            BikeNumbers.delete(0,END)
            return

def leave(event):
    if BikeNumbers.get()=='':
        BikeNumbers.insert(0,"Bike number")
BikeNumbers=Entry(frame,width=20,bd=5, font= ("Arial",10,"bold"))
BikeNumbers.place(x=190,y=60)
BikeNumbers.insert(0,"Bike number")
BikeNumbers.bind('<FocusIn>',enter)
BikeNumbers.bind('<FocusOut>',leave)



def enter(event):
    # p = BikePikupLocation.get()
    # print(p)
    global fBikeCondition
    if (fBikeCondition == 1):
        if(BikeCondition.get() == "Bike Condition"):
            BikeCondition.delete(0,END)
            return


def leave(event):
    if BikeCondition.get()=='':
        BikeCondition.insert(0,"Bike Condition")
BikeCondition=Entry(frame,width=30,bd=5, font= ("Arial",10,"bold"))
BikeCondition.place(x=60,y=190)
BikeCondition.insert(3,"Bike Condition")
BikeCondition.bind("<FocusIn>",enter)
BikeCondition.bind('<FocusOut>',leave)




def enter(event):
    # p = BikePikupLocation.get()
    # print(p)
    global fbIKEprice
    if (fbIKEprice == 1):
        if(Bikeprice.get() == "Bike price"):
            Bikeprice.delete(0,END)
            return


def leave(event):
    if Bikeprice.get()=='':
        Bikeprice.insert(0,"Bike price")
Bikeprice=Entry(frame,width=30,bd=5, font= ("Arial",10,"bold"))
Bikeprice.place(x=60,y=230)
Bikeprice.insert(3,"Bike price")
Bikeprice.bind("<FocusIn>",enter)
Bikeprice.bind('<FocusOut>',leave) 


signup_btn=Button(frame,text="Post",fg='white', bg='blue',width=15,font=('Roboto','12','bold'),command=post)
signup_btn.place(x=90,y=260)
label=Label(frame,text="I have an account",fg='black',bg='white',font=('Roboto',9))
label.place(x=85,y=300)

signin=Button(frame,width=6,text='Sign in',fg='blue',bg='white', bd=0)
signin.place(x=190,y=300)




letsidelogo = Label(text="LET'S UPLOAD THE IMAGE", font=('Roboto','22','bold'), bg='#ADD8E6')
letsidelogo.place(x=60, y=100)



img = Image.open('l.png')
height = 193
width = 350
bike_image = img.resize((width, height), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(bike_image)
Showthebikeimagelabel = Label(image=photo)
Showthebikeimagelabel.place(x=60, y=160)


uploadthebikeimage = Button(text='uploadbikeimage', height=2, width=23, bg='pink',font=('Roboto','12','bold'), command=uploadthebikeimage)
uploadthebikeimage.place(x=110, y=370)



# Impresive
root.mainloop()