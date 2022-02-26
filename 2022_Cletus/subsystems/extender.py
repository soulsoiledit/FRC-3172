import commands2
import constants

import wpilib


class ExtenderSubsystem(commands2.SubsystemBase):
    def __init__(self) -> None:
        super().__init__()

        self.extendMotor0 = wpilib.Talon(constants.kExtendPort0)
        self.extendMotor1 = wpilib.Talon(constants.kExtendPort1)

        self.extendMotors = wpilib.MotorControllerGroup(self.extendMotor0, self.extendMotor1)

    def extend(self) -> None:
        self.extendMotors.set(0.9)

    def stop(self) -> None:
        self.extendMotors.set(0)
