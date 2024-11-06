from utils.cmd.HelpCommand import HelpCommand
from utils.os_c.OSCheck import OSCheck
import os
from controller.SetController import SetController

class BasicCommand:
    def __init__(self, flag):
        self.flag = flag
        self.hc = HelpCommand()
        self.basic_commands = [
            "clear",
            "set", # set mode X
            "bye",
            "help",
            "get", # get time , get name , get os 
            "dl" ,
        ]
        self.dev_commands = [
            "add",
            "rcsv",
            "manage",
            "help",
            "exmod"
        ]
        self.oos = OSCheck()
        self.setCtrl = SetController(flag)


    
    
    def cmd_controller(self):
        try:
            while True:
                if self.flag.get_flag() == 0:
                    cmd = input("[home] >> ")
                elif self.flag.get_flag() == 1:
                    cmd = input("[dev] >> ")
                
                self.__cmd_manager(cmd.split(" "))

        except KeyboardInterrupt:
            print("client Exit")


    def __cmd_manager(self,arg):
        if self.flag.get_flag() == 0 :
            if arg[0] in self.basic_commands:
                if arg[0] == "help":
                    if len(arg) == 1:
                        self.hc.basic_method()
                elif arg[0] == "bye":
                    print("client Exit")
                    exit()
                elif arg[0] == "clear":
                    if self.oos.get_os() == "windows":
                        os.system('cls')
                    else:
                        os.system('clear')
                elif arg[0] == "set":
                    self.setCtrl.get_argv(arg)
            
            else :
                print(f"[command {arg[0]} not found]")
        elif self.flag.get_flag() == 1:
            if arg[0] in self.dev_commands:
                if arg[0] == "exmod":
                    self.flag.set_flag(0)