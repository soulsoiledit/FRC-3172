import commands2
import typing
from subsystems.reacher import ReacherSubsystem


class MoveArms(commands2.CommandBase):
    def __init__(
        self, extend: ReacherSubsystem, 
        leftSpeed:  typing.Callable[[], float], 
        rightSpeed:  typing.Callable[[], float]
    ) -> None:
        super().__init__()

        self.extend = extend
        self.left = leftSpeed
        self.right = rightSpeed
        self.addRequirements(extend)

    def execute(self) -> None:
        self.extend.move(self.left(), self.right())