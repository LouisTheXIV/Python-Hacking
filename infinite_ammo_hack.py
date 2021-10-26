from pymem import *
from pymem.process import *


mem = Pymem("ac_client.exe")
game_module = module_from_name(mem.process_handle, "ac_client.exe").lpBaseOfDll


def getPtrAddr(address, offsets):
    addr = mem.read_int(address)
    for offset in offsets:
        if offset != offsets[-1]:
            addr = mem.read_int(addr + offset)
    addr = addr + offsets[-1]
    return addr

while True:
    mem.write_int(getPtrAddr(game_module + 0x0011E20C, [0x520, 0x568, 0x1E8, 0x3F0, 0x4E0]), 1000)
