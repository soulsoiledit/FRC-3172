import commands2
import constants

import wpilib


class ShooterSubsystem(commands2.SubsystemBase):
    def __init__(self) -> None:
        super().__init__()

        self.shooterMotor = wpilib.PWMSparkMax(constants.kShooterPort)

    def shoot(self, force: float) -> None:
        self.shooterMotor.set(force)

    def stop(self) -> None:
        self.shooterMotor.set(0)
