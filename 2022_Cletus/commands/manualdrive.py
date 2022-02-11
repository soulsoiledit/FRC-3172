import commands2
import typing
from subsystems.drive import DriveSubsystem


class ManualDrive(commands2.CommandBase):
    def __init__(
            self, drive: DriveSubsystem,
            fwd: typing.Callable[[], float],
            rot: typing.Callable[[], float]
    ) -> None:
        super().__init__()

        self.drive = drive
        self.forward = fwd
        self.rotation = rot

        self.addRequirements([self.drive])

    def execute(self) -> None:
        self.drive.curvatureDrive(self.forward(), self.rotation())
