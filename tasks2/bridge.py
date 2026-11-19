from abc import ABC, abstractmethod


class Device(ABC):
    def __init__(self):
        self.on = False
        self.volume = 30

    @abstractmethod
    def name(self) -> str: ...

    def set_volume(self, v):
        self.volume = max(0, min(100, v))


class TV(Device):
    def name(self):
        return "Televizor"


class Radio(Device):
    def name(self):
        return "Radio"


class RemoteControl:
    def __init__(self, device: Device):
        self.device = device

    def toggle_power(self):
        self.device.on = not self.device.on
        print(f"  {self.device.name()}: {'yoqildi' if self.device.on else 'o`chirildi'}")

    def volume_up(self):
        self.device.set_volume(self.device.volume + 10)
        print(f"  {self.device.name()} ovozi: {self.device.volume}")


class AdvancedRemote(RemoteControl):
    def mute(self):
        self.device.set_volume(0)
        print(f"  {self.device.name()}: ovoz o'chirildi")


if __name__ == "__main__":
    print("=== Bridge ===")
    for remote in (RemoteControl(TV()), AdvancedRemote(Radio())):
        remote.toggle_power()
        remote.volume_up()
        if isinstance(remote, AdvancedRemote):
            remote.mute()
