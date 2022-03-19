import commands2
import constants
import rev

import wpilib


class GrabberSubsystem(commands2.SubsystemBase):
    def __init__(self) -> None:
        super().__init__()

        self.grabberMotor = rev.CANSparkMax(constants.kGrabberPortID, rev.CANSparkMaxLowLevel.MotorType(0))

    def grab(self) -> None:
        grabPower = wpilib.Preferences.getFloat("grabPower")
        self.grabberMotor.set(grabPower)

    def stop(self) -> None:
        self.grabberMotor.set(0)
