from tkinter import *
from tkinter import messagebox
from SqlServerHelper import *
from signUp import *

#def thread_job():
#    print("this is a thread of %s"%threading.current_thread())

#def main():
#   thread=threading.Thread(target=thread_job)
#    thread.start()

    
#if __name__ == '__main__':
#    main()

#主界面
mainWindow=Tk()
mainWindow.title("登录")
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

#登录事件
def user_login():
    try:#加入try catch
       var_name=entry_user_name.get()
       var_pwd=entry_user_pwd.get()
       objSqlServerHelper=SqlServerHelper()
       lst=objSqlServerHelper.execute4lst("select * from employees")
       for obj in lst:
          if obj[1]==var_name:
            if obj[3]==var_pwd:
               messagebox.showinfo(title="登录成功", message="欢迎, "+var_name)
               return
       messagebox.showwarning(title="登录失败", message="用户名或密码错误")
    except Exception as e:
       print(e)#加入打印
       
var_user_name=StringVar()
var_user_name.set("admin")
entry_user_name=Entry(mainWindow,textvariable=var_user_name)
entry_user_name.place(x=160,y=150)

var_user_pwd=StringVar()
entry_user_pwd=Entry(mainWindow,textvariable=var_user_pwd,show="*")
entry_user_pwd.place(x=160,y=190)

#加入按钮
btn_login=Button(mainWindow,text="登录",command=user_login)
btn_login.place(x=160,y=230)

def user_sign_up():
    #调用注册类
    objSignUp=SignUp()
    objSignUp.user_sign_up(mainWindow)

btn_sigh_up=Button(mainWindow,text="注册",command=user_sign_up)
btn_sigh_up.place(x=270,y=230)


mainWindow.mainloop()
