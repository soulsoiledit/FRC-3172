import commands2
from subsystems.drive import DriveSubsystem


class ReducedDrive(commands2.CommandBase):
    def __init__(self, drive: DriveSubsystem) -> None:
        super().__init__()

        self.drive = drive

    def initialize(self) -> None:
        self.drive.setMaxOutput(0.5)

    def end(self, interrupted: bool) -> None:
        self.drive.setMaxOutput(1.0)
