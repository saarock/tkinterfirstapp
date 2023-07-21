import tkinter as tk
from PIL import Image, ImageTk
from tkinter import font
# from login import uinqueid
# from keepthedata import uinqueid
from database import mycuror
# For images uploader
from tkinter import filedialog
import os
import shutil
import subprocess
from database import *


# delete_query = "DELETE FROM uploadedbikes"

# # Execute the query
# mycuror.execute(delete_query)

# # Commit the changes
# mydb.commit()

# # Close the cursor and the connection
# mycuror.close()
# mydb.close()









# Getthe module where i have written the program that every user get the 1000 monney by default
#  after the sign up and login
from usergets import give_money
# from paginations import paginations_all

# fOR ALERTPUMP
import tkinter.messagebox as messagebox

# Keepthe_userid 
keeptheuserid = ''
keeptheuserpassword = ''
root = tk.Tk()
root.title('mainLoop')
root.minsize(1200, 1000)
root.state('zoomed')
root.configure(background='#343A40')
#2F2F4F
# Disable window resizing
root.resizable(False, False)

root.iconbitmap('l.png')




# print(uinqueid, 'This is you nuiquesid')



# Lets depickel
import pickle
file = 'useruniqu.pkl'
read_userdata = open(file, 'rb')
userunique_id_for_allthethings = pickle.load(read_userdata)
print(userunique_id_for_allthethings, 'WASDGNALSDJGNSAJKDGAKJDGBKSGBJ,D G')


# Let's get the userid of the user which is unnique and then pikle it for the future use;
mycuror.execute('SELECT username FROM users WHERE id = %s', (userunique_id_for_allthethings,))
user__name = mycuror.fetchone()
print(user__name, 'TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT')
# Keeptheuserid
file = 'username.pkl'
fileobj = open(file, 'wb')
pickle.dump(user__name, fileobj)
fileobj.close()




# Calling the function by giving the user uniue id
give_money(userunique_id_for_allthethings)

from usergets import kepthe_usermoney
print('OK XATE', kepthe_usermoney)



# If
















# Function to uploadimage
def upload_image():
        # messagebox.showinfo('Alert', 'Are you sure to change profile!')
#  ASK SIR IS THERE IS ANY THIS THAT IS LIKE ALERT or Prompt or for confrim
      
    file = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    if(file):
            import os
            file_name = os.path.basename(file)
          #   Let's make ready from uploading the image as a folder
            dir_ = f'profileimage/{file_name}'
            print('You Got a file')
          #   print(file, 'This is the real files')
            image = Image.open(file)
            new_width = 200
            new_height = 160


# Load image 
            imagee = image.resize((new_width, new_height), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(imagee)
            profie_image_label.config(image=photo)
            profie_image_label.image = photo
            if(os.path.exists('profileimage')):
                shutil.rmtree('profileimage')
                os.makedirs('profileimage')
                imagee.save(dir_)
            else:
                 os.makedirs('profileimage')
                 imagee.save(dir_)



if(os.path.exists('profileimage')):
 d = os.listdir('profileimage')
 if(d):
      profile_path = os.path.join('profileimage', d[0])
      print(d, 'You dirssssssssssssss')
      print(d)
      image = Image.open(profile_path)
 else:
      image = Image.open('l.png')
else:
    image = Image.open('l.png')
     
     
      
      
nav = tk.Frame(root, bg='#343A40', pady=105,)
nav.pack(fill='both')

l = tk.Label(nav, bg='skyblue')
l.pack()
photo =  tk.Frame(nav)
    
# Load the image
   
# Resize the image
new_width = 200
new_height = 160


# Load image 
profie_resize = image.resize((new_width, new_height), Image.ANTIALIAS)
tk_image = ImageTk.PhotoImage(profie_resize)






#343a40

image_frame = tk.Frame(root, height=662, bg='#343A40', width=532 ,highlightbackground='#343A40',highlightthickness=2)
image_frame.place(x=40, y=100)
# For profile
profie_image_label  = tk.Label(root, image=tk_image, bg='DarkoliveGreen1')
profie_image_label.place(x=179, y=27)







# User name
username = tk.Label(image_frame, text='Aayush Basnet',font=122) # font= ("Arial",10,"bold")
username.place(x=149, y=156, width=200)

ProfileChange = tk.Button(text='Change profile', font=('Comic Sans MS',10,'bold'),fg='skyblue1',bg="#338bd7", cursor='hand2', padx=19, pady=5, command=upload_image)
ProfileChange.place(x=210, y=204)



# Cut thefeatures_frame
def cut_the_features():
          print('clicked')
          root.update_idletasks()
          features_frame.destroy()
# Let's give thefeature to change thecolorofthewindow according to the user
def changethe_color_of_the_window():
     # image_frame.destroy()
     # bikefeatures_frame.destroy()
     # showbikes.destroy()
     # print('Click')
     #  root.configure(background='red')
     global features_frame
     features_frame = tk.Frame(root, bg='gray',height=703,width=403)
     features_frame.place(x=23)
     buttons_f = tk.Button(features_frame, text='DarkMode', width=20)
     buttons_f.place(x=0)
     # Let'sgive the cut button
     cut_image = Image.open('cut.png')
     h = 33
     w = 33
     siz = cut_image.resize((w,h), Image.ANTIALIAS)
     c= ImageTk.PhotoImage(siz)
     cut_image_label = tk.Button(features_frame,text='cut',command=cut_the_features,cursor='hand2')
     cut_image_label.place(x=342)



# Function to reload the window
def reload_the_window():
     global make,donotmake,root
     # import dash
     # global root

     # New connection for the reload
     mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password= 'Aayush888999',
    database = 'BIKE'
)
    
     mycuror = mydb.cursor()
     file = 'username.pkl'
     read_userdata = open(file, 'rb')
     userid_r = pickle.load(read_userdata)
     print(userid_r)

