from tkinter import *
from tkinter import ttk


import os
from tkinter.font import BOLD
import matplotlib.pyplot as plt

from PIL import ImageTk
from PIL import ImageOps
from PIL import Image

from functools import partial
#from tkHyperLinkManager import HyperlinkManager
from tkinter import messagebox
import logging
import json

import bcrypt  
import sys  

l_img_path=os.path.join(os.getcwd(),'images','bg.jpg')
l_fxpos=250
l_fypos=140
l_fwidth=880
l_fhieght=480

#l_fields={1:'Fisrt Name',2:'Last Name',3:'New Password',4:'Confirm Password',7:'Contact Number',8:'Email',9:'Security Question'
#          ,10:'Security Answer'}
l_agree_txt="I Agree with The Terms & Conditions"

def write_json(keyval1,new_data={},  db=False,filename='sample.json'):
        print(filename)
        print(keyval1)
        print('\n')
        print(new_data)
        if db:
            conn=mysql.connector.connect(host='localhost',user='root',password='Test@123',database='Testproj')
            cur=conn.cursor()
            query=("select * from register where email=%s")
            cur.execute(query,user_id)
            rpw=cur.fetchone()
            if row!=None:
                messagebox.showerror("Error",'E-mail is already Registered')
            else:
                l=list(json_load1['User_Details'][l_key].values())
                cur.execute("insert into register (%s%s%s%s%s%s%s%s%s)",(l[0],l[1],l[2],l[3],l[4],l[5],l[6],l[7]))
            conn.commit()
            conn.close()
        else:
            with open(filename,'r+') as file:
            # First we load existing data into a dict.
                file_data = json.load(file)
                # Join new_data with file_data inside emp_details
                #file_data["User_Details"].append(new_data)
                file_data["User_Details"][keyval1]=new_data
                # Sets file's current position at offset.
                file.seek(0)
                # convert back to json.
                json.dump(file_data, file, indent = 4)


