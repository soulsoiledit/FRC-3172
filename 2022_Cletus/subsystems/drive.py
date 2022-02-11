import commands2
import constants

import wpilib
import wpilib.drive


class DriveSubsystem(commands2.SubsystemBase):
    def __init__(self) -> None:
        super().__init__()

        self.front_left = wpilib.Spark(constants.kDriveFrontLeftPort)
        self.back_left = wpilib.Spark(constants.kDriveBackLeftPort)
        self.left_drive = wpilib.MotorControllerGroup(self.front_left, self.back_left)

        self.front_right = wpilib.Spark(constants.kDriveFrontRightPort)
        self.back_right = wpilib.Spark(constants.kDriveBackRightPort)
        self.right_drive = wpilib.MotorControllerGroup(self.front_right, self.back_right)

        self.drive = wpilib.drive.DifferentialDrive(self.left_drive, self.right_drive)

    def curvatureDrive(self, fwd: float, rot: float) -> None:
        """
        :param fwd: the forward movement command
        :param rot: the rotation command
        """
        self.drive.curvatureDrive(fwd, rot, allowTurnInPlace=True)

    def setMaxOutput(self, maxOutput: float):
        """
        :param maxOutput: maximum output of the drivetrain
        """
        self.drive.setMaxOutput(maxOutput)
