import commands2
import wpilib

from subsystems.drive import DriveSubsystem


class AutoDriveFW(commands2.CommandBase):
    def __init__(self, drive: DriveSubsystem) -> None:
        super().__init__()
        self.drive = drive
        self.addRequirements(drive)

    def initialize(self) -> None:
        self.drive.gyro.reset()
        self.drive.driveStraight(-wpilib.Preferences.getFloat("driveFwdPower")*1.1)

    def execute(self) -> None:
        self.drive.driveStraight(-wpilib.Preferences.getFloat("driveFwdPower")*1.1)

    def end(self, interrupted: bool) -> None:
        self.drive.driveStraight(0)

class AutoDriveBW(commands2.CommandBase):
    def __init__(self, drive: DriveSubsystem) -> None:
        super().__init__()
        self.drive = drive
        self.addRequirements(drive)

    def initialize(self) -> None:
        self.drive.gyro.reset()
        self.drive.driveStraight(wpilib.Preferences.getFloat("autoSpeed"))

    def execute(self) -> None:
        self.drive.driveStraight(wpilib.Preferences.getFloat("autoSpeed"))

    def end(self, interrupted: bool) -> None:
        self.drive.driveStraight(0)