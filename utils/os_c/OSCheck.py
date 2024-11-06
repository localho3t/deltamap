import os
import platform



class OSCheck:
    def get_os(self):
        return str(platform.platform()).split('-')[0].lower()