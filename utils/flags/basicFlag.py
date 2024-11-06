

class BasicFlag:
    
    def __init__(self):
        self.value = 0

    def set_flag(self, new_value):
        self.value = new_value

    def get_flag(self):
        return self.value