import commands2
import wpilib
import constants
from subsystems.shooter import ShooterSubsystem

class WeakShoot(commands2.CommandBase):
    def __init__(self, shooter: ShooterSubsystem) -> None:
        super().__init__()
        self.shooter = shooter
        self.addRequirements(shooter)

    def initialize(self) -> None:
        self.shooter.shoot(-0.5)

    def end(self, interrupted: bool) -> None:
        self.shooter.stop()

class StrongShoot(commands2.CommandBase):
    def __init__(self, shooter: ShooterSubsystem) -> None:
        super().__init__()
        self.shooter = shooter
        self.addRequirements(shooter)

    def initialize(self) -> None:
        self.shooter.shoot(-1)

    def end(self, interrupted: bool) -> None:
        self.shooter.stop()
