import commands2
import wpilib

from subsystems.drive import DriveSubsystem


class AutoDriveFW(commands2.CommandBase):
    def __init__(self, drive: DriveSubsystem) -> None:
        super().__init__()
        self.drive = drive
        self.autoSpeed = 0
        self.addRequirements(drive)

    def initialize(self) -> None:
        self.autoSpeed = wpilib.Preferences.getFloat("autoSpeed")
        self.drive.arcadeDrive(-self.autoSpeed, 0)

    def execute(self) -> None:
        self.drive.arcadeDrive(-self.autoSpeed, 0)

    def end(self, interrupted: bool) -> None:
        self.drive.arcadeDrive(0, 0)

class AutoDriveBW(commands2.CommandBase):
    def __init__(self, drive: DriveSubsystem) -> None:
        super().__init__()
        self.drive = drive
        self.autoSpeed = 0
        self.addRequirements(drive)

    def initialize(self) -> None:
        self.autoSpeed = wpilib.Preferences.getFloat("autoSpeed")
        self.drive.arcadeDrive(self.autoSpeed, 0)

    def execute(self) -> None:
        self.drive.arcadeDrive(self.autoSpeed, 0)

    def end(self, interrupted: bool) -> None:
        self.drive.arcadeDrive(0, 0)