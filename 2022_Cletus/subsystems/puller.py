import commands2
import constants
import rev
import wpilib


class PullerSubsystem(commands2.SubsystemBase):
    def __init__(self) -> None:
        super().__init__()

        self.pullerMotor0 = rev.CANSparkMax(constants.kPullerID0, rev.CANSparkMaxLowLevel.MotorType(0))
        self.pullerMotor1 = rev.CANSparkMax(constants.kPullerID1, rev.CANSparkMaxLowLevel.MotorType(0))

        self.pullerMotors = wpilib.MotorControllerGroup(self.pullerMotor0, self.pullerMotor1)

    def pull(self) -> None:
        self.pullerMotors.set(0.8)

    def unpull(self) -> None:
        self.pullerMotors.set(-0.8)

    def stop(self) -> None:
        self.pullerMotors.set(0)
