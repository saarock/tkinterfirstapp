
from database import *

import pickle
# If the user get's visit to the Homehe/she gets the 10000rs by default
kepthe_usermoney = 0

def give_money(u):
 global kepthe_usermoney
 try:
     file = 'username.pkl'
     fileobj = open(file, 'rb')
     userid = pickle.load(fileobj)
     fileobj.close()
     print(userid,'THIS IS THE USER UNIQUE ID')

    # let'sgive the user monry
# give_user_money = 1000
     give_usermoney = 10000
     date = 'date'
     table_name = 'usersmoney'
     print(u,userid, 'MY NAME IS AAYUSH BASNET AND MY ANOTHER NAME IS ')
     mycuror.execute("SHOW TABLES LIKE 'usersmoney'")
     tabel_exist= mycuror.fetchone()
     if(tabel_exist):
        print('Tabel is exist')
        existing_email_query = "SELECT COUNT(*) FROM usersmoney WHERE userunique_id_for_allthethings = %s AND  userid = %s"
        mycuror.execute(existing_email_query, (u,userid[0]))
        email_count = mycuror.fetchone()[0]
        print(email_count,'IS THIS IS')
        print(email_count, 'rrrrrrrrrrrrrrrrrrrrrrrrrrrr')
        if(email_count == 0):
        #    mycuror.execute(create_table)
        #    mydb.commit()
           print('OK I AM RI')
           datas = '''
    INSERT INTO usersmoney (userunique_id_for_allthethings, userid, money)
    VALUES (%s, %s, %s)
     '''
        

           print(u, userid, give_usermoney, 'THISN ARE THE VALUE WHICH I WANT TOSAVE')
           values = (u, userid[0], give_usermoney)
           mycuror.execute(datas, values)
           print(34)
           mydb.commit()
        #    Close the connection and the database
        else:
            print(35)
            sql = "SELECT money FROM usersmoney WHERE userid = %s"
            mycuror.execute(sql, (userid[0],))
            result = mycuror.fetchone()
            print(result, 'THIS IS YOUR RESULT OR WE CAN SAY THE MONEY')
            kepthe_usermoney = result[0]
            # Keepthepassword
            file = 'money.pkl'
            fileobj = open(file, 'wb')
            pickle.dump(result[0], fileobj)
            # Commit the changes
            fileobj.close()



            


        # mycuror.execute(create_table)
        # mydb.commit()
    #     datas = '''
    # INSERT INTO usersmoney (userunique_id_for_allthethings, userid, money)
    # VALUES (%s, %s, %s)
    #  '''
    #     values = (u, userid, give_usermoney)
    #     mycuror.execute(datas, values)
    #     mycuror.close()
    #     mydb.close()
     else:
        print(36)
        print('TABEL IS NNOT EXISRT')
        # If the tabel is not exist then run from here
        print('Tabel is not exist')
        create_table =  f"""
      CREATE TABLE {table_name} (
        id INT AUTO_INCREMENT PRIMARY KEY,
        userunique_id_for_allthethings VARCHAR(255),
        userid VARCHAR(255),
        money VARCHAR(233),
        {date} DATE NOT NULL DEFAULT (CURRENT_DATE())

        
    )
"""     
        print('i amstill running')
        mycuror.execute(create_table)
        print('i am strill')
        mydb.commit()
        datas = '''
    INSERT INTO usersmoney (userunique_id_for_allthethings, userid, money)
    VALUES (%s, %s, %s)
     '''
        
        values = (u, userid, give_usermoney)
        mycuror.execute(datas, values)
        
 except Exception as e:
    print(e,'THISN IS YOU ERROR')
 finally:
    print('last')
    # mycuror.close()
    # mydb.close()

 
    # db


