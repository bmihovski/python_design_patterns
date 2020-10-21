class Computer:
    def __init__(self, serial_number: str) -> None:
        self.serial = serial_number
        self.memory = None  # in gb
        self.hdd = None  # in gb
        self.gpu = None

    def __str__(self) -> str:
        info = (f"Memory: {self.memory}")