class UnexpectedGameFinish(Exception):
    def __init__(self, str):
        self.str = str


class GameWin(Exception):
    def __init__(self, str):
        self.str = str
