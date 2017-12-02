class tile:
    def __init__(self):
        self.value = 0
        self.joined = False

    def __del__(self):
        self.value = None
        self.joined = None

    def join(self):
        self.value *= 2
        self.joined = True

    def merge(self):
        self.value = 0

    def next_turn(self):
        self.joined = False

    def place(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def is_joined(self):
        return self.joined