# Reload the Balance
     sql = "SELECT money FROM usersmoney WHERE userid = %s"
     mycuror.execute(sql, (userid_r[0],))
     result = mycuror.fetchone()
     print(result, 'THIS IS YOUR RESULT OR WE CAN SAY THE MONEY')
     print('Hello World')
     balance.config(text=f'Balance: {result[0]}')
     mycuror.close()
     mydb.close()


     # pass





# This should be in the def but somethings error occurs ask teacher!!!!!!!!!
# Cutimage 
# Load image 
# cut_openimage = Image.open('menu.png')
# new_widthcut = 50
# new_heightcut = 50
# cutresize = cut_openimage.resize((new_widthcut, new_heightcut), Image.ANTIALIAS)
# cutprofile = ImageTk.PhotoImage(cutresize)
# cut_image_label = tk.Button(root, image=cutprofile, bg='#343A40', cursor='hand2',command=changethe_color_of_the_window)
# cut_image_label.place(x=565, y=151)



# fot the reload imageButton
reload_openimage = Image.open('reload.png')
new_widthreload = 50
new_heightreload = 50
reloadresize = reload_openimage.resize((new_widthreload, new_heightreload), Image.ANTIALIAS)
reloadprofile = ImageTk.PhotoImage(reloadresize)
reload_image_label = tk.Button(root, image=reloadprofile, bg='#343A40', cursor='hand2',command=reload_the_window)
reload_image_label.place(x=44, y=151)




# This is teh userdetails bydefault but id user Sign up and then login it'supdate according to the user details on the database
useremail = tk.Label(image_frame, text='Saarock4646@gmail.com',font=122 )
useremail.place(x=149, y=213, width=200)

useruniquename = tk.Label(image_frame, text='UserName: Saarock4646',font=122 )
useruniquename.place(x=149, y=258, width=200)


balance = tk.Label(image_frame, text='Balance: rs2345',font=122)
balance.place(x=149, y=303, width=200)

# mame_changes = tk.Label(root, text='Make Changes', font = ("Montserrat bold", 25), bg='#343A40', fg='DarkoliveGreen1')
# mame_changes.place(x=149, y=450)
# usernamechange = tk.Entry(root, text='Saarock4646@gmail.com',  bg='#343A40')
# usernamechange.place(x=149, y=513)
# usernamechange.insert(1, 'Email change...')

# namechanges = tk.Entry(root,  bg='#343A40')
# namechanges.place(x=149, y=570)
# namechanges.insert(1, 'Fullname change...')


# uniqusernamechange = tk.Entry(root, font = ("Montserrat", 20), bg='#343A40', relief='sunken')
# uniqusernamechange.place(x=149, y=630)
# uniqusernamechange.insert(1, 'username change...')


