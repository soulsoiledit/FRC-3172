import commands2
import constants

import wpilib


class GrabberSubsystem(commands2.SubsystemBase):
    def __init__(self) -> None:
        super().__init__()

        self.grabberMotor = wpilib.Talon(constants.kGrabberPort)

    def grab(self) -> None:
        self.grabberMotor.set(0.5)

    def stop(self) -> None:
        self.grabberMotor.set(0)
