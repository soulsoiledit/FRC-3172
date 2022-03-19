import commands2
import constants
import rev

import wpilib


class ShooterSubsystem(commands2.SubsystemBase):
    def __init__(self) -> None:
        super().__init__()

        self.leftShooterMotor = rev.CANSparkMax(constants.kLeftShooterPortID, rev.CANSparkMaxLowLevel.MotorType(0))
        self.rightShooterMotor = rev.CANSparkMax(constants.kRightShooterPortID, rev.CANSparkMaxLowLevel.MotorType(0))
        self.rightShooterMotor.setInverted(False)

        self.shooterMotors = wpilib.MotorControllerGroup(self.leftShooterMotor, self.rightShooterMotor)

    def shoot(self, force: float) -> None:
        shootPower = wpilib.Preferences.getFloat("shootPower")
        self.shooterMotors.set(force*shootPower)

    def stop(self) -> None:
        self.shooterMotors.set(0)
