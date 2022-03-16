import wpilib
import commands2
import commands2.button
import constants

from subsystems.drive import DriveSubsystem
from subsystems.grabber import GrabberSubsystem
from subsystems.shooter import ShooterSubsystem
from subsystems.extender import ExtenderSubsystem
from subsystems.puller import PullerSubsystem

from commands.manualdrive import ManualDrive
from commands.reduceddrive import ReducedDrive
from commands.grab import Grab
from commands.shoot import MediumShoot
from commands.shoot import NukeEm
from commands.reach import Reach
from commands.pull import Pull


class RobotContainer:
    def __init__(self) -> None:
        # The driver's controller
        self.xboxController = wpilib.XboxController(constants.kXboxControllerPort)

        # subsystems
        self.drive = DriveSubsystem()
        self.shooter = ShooterSubsystem()
        self.grabber = GrabberSubsystem()
        self.extender = ExtenderSubsystem()
        self.puller = PullerSubsystem()

        self.configureButtonBindings()

        # default drive command
        self.drive.setDefaultCommand(
            ManualDrive(
                self.drive,
                lambda: self.xboxController.getLeftY(),
                lambda: self.xboxController.getLeftX(),
            )
        )

    def configureButtonBindings(self):
        commands2.button.JoystickButton(self.xboxController, 9).whenHeld(
            ReducedDrive(self.drive)
        )

        commands2.button.JoystickButton(self.xboxController, 1).whenHeld(
            MediumShoot(self.shooter)
        )

        commands2.button.JoystickButton(self.xboxController, 2).whenHeld(
            NukeEm(self.shooter)
        )

        commands2.button.JoystickButton(self.xboxController, 3).whenHeld(
            Grab(self.grabber)
        )

        commands2.button.JoystickButton(self.xboxController, 5).whenHeld(
            Reach(self.extender, self.puller)
        )

        commands2.button.JoystickButton(self.xboxController, 6).whenHeld(
            Pull(self.extender, self.puller)
        )

    def getAutonomousCommand(self) -> commands2.Command:
        pass
