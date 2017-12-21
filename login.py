from tkinter import *
from tkinter import messagebox
from SqlServerHelper import *

#def thread_job():
#    print("this is a thread of %s"%threading.current_thread())

#def main():
#   thread=threading.Thread(target=thread_job)
#    thread.start()

    
#if __name__ == '__main__':
#    main()

#主界面
mainWindow=Tk()
#root.title = "Hello"
mainWindow .geometry("450x300+10+10")

#欢迎图片
canvas=Canvas(mainWindow,height=200,width=500)
image_file=PhotoImage(file="c:\\welcome.gif")
image=canvas.create_image(0,0,anchor="nw",image=image_file)
canvas.pack(side="top")

#显示的Label
lblUserName=Label(mainWindow,text="用户名:")
lblUserName.place(x=50,y=150)

lblPwd=Label(mainWindow,text="密码:")
lblPwd.place(x=50,y=190)

var_user_name=StringVar()
var_user_name.set("admin")
entry_user_name=Entry(mainWindow,textvariable=var_user_name)
entry_user_name.place(x=160,y=150)

var_user_pwd=StringVar()
entry_user_pwd=Entry(mainWindow,textvariable=var_user_pwd,show="*")
entry_user_pwd.place(x=160,y=190)


#登录事件
def user_login():
    try:#加入try catch
       var_name=entry_user_name.get()
       var_pwd=entry_user_pwd.get()
       objSqlServerHelper=SqlServerHelper()
       lst=objSqlServerHelper.Select("select * from employees")
       for obj in lst:
          if obj[1]==var_name:
            if obj[3]==var_pwd:
               messagebox.showinfo(title="登录成功", message="欢迎, "+var_name)
               return
       messagebox.showwarning(title="登录失败", message="用户名或密码错误")
    except Exception as e:
       print(e)#加入打印
       
#注册事件
def user_sign_up():

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
       lst=objSqlServerHelper.Select("select * from employees")
       for obj in lst:
          if obj[1]==var_new_name:
               messagebox.showwarning(title="注册失败", message="用户名："+var_new_name+"，已存在！")
               return
       
       my_cursor=objSqlServerHelper.get_cursor()
       tsql = "INSERT INTO Employees (Name, Pwd) VALUES (?,?);"
       with cursor.execute(tsql,var_new_name,var_new_pwd):
          messagebox.showinfo(title="成功", message="注册成功, "+var_new_name)
          var_user_name.set(var_new_name)
          window_sign_up.destroy()

    btn_comfirm_sign_up = Button(window_sign_up, text="确定", command=comfirm_sign_up)
    btn_comfirm_sign_up.place(x=150, y=130)


#加入按钮
btn_login=Button(mainWindow,text="登录",command=user_login)
btn_login.place(x=160,y=230)

btn_sigh_up=Button(mainWindow,text="注册",command=user_sign_up)
btn_sigh_up.place(x=270,y=230)


mainWindow.mainloop()
