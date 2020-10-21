MINI14 = "1.4 GHz Mac Mini"


class AppleFactory:
    class MacMini14:
        def __init__(self) -> None:
            self.memory = 4  # in gb
            self.hdd = 500  # in gb
            self.gpu = "Intel Graphics 5000 HD"

        def __str__(self) -> str:
            info = (f"Model: {MINI14}",
                    f"Memory: {self.memory} GB",
                    f"HDD: {self.hdd} GB",
                    f"Graphics Card: {self.gpu}")
            return "\n".join(info)

    def build_computer(self, model):
        if model == MINI14:
            return self.MacMini14()
        else:
            msg = f"I don't know how to build {model}"
            print(msg)


if __name__ == "__main__":
    afac = AppleFactory()
    mac_mini = afac.build_computer(MINI14)
    print(mac_mini)
