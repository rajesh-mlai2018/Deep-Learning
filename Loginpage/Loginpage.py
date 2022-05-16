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
import register as myreg

def display_image(image):
    fig = plt.figure(figsize=(20, 15))
    plt.grid(False)
    plt.imshow(image)

l_filename='bg.jpg'
l_tmp_file='bg1.jpg'
l_heigth=1550
l_width=800

f_width=610#250
f_height=170#250

f_pos_x =10
f_pox_y=10
for i,j in zip([l_width],[l_heigth]):
    l_gemotry=f'{i}x{j}+0+0'
print('geometry: {}'.format(l_gemotry))

def resize_img(l_filename,l_tmp_file, display=False):
    l_img_path=os.path.join(os.getcwd(),'images',l_filename)
    l_img_path1=os.path.join(os.getcwd(),'images',l_tmp_file)
    
    l_img1=Image.open(l_img_path)
    l_temp_img=ImageOps.fit(l_img1, (l_width, l_heigth), Image.ANTIALIAS)
    
    if display==True:
        display_image(l_temp_img)
    pil_image_rgb = l_temp_img.convert("RGB")
    pil_image_rgb.save(os.path.join(os.getcwd(),'images',l_tmp_file), format="JPEG", quality=90)
    return l_img_path1

l_img_path=resize_img(l_filename,l_tmp_file)    

def callback(event):
    webbrowser.open_new(event.widget.cget("text"))




def validateLogin(username, password):
   print("username entered :", username.get()) 
   print("password entered :", password.get()) 
   return



class LoginPage:
    def __init__(self,rml):
        self.rml=root
        self.rml.title('RAJESH Login Page')
        self.rml.geometry(l_gemotry)

        print(l_img_path)
        self.bg_img=ImageTk.PhotoImage(file=l_img_path)
       
        lbl_bg=Label(self.rml,image=self.bg_img)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)
        
        frame=Frame(self.rml)

        #frame.place(x=450,y=100,width=f_width,height=f_height)
        frame.place(x=570,y=160,width=180,height=160)
        
        #username label and text entry box
        
        Label( frame, text="Login",font="bold").place(x=20,y=10,width=100)#.grid(row=2, column=3)
        #### username and password

        #l_username = input("Enter Username")

        usernameLabel = Label( frame,text="User Name:")
        usernameLabel.place(x=3,y=40,width=70)

        self.txtuser=ttk.Entry(frame)
        self.txtuser.place(x=70,y=40,width=100)
        
        passwordLabel = Label( frame,text="Password:")
        passwordLabel.place(x=3,y=70,width=80)

        self.txtpassentry=ttk.Entry(frame)
        self.txtpassentry.place(x=70,y=70,width=100)

        #validateLogin = partial(validateLogin, username, password)
        #login button
        
        Label( frame, text="  ",font="bold").grid(row=14, column=2) 
        
        #### login button

        loginButton = Button( frame, text="Login", command=self.validLogin)#.grid(row=15, column=3)  
        loginButton.place(x=40,y=100,width=100)

        #Label( frame, text="New User",fg='blue').place(x=4,y=140,width=50)#grid(row=16, column=2) 
        #Label( frame, text="Forgot Password",fg='blue').place(x=60,y=140,width=100)#.grid(row=16, column=3) 

        Label( frame, text="New User",fg='blue').place(x=4,y=140,width=50)#grid(row=16, column=2) 

        reg_btn=Button(frame,text="New User",command=self.reg_windw)

    def validLogin(self):
        if self.txtuser.get()== "" :# or self.passwordEntry.get()=='':
            messagebox.showerror('Error','User name must be entered')
        elif self.txtpassentry.get()=='':
            messagebox.showerror('Error','Password must be entered')
        else:
            messagebox.showinfo('Success','welcome')

    def reg_windw(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

         

        
        


if __name__=="__main__":
    root=Tk()
    app=LoginPage(root)
    root.mainloop()
    


    
