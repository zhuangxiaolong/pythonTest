from tkinter import *
from tkinter import messagebox
from SqlServerHelper import *

class SignUp:
    def __init__(self):  
        print("hello")
#注册事件
    def user_sign_up(self,mainWindow):
           window_sign_up=Toplevel(mainWindow)
       
           window_sign_up.geometry("350x200")
           window_sign_up.title("老铁，注册一个账号吧")
           var_new_name = StringVar()#将输入的注册名赋值给变量
           var_new_name.set("老铁")#将最初显示定为
           Label(window_sign_up, text="用户名: ").place(x=10, y= 10)#将`User name:`放置在坐标（10,10）。
           entry_new_name = Entry(window_sign_up, textvariable=var_new_name)#创建一个注册名的`entry`，变量为`new_name`
           entry_new_name.place(x=150, y=10)#`entry`放置在坐标（150,10）.
       
           var_new_pwd = StringVar()
           Label(window_sign_up, text="密码: ").place(x=10, y=50)
           entry_usr_pwd = Entry(window_sign_up, textvariable=var_new_pwd, show='*')
           entry_usr_pwd.place(x=150, y=50)
       
           new_pwd_confirm = StringVar()
           Label(window_sign_up, text="确认密码: ").place(x=10, y=90)
           entry_usr_pwd_confirm = Entry(window_sign_up, textvariable=new_pwd_confirm, show='*')
           entry_usr_pwd_confirm.place(x=150, y=90)
       
           #处理注册事件
           def comfirm_sign_up():
              var_new_name=entry_new_name.get()
              var_new_pwd=entry_usr_pwd.get()
              var_new_confirm_pwd=entry_usr_pwd_confirm.get()
       
              if var_new_pwd!=var_new_confirm_pwd:
                   messagebox.showwarning(title="注册失败", message="两次密码输入不一致!")
                   return
                
             
              objSqlServerHelper=SqlServerHelper()
              #检查是否已存在
              lst=objSqlServerHelper.execute4lst("select * from employees")
              for obj in lst:
                 if obj[1]==var_new_name:
                      messagebox.showwarning(title="注册失败", message="用户名："+var_new_name+"，已存在！")
                      return
              
              tsql = "INSERT INTO Employees (Name, Pwd) VALUES (?,?);"
              args=(var_new_name,var_new_pwd)
              try:
                 objSqlServerHelper.insert(tsql,args)
                 messagebox.showinfo(title="成功", message="注册成功, "+var_new_name)
                 var_user_name.set(var_new_name)
                 window_sign_up.destroy()
              except Exception as e:
                 print(e)#加入打印
       
           def cannel_sign_up():
                 window_sign_up.destroy()
       
           btn_comfirm_sign_up = Button(window_sign_up, text="确定", command=comfirm_sign_up)
           btn_comfirm_sign_up.place(x=150, y=130)
           btn_cannel_sign_up = Button(window_sign_up, text="取消", command=cannel_sign_up)
           btn_cannel_sign_up.place(x=250, y=130)