# makechangesButton = tk.Button(text='Change', font=('Comic Sans MS',10,'bold'),fg='#343A40',bg="#338bd7", cursor='hand2', padx=29, pady=12)
# makechangesButton.place(x=230, y=690)



# Send the money or transation
def sendthemoney():
    try:
            print('I am Clicked')
            subprocess.Popen(['python', 'transition.py'])

    except FileNotFoundError:
            print("Transition script not found. Make sure the file 'transition.py' exists.")





# DATABSE GETTINGALLTHE INFORMATIONS RELATED TO THE BIKES
# Paginations start
trackthepagination1 = 0
trackthepagination2 = 1
how_many_data = 0

mycuror.execute("SHOW TABLES LIKE 'uploadedbikes'")
table_exist_or_not = mycuror.fetchone()
if(table_exist_or_not):
 mycuror.execute("SELECT * FROM uploadedbikes")
#  mycuror.execute("SELECT * FROM uploadedbikes")
# lET'S FETCH ALL THE DATA
 allthe_datas = mycuror.fetchall()
 print(allthe_datas)
 how_many_data = len(allthe_datas)-1

# For showing1 the bikes...
 if(allthe_datas and how_many_data >=1 ):
  print('I AM SEPER MAN AND I AM LEDGRND')
#   Shwbikes1 frame
  showbikes = tk.Frame(root, height=193, width=910, bg='#343A40',highlightbackground='gray',highlightthickness=2)
  showbikes.place(x=600, y=250)
  bike_height0 = 160
  bike_width0 = 190

  for_bike0 = Image.open(f"bikes/{allthe_datas[0][6]}")
  resizebike0 =for_bike0.resize((bike_width0, bike_height0), Image.LANCZOS)
  global noticebikes0
  noticebikes0 = ImageTk.PhotoImage(resizebike0)
  bikes_label0 = tk.Label(showbikes, image=noticebikes0, cursor='hand2', fg='skyblue1', bg='#343A40')
  bikes_label0.place(x=10, y=14)

  model = tk.Label(showbikes, text='MODEL: XCRR',)
  model.place(x=210, y= 17)

  bike_name = tk.Label(showbikes, text=f'Bike Name: {allthe_datas[0][2]}',)
  bike_name.place(x=210, y= 50)
  bike_location = tk.Label(showbikes, text=f'Bikepickup Location: {allthe_datas[0][3]}',)
  bike_location.place(x=210, y= 83)

  bike_number = tk.Label(showbikes, text=f'Bike Number: {allthe_datas[0][5]}',)
  bike_number.place(x=210, y= 120)




  bikefeatures_frame = tk.Frame(showbikes, bg='#343A40')
  bikefeatures_frame.place(x=550, y=4, height=180,width=300)
  conditionofbike= tk.Label(bikefeatures_frame, text='The Condition of bike?')
  conditionofbike.place(x=0)

  conditionwhat= tk.Label(bikefeatures_frame, text=f'{allthe_datas[0][4]}',)
  conditionwhat.place(x=0, y=23)

  price = tk.Label(bikefeatures_frame, text=f'Price: {allthe_datas[0][9]}',)
  price.place(x=0, y=50)


  stock = tk.Label(bikefeatures_frame, text=f'{allthe_datas[0][8]}')
  stock.place(x=0, y=90)

  userid = tk.Label(bikefeatures_frame, text=f'Userid:{allthe_datas[0][7]}' )
  userid.place(x=0, y=130)
  
  imageid = tk.Label(bikefeatures_frame, text=f'UB:{allthe_datas[0][0]}')
  imageid.place(x=200, y=0) 
  upload_date = tk.Label(bikefeatures_frame, text=f'D:{allthe_datas[0][11]}')
  upload_date.place(x=200, y=130)

  addto_card = tk.Button(showbikes, text='Add to card',  width=19, height=1,font= ("Arial",10),bg="#338bd7", command=sendthemoney)
  addto_card.place(x=220, y=156)


#   addto_card = tk.Button(showbikes, text='Add to card',  width=19, height=1,font= ("Arial",10),bg="#338bd7", command=sendthemoney)
#   addto_card.place(x=220, y=156)
# for_showing1_end





# For showing2 the bikes...
  showbikes1 = tk.Frame(root, height=193, width=910, bg='#343A40',highlightbackground='gray',highlightthickness=2)
  showbikes1.place(x=600, y=450)
  bike_height1 = 160
  bike_width1 = 190
