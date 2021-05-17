import pymem
import subprocess

try:
    mem = pymem.Pymem("notepad.exe") ### reads memory of notepad.exe
except:
    subprocess.Popen("notepad.exe")
    mem = pymem.Pymem("notepad.exe")

mem.inject_python_interpreter() ### injects the python interpreter to be able to understand python code

### code which we will be injecting
code = """ 
import tkinter as tk

win = tk.Tk()
win.mainloop()
"""

mem.inject_python_shellcode(code) ### injecting the code
