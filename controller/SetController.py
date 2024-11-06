
class SetController:
    def __init__(self,flag):
        self.flag = flag

    def get_argv(self,arg):
        if  len(arg) > 1:
            if arg[1] == "help" or arg[1] == "?" :
                self.__set_helper()
            elif arg[1] == "mode":
                if arg[2] == "dev":
                    self.flag.set_flag(1)
        else:
            self.__set_helper()

    def __set_helper(self):
        print("""

[*] Set Helper

[^] [ ? , help ]  ->   Help
[^] mode          ->   In this section, we can change the desired modes
[^] option        ->   comming soon ...

""")