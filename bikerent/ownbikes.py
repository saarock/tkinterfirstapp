from tkinter import *

import pickle
from PIL import Image,ImageTk
from database import *
# This is the anotherwindow to look the uploaded bikes 
root = Tk()


root.minsize(1200, 1000)
root.state('zoomed')
root.configure(background='#FDF5E6')
# Disable window resizing
root.resizable(False, False)

# Let'spicke the username which unique

read_file = 'username.pkl'
uni_userid = open(read_file, 'rb')
user_id_which_unique = pickle.load(uni_userid)
print(user_id_which_unique)



# make available

def makeavailable(n):
#    button =button_
   keep = int(n)
   print(type(keep))
   print(keep, 'THIS IS YOU CLICKED')
   print('I MA CLICKED FFFFFFFFFFFFFFFFFFFFFFFFFFU ')
   print(keep)
   
   if(isinstance(keep,int)):
        try:
         print('You are right',user_id_which_unique[0])
         query_foravai = "UPDATE uploadedbikes SET available = %s WHERE userid= %s AND id = %s"
         avai ='YES'
         mycuror.execute(query_foravai,(avai, user_id_which_unique[0],keep))
         mydb.commit()
         m = make.cget('text')
         print(m)
         make.config(text='DONE')
        
        except Exception as e:
           print(e)
        #  keep = ''
        #  return
      
   



# MAKE DISABLE

def makedisable(n):
   print('Hello')
   keep = int(n)
   
   print(keep,'THIS IS YOU CLICKE FOR DISABLE')

        #  mycuror.close()
        #  mydb.close()
        #  print('DONE')
   if(isinstance(keep,int)):
         print('Milyo')
         query_foravai = "UPDATE uploadedbikes SET available = %s WHERE userid= %s AND id=%s"
         avai ='NO'
         mycuror.execute(query_foravai,(avai,  user_id_which_unique[0], keep))
         mydb.commit()
         donotmake.config(text = 'Done')
         print('NAACHO')
        #  keep = ''
   else:
      pass
   pass
   



button_dict= {}
def load():
    global donotmake, make
    # print('I am running', user_id_which_unique)
    # upframe = Frame(root, height=200, width=1222, bg='gray')
    # upframe.place(x=243,y=33)
    # la_bel = Label(upframe,text='asdgasdgasd')
    # la_bel.place()
    mycuror.execute("SHOW TABLES LIKE 'uploadedbikes'")
    table_exist_or_not = mycuror.fetchone()
    # print(table_exist_or_not)
    if(table_exist_or_not):
      mycuror.execute("SELECT * FROM uploadedbikes")
#  mycuror.execute("SELECT * FROM uploadedbikes")
# lET'S FETCH ALL THE DATA
      allthe_bikes = mycuror.fetchall()
      x = 200
      y = 20
      t = 0
 
    #   if(allthe_datas)
      for allthe_datas in allthe_bikes:
       if(allthe_datas[7]== user_id_which_unique[0]):
            var = IntVar()
            print(allthe_datas[0])
        #   print('I AM SEPER MAN AND I AM LEDGRND')
            showbikes = Frame(root, height=193, width=910, bg='#CDCDC8')
            showbikes.place(x=x, y=y)
            bike_height0 = 160
            bike_width0 = 190
            for_bike0 = Image.open(f"bikes/{allthe_datas[6]}")
            resizebike0 =for_bike0.resize((bike_width0, bike_height0), Image.LANCZOS)
            global noticebikes0
            noticebikes0 = ImageTk.PhotoImage(resizebike0)
            bikes_label0 = Label(showbikes, image=noticebikes0, cursor='hand2', fg='black', bg='#CDCDC8')
            bikes_label0.image = noticebikes0
            bikes_label0.place(x=10, y=14)

            model = Label(showbikes, text='MODEL: XCRR',font= ("Arial",16), fg='black', bg='#CDCDC8')
            model.place(x=210, y= 17)

            bike_name = Label(showbikes, text=f'Bike Name: {allthe_datas[2]}',font= ("Arial",16),fg='black', bg='#CDCDC8')
            bike_name.place(x=210, y= 50)
            bike_location = Label(showbikes, text=f'Bikepickup Location: {allthe_datas[3]}',font= ("Arial",16), fg='black', bg='#CDCDC8')
            bike_location.place(x=210, y= 83)

            bike_number = Label(showbikes, text=f'Bike Number: {allthe_datas[5]}',font= ("Arial",16), fg='black', bg='#CDCDC8')
            bike_number.place(x=210, y= 120)




            bikefeatures_frame = Frame(showbikes, bg='#CDCDC8')
            bikefeatures_frame.place(x=550, y=14, height=513, width=534)
            conditionofbike= Label(bikefeatures_frame, text='The Condition of bike?', bg='#CDCDC8',  font = ("Montserrat bold", 10))
            conditionofbike.place(x=0)

            conditionwhat= Label(bikefeatures_frame, text=f'{allthe_datas[4]}', font = ("Montserrat bold", 10),fg='black', bg='#CDCDC8')
            conditionwhat.place(x=0, y=23)

            price = Label(bikefeatures_frame, text=f'Price: {allthe_datas[9]}',fg='green',font= ("Arial",16))
            price.place(x=0, y=50)


            stock = Label(bikefeatures_frame, text=f'{allthe_datas[8]}' ,fg='green',font= ("Arial",16))
            stock.place(x=0, y=90)

            userid = Label(bikefeatures_frame, text=f'UserId:{allthe_datas[7]}' ,fg='green',font= ("Arial",16))
            userid.place(x=0, y=130)
  
            imageid = Label(bikefeatures_frame, text=f'UB:{allthe_datas[0]}',fg='green',font= ("Arial",16))
            imageid.place(x=200, y=0) 
            upload_date = Label(bikefeatures_frame, text=f'D:{allthe_datas[11]}',fg='green',font= ("Arial",16))
            upload_date.place(x=200, y=130)

            # addto_card = Button(showbikes, text='Add to card',  width=19, height=1,font= ("Arial",10),bg="#338bd7")
            # addto_card.place(x=220, y=156)

            # query = "SELECT available FROM uploadedbikes WHERE userid = %s"
  
  
            # print(user_id_which_unique[0],'THIS IS VALID OR NOT')
            # mycuror.execute(query, (user_id_which_unique[0],))
            # print(2)
            # ownerbike = mycuror.fetchone()
            # print(ownerbike, 'THISN IS THE MESAGE THAT THTE BIKE IS AVAILABLE OR NOT')
            if(allthe_datas[8]== 'NO'):
            #    print('I MATTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT')
               make = Button(showbikes, text=f'make availableto{allthe_datas[0]}',  width=19, height=1,font= ("Arial",10),bg="#338bd7", command= lambda data=allthe_datas[0]: makeavailable(data))
               make.place(x=220, y=156)
            if(allthe_datas[8]=='YES'):
               donotmake = Button(showbikes, text=f'make disableto{allthe_datas[0]}',  width=19, height=1,font= ("Arial",10),bg="#338bd7", command=lambda data=allthe_datas[0]: makedisable(data))
               donotmake.place(x=220, y=156)
            y+=200
            t+=1
            # Multiple queries can executed withe the single execute()
            mycuror.nextset()
       else:
          pass
    else:
      print('Tble does not xist')
      mycuror.close()
      mydb.close()




load()








# Function for backto Home

root = mainloop()