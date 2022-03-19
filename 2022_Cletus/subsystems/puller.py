import commands2
import constants
import wpilib


class PullerSubsystem(commands2.SubsystemBase):
    def __init__(self) -> None:
        super().__init__()

        
        self.rightPullerMotor = wpilib.Spark(constants.kRightPullerPort)
        self.leftPullerMotor = wpilib.Spark(constants.kLeftPullerPort)
        self.leftPullerMotor.setInverted(True)

        self.pullerMotors = wpilib.MotorControllerGroup(self.rightPullerMotor, self.leftPullerMotor)

    def contract(self) -> None:
        pullPower = wpilib.Preferences.getFloat("pullPower")
        self.pullerMotors.set(pullPower)

    def extend(self) -> None:
        pullPower = wpilib.Preferences.getFloat("pullPower")
        self.pullerMotors.set(-pullPower)

    def stop(self) -> None:
        self.pullerMotors.set(0)
