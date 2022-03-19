import commands2
import wpilib
import constants
from subsystems.shooter import ShooterSubsystem


class MediumShoot(commands2.CommandBase):
    def __init__(self, shooter: ShooterSubsystem) -> None:
        super().__init__()
        self.shooter = shooter
        self.addRequirements(shooter)

    def initialize(self) -> None:
        speed = -0.05
        time = wpilib.Timer.get()
        while (wpilib.Timer.get()-time) < 0.75 or speed == -0.5:
            speed -= 0.005
        self.shooter.shoot(-0.5)

    def end(self, interrupted: bool) -> None:
        self.shooter.stop()

class NukeEm(commands2.CommandBase):
    def __init__(self, shooter: ShooterSubsystem) -> None:
        super().__init__()
        self.shooter = shooter
        self.addRequirements(shooter)

    def initialize(self) -> None:
        speed = -0.05
        time = wpilib.Timer.get()
        while (wpilib.Timer.get()-time) < 0.75 or speed == -0.5:
            speed -= 0.005
        self.shooter.shoot(-1)

    def end(self, interrupted: bool) -> None:
        self.shooter.stop()
