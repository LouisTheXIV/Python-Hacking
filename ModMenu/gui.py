from tkinter import *
from pymem import *
from pymem.process import *
from settings import *


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
        self.win.title(window_title)
        self.win.geometry(f"{width}x{height}")
        self.win.wm_overrideredirect(True)
        self.win.wm_attributes("-topmost", 1)
        self.win.wm_attributes("-alpha", 0.7)
        self.win.configure(background=BG)

        self.title_label = Label(self.win, text=window_title, font=('Arial',12), bg=BG, fg=FG)
        self.title_label.pack()

        self.ammo_btn = Button(self.win, text="Ammo Hack", font=('Arial',12), bg=BG, fg=FG, command=self.ammo_hack)
        self.ammo_btn.pack()

        self.close_btn = Button(self.win, text="Close", font=('Arial',12), bg=BG, fg=FG, command=self.win.destroy)
        self.close_btn.pack()

    def ammo_hack(self):
        mem.write_int(getPointerAddr(module + 0x0011E20C, ammo_offsets), 1000)



modmenu = ModMenu("Assault Cube Modmenu", 350, 200)
modmenu.win.mainloop()
