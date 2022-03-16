import commands2
import constants
from subsystems.shooter import ShooterSubsystem


class MediumShoot(commands2.CommandBase):
    def __init__(self, shooter: ShooterSubsystem) -> None:
        super().__init__()
        self.shooter = shooter
        self.addRequirements(shooter)

    def initialize(self) -> None:
        self.shooter.shoot(-0.5*constants.shootPower)

    def end(self, interrupted: bool) -> None:
        self.shooter.stop()

class NukeEm(commands2.CommandBase):
    def __init__(self, shooter: ShooterSubsystem) -> None:
        super().__init__()
        self.shooter = shooter
        self.addRequirements(shooter)

    def initialize(self) -> None:
        self.shooter.shoot(-1*constants.shootPower)

    def end(self, interrupted: bool) -> None:
        self.shooter.stop()
