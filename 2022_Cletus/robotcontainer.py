import constants
import wpilib

import commands2
import commands2.button

from subsystems.drive import DriveSubsystem
from subsystems.shooter import ShooterSubsystem
from subsystems.grabber import GrabberSubsystem

from commands.manualdrive import ManualDrive
from commands.reduceddrive import ReducedDrive
from commands.shoot import MediumShoot
from commands.nuke_em import NukeEm
from commands.grab import Grab


class RobotContainer:
    def __init__(self) -> None:

        # The driver's controller
        self.xboxController = wpilib.XboxController(constants.kXboxControllerPort)

        # subsystems
        self.drive = DriveSubsystem()
        self.shooter = ShooterSubsystem()
        self.grabber = GrabberSubsystem()

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
        commands2.button.JoystickButton(self.xboxController, 5).whenHeld(
            ReducedDrive(self.drive)
        )

        commands2.button.JoystickButton(self.xboxController, 1).whenPressed(
            MediumShoot(self.shooter)
        )

        commands2.button.JoystickButton(self.xboxController, 2).whenPressed(
            NukeEm(self.shooter)
        )

        commands2.button.JoystickButton(self.xboxController, 3).whenPressed(
            Grab(self.grabber)
        )

    def getAutonomousCommand(self) -> commands2.Command:
        pass