class Register(object):
    """description of class"""
    def __init__(self,root):
        self.root=root
        self.root.title='Register'
        self.root.geometry("1600x900+0+0")
        l_f_x=70
        l_f_y=10
        l_f_w=200
        
        self.var_FisrtName = StringVar()
        self.var_LastName = StringVar()
        self.var_NewPassword = StringVar()
        self.var_ConfirmPassword = StringVar()
        self.var_ContactNumber = StringVar()
        self.var_Email = StringVar()
        self.var_SecurityQuestion = StringVar()
        self.var_SecurityAnswer = StringVar()
        self.var_user  = StringVar()
        
        self.bg_img=ImageTk.PhotoImage(file=l_img_path)
       
        lbl_bg=Label(self.root,image=self.bg_img)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)
        
        frame=Frame(self.root)
        frame.place(x=l_fxpos,y=l_fypos,width=l_fwidth,height=l_fhieght)
        #Label( frame, text="Registration in progress",font="bold",fg='darkgreen').place(x=l_f_x,y=l_f_y,width=l_f_w  )
        
        l_f_y1=l_f_y
        
        l_f_x1=10
        #l_f_y1=l_f_y1+50
        l_f_w1=120
        
        l_f_x2=125
        l_f_w2=150
        
        l_f_x3=280
        l_f_x4=390
        
        Label( frame, text="Registration in progress",font="bold",fg='darkgreen').place(x=l_f_x2+40,y=l_f_y,width=l_f_w  )
        l_f_y1=l_f_y1+30
        fname=Label(frame,text='First Name:').place(x=l_f_x1,y=l_f_y1,width=l_f_w1  )
        self.fnameentry=ttk.Entry(frame,textvariable=self.var_FisrtName).place(x=l_f_x2,y=l_f_y1,width=l_f_w2  )
        
        lname=Label(frame,text='Last Name:').place(x=l_f_x3,y=l_f_y1,width=l_f_w1  )
        self.lnameentry=ttk.Entry(frame,textvariable=self.var_LastName).place(x=l_f_x4,y=l_f_y1,width=l_f_w2  )
 
        l_f_y1=l_f_y1+30
        fuser=Label(frame,text='User Name:').place(x=l_f_x1,y=l_f_y1,width=l_f_w1  )
        self.fuserentry=ttk.Entry(frame,textvariable=self.var_user).place(x=l_f_x2,y=l_f_y1,width=l_f_w2  )
      
        l_f_y1=l_f_y1+30
        fpass=Label(frame,text='New Password:').place(x=l_f_x1,y=l_f_y1,width=l_f_w1  )
        self.fpassentry=ttk.Entry(frame,textvariable=self.var_NewPassword).place(x=l_f_x2,y=l_f_y1,width=l_f_w2  )
        
        cpass=Label(frame,text='Confirm Password:').place(x=l_f_x3,y=l_f_y1,width=l_f_w1  )
        self.cpassentry=ttk.Entry(frame,textvariable=self.var_ConfirmPassword).place(x=l_f_x4,y=l_f_y1,width=l_f_w2  )
        
        l_f_y1=l_f_y1+30
        contnum=Label(frame,text='Contact Number:').place(x=l_f_x1,y=l_f_y1,width=l_f_w1  )
        self.contnumentry=ttk.Entry(frame,textvariable=self.var_ContactNumber).place(x=l_f_x2,y=l_f_y1,width=l_f_w2  )
        
        em=Label(frame,text='Email:').place(x=l_f_x3,y=l_f_y1,width=l_f_w1  )
        self.emeentry=ttk.Entry(frame,textvariable=self.var_Email).place(x=l_f_x4,y=l_f_y1,width=l_f_w2  )

        l_f_y1=l_f_y1+30
        seq_q=Label(frame,text='Security Question:').place(x=l_f_x1,y=l_f_y1,width=l_f_w1  )
        self.secqentry=ttk.Combobox(frame,textvariable=self.var_SecurityQuestion)
        self.secqentry["values"]=("Select","Your Birth Place","Your Pet Name",'Your Fav. Place')
        self.secqentry.current(0)
        self.secqentry.place(x=l_f_x2,y=l_f_y1,width=l_f_w2  )
        
        
        sec_a=Label(frame,text='Security Answer:').place(x=l_f_x3,y=l_f_y1,width=l_f_w1  )
        self.secaentry=ttk.Entry(frame,textvariable=self.var_SecurityAnswer).place(x=l_f_x4,y=l_f_y1,width=l_f_w2  )
        
        '''

        for k,j in l_fields.items():
            
            l_f_name='self.'+j.replace(' ','')+'entry'
            l_v_name='self.var_'+j.replace(' ','')
            #print(l_v_name)
           # for i in l_v_name:
           #     i=StringVar()
            #globals()[f"{l_v_name}"] = StringVar()
            
            #globals()[l_v_name] = StringVar()
            #exec("%s = %s" % (l_v_name,StringVar()))
           
        #print(self.var_FisrtName)
            
            if k%2==0:
               
                
                self.j=Label(frame,text=j+':').place(x=l_f_x3,y=l_f_y1,width=l_f_w1  )
                #l_f_name=ttk.Entry(frame).place(x=l_f_x4,y=l_f_y1,width=l_f_w2  )
                if j=='Security Question':
                    
                    l_f_name=ttk.Combobox(frame,state='readonly')
                    #l_f_name["values"]=("Select","Your Birth Place")
                else:
                        l_f_name=ttk.Entry(frame,textvariable=l_v_name).place(x=l_f_x4,y=l_f_y1,width=l_f_w2  )
            else:
                l_f_y1=l_f_y1+30
                
                self.j=Label(frame,text=j+':').place(x=l_f_x1,y=l_f_y1,width=l_f_w1  )
                #l_f_name=ttk.Entry(frame).place(x=l_f_x2,y=l_f_y1,width=l_f_w2  )
                if j=='Security Question':
                    
                     
                    self.combo_sec_q=ttk.Combobox(frame,textvariable=l_v_name)
                    self.combo_sec_q["values"]=("Select","Your Birth Place","Your Pet Name",'Your Fav. Place')
                    self.combo_sec_q.place(x=l_f_x2,y=l_f_y1,width=l_f_w2  )
                    self.combo_sec_q.current(0)
                    
                else:
                        l_f_name=ttk.Entry(frame,textvariable=l_v_name).place(x=l_f_x2,y=l_f_y1,width=l_f_w2  )
        
        '''
        self.var_chkbox=IntVar()
        l_chk_box=Checkbutton(frame,variable=self.var_chkbox, text=l_agree_txt,onvalue=1,offvalue=0)
        l_f_y1=l_f_y1+30
        l_chk_box.place(x=10,y=l_f_y1,width=250)
               
        img=Image.open(os.path.join(os.getcwd(),'images','register_button.png'))
        img=ImageOps.fit(img, (90, 20), Image.ANTIALIAS)
        self.photimg=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photimg,command=self.register_data,cursor="hand2")
        l_f_y1=l_f_y1+30
        b1.place(x=50,y=l_f_y1,width=90)
        #==============Fields===============##########
    
    
     

    def encrypt_the_string(self,p_pass,number_of_rounds=16):  
        salt_object = bcrypt.gensalt(rounds=number_of_rounds) 
        p_pass=p_pass.encode('utf-8') 
        resultant_hashed_str = bcrypt.hashpw(p_pass, salt_object)  
        print("The encrypted text or password is: {}".format(resultant_hashed_str))  
        return resultant_hashed_str 
    
    def decrypt_the_string(self,p_pass, number_of_rounds=16):  
        salt_object = bcrypt.gensalt(rounds=number_of_rounds)  
        p_pass=p_pass.encode('utf-8') 
        resultant_hashed_str = bcrypt.hashpw(p_pass, salt_object)  
        if bcrypt.checkpw(p_pass, resultant_hashed_str):  
            return True  
        else:  
            return False  
    
    def register_data(self):
        #var_user
        if self.var_user.get() =='':
            messagebox.showerror("Error","enter UserID")
        elif self.var_FisrtName.get()=='':
            messagebox.showerror("Error","enter value for First Name")
        elif self.var_LastName.get()=='':
            messagebox.showerror("Error","enter value for Last Name")    
        elif self.var_NewPassword.get()=='' or self.var_ConfirmPassword.get()=='':
            messagebox.showerror("Error","Password or Confirm password is null")
        elif self.var_NewPassword.get() != self.var_ConfirmPassword.get() :
            messagebox.showerror("Error","Password and Confirm Password are not matching!!")
        elif self.var_chkbox.get()==0:
            messagebox.showerror("Error","Please accept Terms and Conditions")
        elif self.var_SecurityQuestion.get()=='Select':
            messagebox.showerror("Error","Please Select Security Question")
        elif self.var_SecurityAnswer.get()=='':
            messagebox.showerror("Error","Please enter Answer to Security Question")
        else:
           # l_json_dict={'userid':self.var_user.get(),
           #              'fname':self.var_FisrtName.get(),
           #              'lname':self.var_LastName.get(),
           #              'password': self.encrypt_the_string(self.var_NewPassword.get()).strip().decode(),
           #              'contactnum':self.var_ContactNumber.get(),
           #              'email':self.var_Email.get(),
           #              'sec_q':self.var_SecurityQuestion.get(),
           #              'sec_a':self.var_SecurityAnswer.get()}
            
            
            l_json_dict={
                         'fname':self.var_FisrtName.get(),
                         'lname':self.var_LastName.get(),
                         'password': self.encrypt_the_string(self.var_NewPassword.get()).strip().decode(),
                         'contactnum':self.var_ContactNumber.get(),
                         'email':self.var_Email.get(),
                         'sec_q':self.var_SecurityQuestion.get(),
                         'sec_a':self.var_SecurityAnswer.get()}
                
                
            
            #with open("sample.json", "w") as outfile:
            #    json.dump(l_json_dict, outfile,indent=4)
            #self.write_json(l_json_dict)
            write_json(keyval1=self.var_user.get(),new_data=l_json_dict)
            
            messagebox.showinfo('Success','Registration Successfull')
           
            
            
            

#if __name__=='__main__':
#    root=Tk()
#    app=Register(root)
#    root.mainloop()




