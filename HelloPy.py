import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import filedialog
from tkinter import Button
from tkinter import *
import time
import this

ticks = time.time()
print(ticks)
localtime = time.localtime(ticks)
print(localtime)
formatTime = time.asctime(localtime)
print(formatTime)
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))


window = tk.Tk()
#root.mainloop()
window .geometry("800x600+10+10")
window.title = "Hello Python"

on_hit = False  # 默认初始状态为 False
def hit_me():
    global on_hit
    if on_hit == False:     # 从 False 状态变成 True 状态
        on_hit = True
        var.set('you hit me')   # 设置标签的文字为 'you hit me'
    else:       # 从 True 状态变成 False 状态
        on_hit = False
        var.set('')  # 设置 文字为空

def insert_point():
    var=txt.get()
    t.insert('insert',var)
def insert_end():
    var=txt.get()
    t.insert('end',var)

def show_msg_box():
#    tk.messagebox.showinfo(title="Hi",message="hello world, colin")
     tk.messagebox.askquestion(title="Hi",message="hello world, colin")

txt=tk.Entry(window,show="")
txt.pack()

btn = tk.Button(window, text="insert_point", width=50, height=5, command=insert_point)
btn.pack()

btn_insert_end = tk.Button(window, text="insert_end", width=50, height=5, command=insert_end)
btn_insert_end.pack()

var = tk.StringVar()
lbl = tk.Label(window, textvariable=var, bg="green", width=15, height=2)
lbl.pack()

t=tk.Text(window,height=2)
t.pack()

btn_show_msg = tk.Button(window, text="show_msg", width=50, height=5, command=show_msg_box)
btn_show_msg.pack()


window .mainloop()