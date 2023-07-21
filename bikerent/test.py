#Read and verify the DB information
def check():
        a=Email.get() #used to retrieve the value entered in an email input field in tkinter.
        b=Password.get()
        try:
            con=sqlite3.connect("client.db")
            c=con.cursor()
            c.execute("SELECT * FROM users")
            record=c.fetchall() #used in Python's SQLite database programming to retrieve all the rows of data returned by a database query.
            i = len(record)-1
            while i>=0:
                if record[i][2]!=a or record [i][3]!=b:
                    i = i-1
                    if i == -1:
                        messagebox.showerror("Login","Invalid")
                        break
                    else:
                        c.execute("""UPDATE users SET
                        satus =:inactive 
                        WHERE status=:active""",
                        {"inactive":False,
                        "active":True})
                        con.commit()  #used in Python's SQLite database programming to save or commit the changes made to the database.
                        
                        
                        c.execute("""UPDATE users SET
                        status=:val
                        WHERE Email =:a""",
                        {
                            'val':True,
                            'a':a 
                        })
                        con.commit()
                        messagebox.showerror("Login","Sign Up First")
                        break
                con.comit()
                con.close()
        except:
            messagebox.showerror("Login","Sign Up First")