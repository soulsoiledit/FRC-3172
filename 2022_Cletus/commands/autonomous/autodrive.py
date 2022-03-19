import commands2
import wpilib

from subsystems.drive import DriveSubsystem


class AutoDriveFW(commands2.CommandBase):
    def __init__(self, drive: DriveSubsystem, gyro: wpilib.ADXRS450_Gyro) -> None:
        super().__init__()
        self.drive = drive
        self.gyro = gyro
        self.autoSpeed = 0
        self.addRequirements(drive)
        

    def initialize(self) -> None:
        self.autoSpeed = wpilib.Preferences.getFloat("autoSpeed")
        self.drive.arcadeDrive(-self.autoSpeed*2, 0)

    def execute(self) -> None:
        error = -self.gyro.getAngle()
        turnPower = 0.5 * error

        self.drive.arcadeDrive(-self.autoSpeed*2, turnPower)

    def end(self, interrupted: bool) -> None:
        self.drive.arcadeDrive(0, 0)

class AutoDriveBW(commands2.CommandBase):
    def __init__(self, drive: DriveSubsystem, gyro: wpilib.ADXRS450_Gyro) -> None:
        super().__init__()
        self.drive = drive
        self.gyro = gyro
        self.autoSpeed = 0
        self.addRequirements(drive)

    def initialize(self) -> None:
        self.autoSpeed = wpilib.Preferences.getFloat("autoSpeed")
        self.drive.arcadeDrive(self.autoSpeed, 0)

    def execute(self) -> None:
        error = -self.gyro.getAngle()
        turnPower = 0.5 * error

        self.drive.arcadeDrive(self.autoSpeed, turnPower)

    def end(self, interrupted: bool) -> None:
        self.drive.arcadeDrive(0, 0)