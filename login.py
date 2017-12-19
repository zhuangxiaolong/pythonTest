import tkinter as tk
from tkinter import messagebox

def user_login():
    tk.messagebox.showinfo(title="login",message="just a test")

def user_sign_up():
    tk.messagebox.showinfo(title="sign up",message="ok, you sign up success")

window=tk.Tk()
window.title = "Hello"
window .geometry("450x300+10+10")
#welcome image
canvas=tk.Canvas(window,height=200,width=500)
image_file=tk.PhotoImage(file="c:\\welcome.gif")
image=canvas.create_image(0,0,anchor="nw",image=image_file)
canvas.pack(side="top")

#user information
lblUserName=tk.Label(window,text="User Name:")
lblUserName.place(x=50,y=150)

lblPwd=tk.Label(window,text="Password:")
lblPwd.place(x=50,y=190)

var_user_name=tk.StringVar()
var_user_name.set("admin")
entry_user_name=tk.Entry(window,textvariable=var_user_name)
entry_user_name.place(x=160,y=150)

var_user_pwd=tk.StringVar()
entry_user_pwd=tk.Entry(window,textvariable=var_user_pwd,show="*")
entry_user_pwd.place(x=160,y=190)

#login and sign up button
btn_login=tk.Button(window,text="Login",command=user_login)
btn_login.place(x=160,y=230)

btn_sigh_up=tk.Button(window,text="Sign up",command=user_sign_up)
btn_sigh_up.place(x=270,y=230)


window.mainloop()