import typing

import commands2
import wpilib
import constants

from robotcontainer import RobotContainer


class Cletus(commands2.TimedCommandRobot):
    autoCommand: typing.Optional[commands2.Command] = None

    def robotInit(self) -> None:
        self.container = RobotContainer()

        if not wpilib.Preferences.containsKey("driveFwdPower"):
            wpilib.Preferences.setFloat("driveFwdPower", constants.kDefDriveRotPower)

        if not wpilib.Preferences.containsKey("driveRotPower"):
            wpilib.Preferences.setFloat("driveRotPower", constants.kDefDriveFwdPower)

        if not wpilib.Preferences.containsKey("shootPower"):
            wpilib.Preferences.setFloat("shootPower", constants.kDefShootPower)

        if not wpilib.Preferences.containsKey("grabPower"):
            wpilib.Preferences.setFloat("grabPower", constants.kDefGrabPower)

        if not wpilib.Preferences.containsKey("reachPower"):
            wpilib.Preferences.setFloat("reachPower", constants.kDefReachPower)

        if not wpilib.Preferences.containsKey("pullPower"):
            wpilib.Preferences.setFloat("pullPower", constants.kDefPullPower)

        if not wpilib.Preferences.containsKey("autoSpeed"):
            wpilib.Preferences.setFloat("autoSpeed", constants.kDefAutoSpeed)

        if not wpilib.Preferences.containsKey("autoTime"):
            wpilib.Preferences.setFloat("autoTime", constants.kDefAutoTime)

    def disabledInit(self) -> None:
        """This function is called once each time the robot enters Disabled mode."""

    def disabledPeriodic(self) -> None:
        """This function is called periodically when disabled"""

    def autonomousInit(self) -> None:
        """This autonomous runs the autonomous command selected by your RobotContainer class."""
        self.autoCommand = self.container.getAutonomousCommand()

        if self.autoCommand:
            print("gotAuto")
            self.autoCommand.schedule()

    def autonomousPeriodic(self) -> None:
        """This function is called periodically during autonomous"""

    def teleopInit(self) -> None:
        # if you want auto to continue until manual, remove this
        if self.autoCommand:
            self.autoCommand.cancel()

    def teleopPeriodic(self) -> None:
        """This function is called periodically during operator control"""

    def testInit(self) -> None:
        # Cancels all running commands at the start of test mode
        commands2.CommandScheduler.getInstance().cancelAll()


if __name__ == "__main__":
    wpilib.run(Cletus)
