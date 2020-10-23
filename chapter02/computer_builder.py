import builtins


class Computer:
    def __init__(self) -> None:
        self.serial = None
        self.memory = None  # in gb
        self.hdd = None  # in gb
        self.gpu = None

    def __str__(self) -> str:
        info = (f"Serial Number: {self.serial}",
                f"Memory: {self.memory}GB",
                f"Hard Disk: {self.hdd}GB",
                f"Graphics Card: {self.gpu}")

        return "\n".join(info)


class Tablet:
    def __init__(self) -> None:
        self.screen = None
        self.memory = None
        self.cpu = None

    def __str__(self) -> str:
        tablet_info = (f"Screen: {self.screen} Inches",
                       f"Memory: {self.memory} GB",
                       f"CPU : {self.cpu} GHz")
        return "\n".join(tablet_info)


class ComputerBuilder:
    def __init__(self) -> None:
        self.computer = Computer()

    def configure_serial(self, serial):
        self.computer.serial = serial

    def configure_memory(self, amount):
        self.computer.memory = amount

    def configure_hdd(self, amount):
        self.computer.hdd = amount

    def configure_gpu(self, gpu_model):
        self.computer.gpu = gpu_model


class TabletBuilder:
    def __init__(self) -> None:
        self.tablet = Tablet()

    def configure_screen(self, size):
        self.tablet.screen = size

    def configure_memory(self, amount):
        self.tablet.memory = amount

    def configure_cpu(self, type):
        self.tablet.cpu = type


class HardwareEngineer:
    def __init__(self) -> None:
        self.builder = None

    def construct_computer(self, serial, memory, hdd, gpu):
        self.builder = ComputerBuilder()
        steps = (self.builder.configure_serial(serial),
                 self.builder.configure_memory(memory),
                 self.builder.configure_hdd(hdd),
                 self.builder.configure_gpu(gpu))
        [step for step in steps]

    @property
    def computer(self):
        return self.builder.computer

    def construct_tablet(self, screen, memory, cpu):
        self.builder = TabletBuilder()
        tablet_steps = (self.builder.configure_screen(screen),
                        self.builder.configure_memory(memory),
                        self.builder.configure_cpu(cpu))
        [step for step in tablet_steps]

    @property
    def tablet(self):
        return self.builder.tablet


def main():
    engineer = HardwareEngineer()
    engineer.construct_computer(serial="KB4343", memory=512, hdd=250, gpu="Tegra")
    computer = engineer.computer
    print(computer)
    engineer.construct_tablet(screen=9, memory=2, cpu="Qualcomm")
    tablet = engineer.tablet
    print(tablet)


if __name__ == "__main__":
    main()