# try:
  for_bike1 = Image.open(f"bikes/{allthe_datas[1][6]}")
  resizebike1 =for_bike1.resize((bike_width1, bike_height1), Image.LANCZOS)
  noticebikes1 = ImageTk.PhotoImage(resizebike1)
  bikes_label1 = tk.Label(showbikes1, image=noticebikes1, cursor='hand2', bg='#343A40')
  bikes_label1.place(x=10, y=14)

  model1 = tk.Label(showbikes1, text='MODEL: XCRR')
  model1.place(x=210, y= 17)

  bike_name1 = tk.Label(showbikes1, text=f'Bike Name: {allthe_datas[1][2]}',)
  bike_name1.place(x=210, y= 50)
  bike_location1 = tk.Label(showbikes1, text=f'Bikepickup Location: {allthe_datas[1][3]}',)
  bike_location1.place(x=210, y= 86)

  bike_number1 = tk.Label(showbikes1, text=f'Bike Number: {allthe_datas[1][5]}',)
  bike_number1.place(x=210, y= 120)




  bikefeatures_frame1 = tk.Frame(showbikes1,bg='#343A40')
  bikefeatures_frame1.place(x=550, y=4,  height=180,width=300)
  conditionofbike1= tk.Label(bikefeatures_frame1, text='The Condition of bike?')
  conditionofbike1.place(x=0)

  conditionwhat1= tk.Label(bikefeatures_frame1, text=f'{allthe_datas[1][4]}')
  conditionwhat1.place(x=0, y=23)

  price1 = tk.Label(bikefeatures_frame1, text=f'Price:{allthe_datas[1][9]}')
  price1.place(x=0, y=50)


  stock1 = tk.Label(bikefeatures_frame1, text=f'{allthe_datas[1][8]}')
  stock1.place(x=0, y=90)

  userid1 = tk.Label(bikefeatures_frame1, text=f'Userid:{allthe_datas[1][7]}')
  userid1.place(x=0, y=130)

  imageid1 = tk.Label(bikefeatures_frame1, text=f'UB:{allthe_datas[1][0]}')
  imageid1.place(x=200, y=0) 
  upload_date1 = tk.Label(bikefeatures_frame1, text=f'D:{allthe_datas[1][11]}')
  upload_date1.place(x=200, y=130)

  addto_card1 = tk.Button(showbikes1, text='Add to card',  width=19, height=1,font= ("Arial",10),bg="#338bd7", command=sendthemoney)
  addto_card1.place(x=220, y=156)


# except IOError as e:
#      print(e)

# for_showing2_end


 if(how_many_data==0):
  print('I AM SEPER MAN AND I AM LEDGRND')
  showbikes = tk.Frame(root, height=193, width=910, bg='#343A40')
  showbikes.place(x=600, y=250)
  bike_height0 = 160
  bike_width0 = 190
  for_bike0 = Image.open(f"bikes/{allthe_datas[0][6]}")
  resizebike0 =for_bike0.resize((bike_width0, bike_height0), Image.LANCZOS)
  noticebikes0 = ImageTk.PhotoImage(resizebike0)
  bikes_label0 = tk.Label(showbikes, image=noticebikes0, cursor='hand2', fg='DarkoliveGreen1', bg='#343A40')
  bikes_label0.place(x=10, y=14)
  model = tk.Label(showbikes, text='MODEL: XCRR',)
  model.place(x=210, y= 17)
  bike_name = tk.Label(showbikes, text=f'Bike Name: {allthe_datas[0][2]}',font= ("Arial",16),fg='DarkoliveGreen1', bg='#343A40')
  bike_name.place(x=210, y= 50)
  bike_location = tk.Label(showbikes, text=f'Bikepickup Location: {allthe_datas[0][3]}',)
  bike_location.place(x=210, y= 83)
  bike_number = tk.Label(showbikes, text=f'Bike Number: {allthe_datas[0][5]}',)
  bike_number.place(x=210, y= 120)




  bikefeatures_frame = tk.Frame(showbikes, bg='#343A40')
  bikefeatures_frame.place(x=550, y=14, height=513, width=534)
  conditionofbike= tk.Label(bikefeatures_frame, text='The Condition of bike?')
  conditionofbike.place(x=0)

  conditionwhat= tk.Label(bikefeatures_frame, text=f'{allthe_datas[0][4]}', font = ("Montserrat bold", 10),fg='DarkoliveGreen1', bg='#343A40')
  conditionwhat.place(x=0, y=23)

  price = tk.Label(bikefeatures_frame, text=f'Price: {allthe_datas[0][9]}')
  price.place(x=0, y=50)


  stock = tk.Label(bikefeatures_frame, text=f'Available: {allthe_datas[0][8]}')
  stock.place(x=0, y=90)

  userid = tk.Label(bikefeatures_frame, text=f'Userid: {allthe_datas[0][7]}')
  userid.place(x=0, y=130)

  addto_card = tk.Button(showbikes, text='Add to card',  width=19, height=1,font= ("Arial",10),bg="#338bd7", command=sendthemoney)
  addto_card.place(x=220, y=156)

  upload_date = tk.Label(bikefeatures_frame, text=f'D:{allthe_datas[0][11]}')
  upload_date.place(x=200, y=130)

  imageid = tk.Label(bikefeatures_frame, text=f'UB: {allthe_datas[0][0]}')
  imageid.place(x=200, y=0) 
  addto_card = tk.Button(showbikes, text='Add to card',  width=19, height=1,font= ("Arial",10),bg="#338bd7", command=sendthemoney)
  addto_card.place(x=220, y=156)

