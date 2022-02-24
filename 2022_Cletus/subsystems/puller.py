import commands2
import constants

import wpilib

class PullerSubsystem(commands2.SubsystemBase):
    def __init__(self) -> None:
        super().__init__()

        self.pullerMotor0 = wpilib.PWMSparkMax(constants.kPullerPort0)
        self.pullerMotor1 = wpilib.PWMSparkMax(constants.kPullerPort1)

        self.pullerMotors = wpilib.MotorControllerGroup(self.pullerMotor0, self.pullerMotor1)

    def pull(self) -> None:
        self.pullerMotors.set(0.9)

    def stop(self) -> None:
        self.pullerMotors.set(0)
