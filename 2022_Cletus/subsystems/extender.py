import commands2
import constants

import wpilib


class ExtenderSubsystem(commands2.SubsystemBase):
    def __init__(self) -> None:
        super().__init__()

        self.leftExtendMotor = wpilib.Spark(constants.kLeftExtendPort)
        self.rightExtendMotor = wpilib.Spark(constants.kRightExtendPort)

        self.extendMotors = wpilib.MotorControllerGroup(self.leftExtendMotor, self.rightExtendMotor)

    def extend(self) -> None:
        self.extendMotors.set(constants.extendPower)

    def contract(self) -> None:
        self.extendMotors.set(-constants.extendPower)

    def stop(self) -> None:
        self.extendMotors.set(0)
