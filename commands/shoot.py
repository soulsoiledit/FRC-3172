import commands2
from subsystems.shooter import ShooterSubsystem


class MediumShoot(commands2.CommandBase):
    def __init__(self, shooter: ShooterSubsystem) -> None:
        super().__init__()
        self.shooter = shooter
        self.addRequirements(shooter)

    def initialize(self) -> None:
        self.shooter.shoot(0.5)

    def end(self, interrupted: bool) -> None:
        self.shooter.stop()
