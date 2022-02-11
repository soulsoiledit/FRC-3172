import wpilib
import typing
import commands2

from robotcontainer import RobotContainer


class Cletus(commands2.TimedCommandRobot):
    autoCommand: typing.Optional[commands2.Command] = None

    def robotInit(self) -> None:
        self.container = RobotContainer()

    def disabledInit(self) -> None:
        """This function is called once each time the robot enters Disabled mode."""

    def disabledPeriodic(self) -> None:
        """This function is called periodically when disabled"""

    def autonomousInit(self) -> None:
        """This autonomous runs the autonomous command selected by your RobotContainer class."""
        self.autoCommand = self.container.getAutonomousCommand()

        if self.autoCommand:
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