# for_showing1_end
      


# Gets the informations from the database
# data changes acording to the  userdetails on the database; 
def to_get_the_user_details():
    global username, useruniquename, useremail, balance, balance,keeptheuserpassword,keeptheuserid
    print(userunique_id_for_allthethings, 'This is')
    mycuror.execute('SELECT * FROM users WHERE id = %s', (userunique_id_for_allthethings,))
    userdatas = mycuror.fetchone()
    print(userdatas, 'THSI THIS THIS THIS')
    username.config(text=userdatas[1])
    useremail.config(text=userdatas[2])
    useruniquename.config(text=userdatas[5])
#     keeptheuserid = userdatas[5]
    keeptheuserpassword = userdatas[4]
#     import pickle
    file = 'money.pkl'
    read_userdata = open(file, 'rb')
    user_money = pickle.load(read_userdata)
    print(user_money, 'WASDGNALSDJGNSAJKDGAKJDGBKSGBJ,D G')
    read_userdata.close()
    # Keepthepassword
    file = 'pa.pkl'
    fileobj = open(file, 'wb')
    pickle.dump(keeptheuserpassword, fileobj)
    fileobj.close()
    
    balance_user = balance.config(text=f'Balance: {user_money}')
to_get_the_user_details()




# NAVBARS
# Navs for home
home_height = 52
home_width = 52
frameforchildnavs = tk.Frame(root, height=132, width=900, bg='#343A40',highlightbackground='#343A40',highlightthickness=2)
frameforchildnavs.place(x=600, y=99)
try:
     for_home = Image.open('hom1.png')
     resize_home = for_home.resize((home_width, home_height), Image.LANCZOS)
     homeImage = ImageTk.PhotoImage(resize_home)
     home_label = tk.Button(frameforchildnavs, image=homeImage, cursor='hand2', bg='#343A40')
     home_label.place(x=66, y=50)
except IOError as e:
       print(e)






# makes click to the contact image label
def on_image_click():
     # import uploadsbikes
     subprocess.Popen(['python', 'uploadsbikes.py'])
     


# Navs for Upload
home_height = 52
home_width = 52
try:
     for_upload = Image.open('upload.png')
     resize_upload = for_upload.resize((home_width, home_height), Image.LANCZOS)
     upload_imagesicon = ImageTk.PhotoImage(resize_upload)
     upload_image_icon_label = tk.Button(frameforchildnavs, image=upload_imagesicon, cursor='hand2', bg='#343A40', command=on_image_click)
     # Bind the click event to the label
    #  upload_image_icon_label.bind("<Button-1>", on_image_click)
     upload_image_icon_label.place(x=142, y=50)
except IOError as e:
       print(e)




# For Notifications
home_height = 52
home_width = 52
try:
     for_notice = Image.open('contact.png')
     resixe_notice =for_notice.resize((home_width, home_height), Image.LANCZOS)
     noticeimage = ImageTk.PhotoImage(resixe_notice)
     notice_lable = tk.Button(frameforchildnavs, image=noticeimage, cursor='hand2', bg='#343A40')
     
     notice_lable.place(x=214, y=50)
