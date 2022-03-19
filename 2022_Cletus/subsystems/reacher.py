import commands2
import constants

import wpilib


class ReacherSubsystem(commands2.SubsystemBase):
    def __init__(self) -> None:
        super().__init__()

        self.leftReachMotor = wpilib.Spark(constants.kLeftReachPort)
        self.rightReachMotor = wpilib.Spark(constants.kRightExtendPort)

        self.extendMotors = wpilib.MotorControllerGroup(self.leftReachMotor, self.rightReachMotor)

    def move(self, leftSpeed: float, rightSpeed: float) -> None:
        self.extendMotors.set((leftSpeed-rightSpeed)*constants.reachPower)
