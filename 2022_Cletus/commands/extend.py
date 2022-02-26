import commands2
from subsystems.extender import ExtendSubsystem


class Extend(commands2.CommandBase):
    def __init__(self, extend: ExtendSubsystem) -> None:
        super().__init__()
        self.extend = extend
        self.addRequirements(extend)

    def initialize(self) -> None:
        self.extend.extend()

    def end(self, interrupted: bool) -> None:
        self.extend.stop()
