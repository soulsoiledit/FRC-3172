import commands2
import wpilib

from subsystems.drive import DriveSubsystem


class AutoDriveTime(commands2.CommandBase):
    def __init__(self, drive: DriveSubsystem, speed: float, elapsedTime: float) -> None:
        super().__init__()
        self.drive = drive

        self.timer = wpilib.Timer()
        self.timer.start()

        self.startTime = self.timer.get()
        self.elapsedTime =  elapsedTime

        self.speed = speed

        self.addRequirements(drive)

    def initialize(self) -> None:
        self.drive.arcadeDrive(self.speed, 0)

    def execute(self) -> None:
        self.drive.arcadeDrive(self.speed, 0)

    def end(self, interrupted: bool) -> None:
        self.drive.arcadeDrive(0, 0)

    def isFinished(self) -> bool:
        return (self.timer.get() - self.startTime) >= self.elapsedTime