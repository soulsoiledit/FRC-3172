import commands2
from subsystems.puller import PullerSubsystem


class Pull(commands2.CommandBase):
    def __init__(self, puller: PullerSubsystem) -> None:
        super().__init__()
        self.puller = puller
        self.addRequirements(puller)

    def initialize(self) -> None:
        self.puller.pull()

    def end(self, interrupted: bool) -> None:
        self.puller.stop()