except IOError as e:
       print(e)



# For search
search = tk.Text(frameforchildnavs, height=3, width=53,font=('Comic Sans MS',10,'bold'))
search.insert(1.0, 'Search...')
search.place(x=294, y=50)

# For Search icons
home_height = 52
home_width = 52
try:
     for_search = Image.open('search.png')
     search_notice =for_search.resize((home_width, home_height), Image.LANCZOS)
     searchimage = ImageTk.PhotoImage(search_notice)
     search_label = tk.Button(frameforchildnavs, image=searchimage, cursor='hand2', bg='#343A40')
     search_label.place(x=725, y=50)
except IOError as e:
       print(e)


# For other menu

cut_openimage = Image.open('menu.png')
new_widthcut = 50
new_heightcut = 50
cutresize = cut_openimage.resize((new_widthcut, new_heightcut), Image.ANTIALIAS)
cutprofile = ImageTk.PhotoImage(cutresize)
cut_image_label = tk.Button(frameforchildnavs, image=cutprofile, bg='#343A40', cursor='hand2',command=changethe_color_of_the_window)
cut_image_label.place(x=0, y=50)




# BikeBreez logo
home_height = 92
home_width = 120
try:
     for_logo = Image.open('m.png')
     resize_logo =for_logo.resize((home_width, home_height), Image.LANCZOS)
     logoimage = ImageTk.PhotoImage(resize_logo)
     logo_label = tk.Label(frameforchildnavs, image=logoimage, cursor='hand2', bg='#343A40')
     
     logo_label.place(x=804, y=34)
except IOError as e:
       print(e)
# Navbars ENDS;



print(how_many_data, 'asdgnalskdgasjkdbgkjsadbgkjsadbgjksadbgjkasdgklasdng4963564y6')
# Paginations start
show_firstone = 0
def goRight():
 global trackthepagination1, trackthepagination2, how_many_data
 if(how_many_data>1):
     print(trackthepagination1, 'TTTTTTTTTTTTTTTTTT1111111111')
     print(trackthepagination2, 'TTTTTTTTTTTTTTTTTT22222222')
     # if(trackthepagination1 ==0):
     #      trackthepagination1+=2
     if(trackthepagination1<0):
          trackthepagination1+=2

     if(trackthepagination2<0):
          trackthepagination2+=2

     if(trackthepagination1==0):
          trackthepagination1+=2

     if(trackthepagination2==1):
          trackthepagination2+=2
          print('JAY BAHAUBALI')

     if(trackthepagination2 > how_many_data):
          print('DATA OUT OF RANGE')
          trackthepagination2 = how_many_data
          trackthepagination1 = how_many_data-1



     # Starting for the first bike show
     if(trackthepagination1 > how_many_data):
          return
     


     new_image_path0 = f"bikes/{allthe_datas[trackthepagination1][6]}"
     new_image0 = Image.open(new_image_path0)
     bike_height0 = 160
     bike_width0 = 190
    # Resize the new image to fit the label
     new_image0 = new_image0.resize((bike_width0,   bike_height0), Image.LANCZOS)
    # Update the Tkinter image object
     noticebikes0.paste(new_image0)

    # Update the displayed image
     bikes_label1.image = new_image0
     bike_name.config(text=f'Bike Name: {allthe_datas[trackthepagination1][2]}')
     bike_location.config(text=f'Bikepickup Location: {allthe_datas[trackthepagination1][3]}')
     conditionwhat.config(text=allthe_datas[trackthepagination1][4])
     bike_number.config(text=f'Bike Number: {allthe_datas[trackthepagination1][5]}')
     conditionwhat.config(text=f'{allthe_datas[trackthepagination1][4]}')
     price.config(text=f'Price: {allthe_datas[trackthepagination1][9]}')
     stock.config(text=f'{allthe_datas[trackthepagination1][8]}')
     userid .config(text=f'Userid:{allthe_datas[trackthepagination1][7]}')
     upload_date.config(text=f'D:{allthe_datas[trackthepagination1][11]}')
     imageid.config(text=f'UB:{allthe_datas[trackthepagination1][0]}')
     # print(allthe_datas[trackthepagination1][11])

     # if(trackthepagination1 == how_many_data):
     #      return

     # trackthepagination1+=2  
     
     if(trackthepagination2>how_many_data):
          return
     bike_name1.config(text=f'Bike Name: {allthe_datas[trackthepagination2][2]}')
     bike_location1.config(text=f'Bikepickup Location: {allthe_datas[trackthepagination2][3]}')
     conditionwhat1.config(text=allthe_datas[trackthepagination2][4])
     bike_number1.config(text=f'Bike Number: {allthe_datas[trackthepagination2][5]}')
     conditionwhat1.config(text=f'{allthe_datas[trackthepagination2][4]}')
     price1.config(text=f'Price:{allthe_datas[trackthepagination2][9]}')
     stock1.config(text=f'{allthe_datas[trackthepagination2][8]}')
     userid1.config(text=f'Userid:{allthe_datas[trackthepagination2][7]}')
     imageid1.config(text=f'UB:{allthe_datas[trackthepagination2][0]}')
     upload_date1.config(text=f'D:{allthe_datas[trackthepagination2][11]}')

      
          # Chnages the bike image
         # Load the new image

     new_image_path = f"bikes/{allthe_datas[trackthepagination2][6]}"
     new_image = Image.open(new_image_path)
     bike_height1 = 160
     bike_width1 = 190
    # Resize the new image to fit the label
     new_image = new_image.resize((bike_width1,   bike_height1), Image.LANCZOS)
    # Update the Tkinter image object
     noticebikes1.paste(new_image)

    # Update the displayed image
     bikes_label1.image = new_image

