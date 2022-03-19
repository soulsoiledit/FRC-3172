import wpilib
import commands2
import commands2.button
import constants

from subsystems.drive import DriveSubsystem
from subsystems.grabber import GrabberSubsystem
from subsystems.shooter import ShooterSubsystem
from subsystems.reacher import ReacherSubsystem
from subsystems.puller import PullerSubsystem

from commands.manualdrive import ManualDrive
from commands.reduceddrive import ReducedDrive
from commands.grab import Grab
from commands.shoot import MediumShoot
from commands.shoot import NukeEm
from commands.movearms import MoveArms
from commands.movewheels import ForwardWheel
from commands.movewheels import BackwardWheel
from commands.autonomous.sequence import AutoSequence


class RobotContainer:
    def __init__(self) -> None:
        # The driver's controller
        self.xboxController = wpilib.XboxController(constants.kXboxControllerPort)

        # subsystems
        self.drive = DriveSubsystem()
        self.shooter = ShooterSubsystem()
        self.grabber = GrabberSubsystem()
        self.extender = ReacherSubsystem()
        self.puller = PullerSubsystem()

        self.autoSpeed = wpilib.Preferences.getFloat("autoSpeed")
        self.autoTime = wpilib.Preferences.getFloat("autoTime")
        self.autoDrive = AutoSequence(self.drive, self.shooter)

        self.configureButtonBindings()

        # default drive command
        self.drive.setDefaultCommand(
            ManualDrive(
                self.drive,
                lambda: self.xboxController.getLeftY(),
                lambda: self.xboxController.getLeftX(),
            )
        )

        self.extender.setDefaultCommand(
            MoveArms(
                self.extender,
                lambda: self.xboxController.getLeftTriggerAxis(),
                lambda: self.xboxController.getRightTriggerAxis()    
            )
        )

    def configureButtonBindings(self):
        commands2.button.JoystickButton(self.xboxController, 9).whenHeld(
            ReducedDrive(self.drive)
        )

        # A
        commands2.button.JoystickButton(self.xboxController, 1).whenHeld(
            MediumShoot(self.shooter)
        )

        # B
        commands2.button.JoystickButton(self.xboxController, 2).whenHeld(
            NukeEm(self.shooter)
        )

        # X
        commands2.button.JoystickButton(self.xboxController, 3).whenHeld(
            Grab(self.grabber)
        )

        # left bumper
        commands2.button.JoystickButton(self.xboxController, 5).whenHeld(
            ForwardWheel(self.puller)
        )

        # right bumper
        commands2.button.JoystickButton(self.xboxController, 6).whenHeld(
            BackwardWheel(self.puller)
        )

    def getAutonomousCommand(self) -> commands2.Command:
        return self.autoDrive
