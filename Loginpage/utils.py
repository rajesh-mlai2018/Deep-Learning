from tkinter import messagebox
import mysql
def populate_db(user_id,Email_id,userdetails=[]):
    conn=mysql.connector.connect(host='localhost',user='root',password='Test@123',database='Testproj')
    cur=conn.cursor()
    query=("select * from register where email=%s")
    cur.execute(query,user_id)
    rpw=cur.fetchone()
    if row!=None:
        messagebox.showerror("Error",'E-mail is already Registered')
    else:
        cur.execute("insert into register (%s%s%s%s%s%s%s%s%s)",())