import commands2

from subsystems.shooter import ShooterSubsystem

class AutoShoot(commands2.CommandBase):
    def __init__(self, shoot: ShooterSubsystem, power: float) -> None:
        super().__init__()
        self.shoot = shoot
        self.addRequirements(shoot)

        self.power = power

    def initialize(self) -> None:
        self.shoot.shoot(self.power)

    def execute(self) -> None:
        self.shoot.shoot(self.power)

    def end(self, interrupted: bool) -> None:
        self.shoot.shoot(0)