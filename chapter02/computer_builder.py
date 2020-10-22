class Computer:
    def __init__(self, serial_number: str) -> None:
        self.serial = serial_number
        self.memory = None  # in gb
        self.hdd = None  # in gb
        self.gpu = None

    def __str__(self) -> str:
        info = (f"Memory: {self.memory}GB",
                f"Hard Disk: {self.hdd}GB",
                f"Graphics Card: {self.gpu}")

        return "\n".join(info)


class ComputerBuilder:
    def __init__(self) -> None:
        self.computer = Computer("Ader33434")

    def configure_memory(self, amount):
        self.computer.memory = amount

    def configure_hdd(self, amount):
        self.computer.hdd = amount

    def configure_gpu(self, gpu_model):
        self.computer.gpu = gpu_model


class HardwareEngineer:
    def __init__(self) -> None:
        self.builder = None

    def construct_computer(self, memory, hdd, gpu):
        self.builder = ComputerBuilder()
        steps = (self.builder.configure_memory(memory),
                 self.builder.configure_hdd(hdd),
                 self.builder.configure_gpu(gpu))
        [step for step in steps]

    @property
    def computer(self):
        return self.builder.computer


def main():
    engineer = HardwareEngineer()
    engineer.construct_computer(memory=512, hdd=250, gpu="Tegra")
    computer = engineer.computer
    print(computer)


if __name__ == "__main__":
    main()
