from tkinter import *
from pymem import *
from pymem.process import *
from settings import *
import keyboard as kb
from threading import Thread
from time import sleep

mem = Pymem("ac_client.exe")
module = module_from_name(mem.process_handle, "ac_client.exe").lpBaseOfDll
ammo_offsets = [0x598, 0x410, 0x434, 0x3C8, 0xC]

def getPointerAddr(base, offsets):
    addr = mem.read_int(base)
    for offset in offsets:
        if offset != offsets[-1]:
            addr = mem.read_int(addr + offset)
    addr = addr + offsets[-1]
    return addr

class ModMenu():
    def __init__(self, window_title, width, height):
        self.win = Tk()
        x, y = self.center(width, height)
        self.win.geometry(f"{width}x{height}+{x}+{y}")
        self.win.overrideredirect(True)
        self.win.wm_attributes("-topmost", 1)
        self.win.wm_attributes("-alpha", 0.7)
        self.win.configure(background=BG)

        self.title_label = Label(self.win, text=window_title, font=('Arial',12), bg=BG, fg=FG)
        self.title_label.pack()

        self.ammo_btn = Button(self.win, text="Ammo Hack", font=('Arial',14), bg=BG, fg=FG, command=self.ammo_hack)
        self.ammo_btn.pack()

        self.exit_btn = Button(self.win, text="Exit", font=('Arial',14), bg=BG, fg=FG, command=self.win.destroy)
        self.exit_btn.place(x=160, y=150)

    def ammo_hack(self):
        mem.write_int(getPointerAddr(module + 0x0011E20C, ammo_offsets), 1000)

    def center(self, width, height):
        swidth = self.win.winfo_screenwidth()
        sheight = self.win.winfo_screenheight()
        x = (swidth/2) - (width/2)
        y = (sheight/2) - (height/2)
        return int(x), int(y)



def keybinds(modmenu):
    isopen = True
    while True:
        if kb.is_pressed(OPEN):
            if isopen == True:
                modmenu.win.withdraw()
                isopen = False
            else:
                modmenu.win.deiconify()
                isopen = True
                modmenu.win.focus_force()
            sleep(0.5)






modmenu = ModMenu("Assault Cube Hack", 350, 200)

keybinds_thread = Thread(target=keybinds, args=(modmenu,))
keybinds_thread.setDaemon(True)
keybinds_thread.start()

modmenu.win.mainloop()
