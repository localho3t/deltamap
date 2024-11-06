from utils.banner.v1 import BannerV1
from utils.os_c.OSCheck import OSCheck
from utils.cmd.BasicCommand import BasicCommand
import os
from utils.flags.basicFlag import BasicFlag

def main():
    if oos.get_os() == "windows":
        os.system('cls')
    else:
        os.system('clear')
       
    print(bnrv1.show())
    print(f"[OS] {oos.get_os()}")
    
    # اجرای cmd_controller فقط در صورتی که cmd مقداردهی شده باشد
    if cmd:
        cmd.cmd_controller()
    else:
        print("Error: cmd is not initialized.")

if __name__ == "__main__":
    bnrv1 = BannerV1()
    oos = OSCheck()
    shared_flag = BasicFlag()
    cmd = BasicCommand(shared_flag)
    main()
