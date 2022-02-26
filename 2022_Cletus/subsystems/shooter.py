import commands2
import constants

import wpilib


class ShooterSubsystem(commands2.SubsystemBase):
    def __init__(self) -> None:
        super().__init__()

        self.shooterMotor0 = wpilib.Talon(constants.kShooterPort0)
        self.shooterMotor1 = wpilib.Talon(constants.kShooterPort1)
        self.shooterMotor1.setInverted()

        self.shooterMotors = wpilib.MotorControllerGroup(self.shooterMotor0, self.shooterMotor1)

    def shoot(self, force: float) -> None:
        self.shooterMotors.set(force)

    def stop(self) -> None:
        self.shooterMotors.set(0)