# Checking the condition to thehow_many_data variable which is assign to the length of the data thatcomes from the database If condition match then return from the function;
     if(how_many_data == trackthepagination2 or trackthepagination1 == how_many_data):
          print('Condition matched1')
          return
     trackthepagination1+=2  
     trackthepagination2+=2

     


def goLeft():
 global trackthepagination1, trackthepagination2, how_many_data
 if( how_many_data>1):

     print(trackthepagination1, 'TTTTTTTTTTTTTTTTTT1111111111')
     print(trackthepagination2, 'TTTTTTTTTTTTTTTTTT22222222')
     # return
     if(trackthepagination1 < 0 or trackthepagination2<0):
          return
          trackthepagination1 = 0
          trackthepagination1 = 1
          
          # return
          # print('Smaller')
          # return
     a = how_many_data-1
     # b = how_many_data+1
     if(trackthepagination1 >2):
      if(trackthepagination1== a ):
          trackthepagination1-=2
      if(trackthepagination2==how_many_data):
          trackthepagination2-=2
     else:
          if(trackthepagination1== a):
               trackthepagination1-=1
          if(trackthepagination2 == how_many_data):
               trackthepagination2-=1



     

     # if(trackthepagination1<0):
 
     bike_name.config(text=f'Bike Name: {allthe_datas[trackthepagination1][2]}')
     bike_location.config(text=f'Bikepickup Location: {allthe_datas[trackthepagination1][3]}')
     conditionwhat.config(text=allthe_datas[trackthepagination1][4])
     bike_number.config(text=f'Bike Number: {allthe_datas[trackthepagination1][5]}')
     conditionwhat.config(text=f'{allthe_datas[trackthepagination1][4]}')
     price.config(text=f'Price: {allthe_datas[trackthepagination1][9]}')
     stock.config(text=f'{allthe_datas[trackthepagination1][8]}')
     userid .config(text=f'Userid:{allthe_datas[trackthepagination1][7]}')
     upload_date.config(text=f'D:{allthe_datas[trackthepagination1][11]}')
     imageid.config(text=f'UB:{allthe_datas[trackthepagination1][0]}')
     new_image_path0 = f"bikes/{allthe_datas[trackthepagination1][6]}"
     new_image0 = Image.open(new_image_path0)
     bike_height0 = 160
     bike_width0 = 190
    # Resize the new image to fit the label
     new_image0 = new_image0.resize((bike_width0,   bike_height0), Image.LANCZOS)
    # Update the Tkinter image object
     noticebikes0.paste(new_image0)
 
     # trackthepagination1-=1


     if(trackthepagination2> how_many_data):
          trackthepagination2-=2
          # trackthepagination2-=1
     bike_name1.config(text=f'Bike Name: {allthe_datas[trackthepagination2][2]}')
     bike_location1.config(text=f'Bikepickup Location: {allthe_datas[trackthepagination2][3]}')
     conditionwhat1.config(text=f'{allthe_datas[trackthepagination2][4]}')
     bike_number1.config(text=f'Bike Number: {allthe_datas[trackthepagination2][5]}')
     conditionwhat1.config(text=f'{allthe_datas[trackthepagination2][4]}')
     price1.config(text=f'Price:{allthe_datas[trackthepagination2][9]}')
     stock1.config(text=f'{allthe_datas[trackthepagination2][8]}')
     userid1.config(text=f'Userid:{allthe_datas[trackthepagination2][7]}')
     imageid1.config(text=f'UB:{allthe_datas[trackthepagination2][0]}')
     upload_date1.config(text=f'D:{allthe_datas[trackthepagination2][11]}')



     # Chnages the bike image
         # Load the new image
     new_image_path = f"bikes/{allthe_datas[trackthepagination2][6]}"
     new_image = Image.open(new_image_path)
     bike_height1 = 160
     bike_width1 = 190
    # Resize the new image to fit the label
     new_image = new_image.resize((bike_width1,   bike_height1) , Image.LANCZOS)

    # Update the Tkinter image object
     noticebikes1.paste(new_image)

    # Update the displayed image
     # bikes_label1 .configure(image=tk_image)
     bikes_label1.image = new_image
     if( trackthepagination1==0 or trackthepagination2==0):
          return
     
     if(trackthepagination1==1 and trackthepagination2 == 2):
          second_one = trackthepagination1
          trackthepagination1= show_firstone
          trackthepagination2 = second_one
          return
     trackthepagination2-=2
     trackthepagination1-=2 
     


