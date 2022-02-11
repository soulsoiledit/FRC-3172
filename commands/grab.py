import commands2
from subsystems.grabber import  GrabberSubsystem


class Grab(commands2.CommandBase):
    def __init__(self, grabber: GrabberSubsystem) -> None:
        super().__init__()
        self.grabber = grabber
        self.addRequirements(grabber)

    def initialize(self) -> None:
        self.grabber.grab()

    def end(self, interrupted: bool) -> None:
        self.grabber.stop()
