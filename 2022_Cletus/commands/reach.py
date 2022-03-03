import commands2
from subsystems.extender import ExtenderSubsystem
from subsystems.puller import PullerSubsystem


class Reach(commands2.CommandBase):
    def __init__(self, extend: ExtenderSubsystem, pull: PullerSubsystem) -> None:
        super().__init__()
        self.extend = extend
        self.pull = pull
        self.addRequirements(extend)
        self.addRequirements(pull)

    def initialize(self) -> None:
        self.extend.extend()
        self.pull.unpull()

    def end(self, interrupted: bool) -> None:
        self.extend.stop()
        self.pull.stop()