# noticebikes0






# Fo the pagination
# paginations_all()
# def paginations_all():

# MAKE THIS PUT IN THE FUNCTION
# This is for the left paginations
paginations_frame = tk.Frame(root, height=116, width=910, bg='#343A40',highlightbackground='#343A40',highlightthickness=2)
paginations_frame.place(x=600, y=650)
go_left = Image.open('left.png')
home_height = 42
home_width = 80
resizeleft =go_left.resize((home_width, home_height), Image.LANCZOS)
leftimage = ImageTk.PhotoImage(resizeleft)
left_label = tk.Button(paginations_frame, image=leftimage, cursor='hand2', bg='#343A40', command=goLeft)
left_label.place(x=0, y=35)


# paginations_all()
# This is for the right paginations
go_right = Image.open('right.png')
home_height = 42
home_width = 80
resizeright =go_right.resize((home_width, home_height), Image.LANCZOS)
rightimage = ImageTk.PhotoImage(resizeright)
right_label = tk.Button(paginations_frame, image=rightimage, cursor='hand2', bg='#343A40', command=goRight)
right_label.place(x=825, y=35)



# # Keeptheuserid
# file = 'username.pkl'
# fileobj = open(file, 'wb')
# pickle.dump(keeptheuserid, fileobj)
# fileobj.close()

# # Keepthepassword
# file = 'pa.pkl'
# fileobj = open(file, 'wb')
# pickle.dump(keeptheuserpassword, fileobj)
# fileobj.close()


# Function to showthebikes ofthe user

def showmybikes():
     root.destroy()
     import ownbikes





# footer for to contact socially and user details of bikes , Notifications;
def footer():
     global ImageTk,Image
     footer_frame = tk.Frame(root, height=53,width=1464, bg='#343A40', highlightbackground='#343A40',highlightthickness=2)
     footer_frame.place(x=43,y=772)
     label= tk.Label(footer_frame, text='My namenisaaysh abset')
     label.place(x=23,y=2342)
     notification = Image.open('noti.png')
     h= 40
     w= 40
     n_s = notification.resize((w,h),Image.LANCZOS)
     n_img =ImageTk.PhotoImage(n_s)
     noti_label = tk.Button(footer_frame, image=n_img)
     # Load the image under the noti_label to show note(in the function without doing this we cannot show the image but at global we can)
     noti_label.image = n_img  
     noti_label.place(x=3,y=4)

     # images button to contact on the sociall media of the owners

# Button to look ownb bikes uploaded
     button_for_my_bikes = tk.Button(footer_frame, text='My bikes',height=2,width=12, bg='DarkoliveGreen1',fg='#343A40',command=showmybikes)
     button_for_my_bikes.place(x=1360,y=5)

footer()






# To delete the datafrom the databae tabel





root.mainloop()
