import commands2
from subsystems.puller import PullerSubsystem


class ForwardWheel(commands2.CommandBase):
    def __init__(self, pull: PullerSubsystem) -> None:
        super().__init__()
        self.pull = pull
        self.addRequirements(pull)

    def initialize(self) -> None:
        self.pull.extend()

    def end(self, interrupted: bool) -> None:
        self.pull.stop()

class BackwardWheel(commands2.CommandBase):
    def __init__(self, pull: PullerSubsystem) -> None:
        super().__init__()
        self.pull = pull
        self.addRequirements(pull)

    def initialize(self) -> None:
        self.pull.contract()

    def end(self, interrupted: bool) -> None:
        self.pull.stop()

