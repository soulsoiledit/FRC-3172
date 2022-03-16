import commands2
import constants

import wpilib
import wpilib.drive


class DriveSubsystem(commands2.SubsystemBase):
    def __init__(self) -> None:
        super().__init__()

        self.front_right = wpilib.Talon(constants.kDriveFrontRightPort)
        self.back_right = wpilib.Talon(constants.kDriveBackRightPort)
        self.right_drive = wpilib.MotorControllerGroup(self.front_right, self.back_right)

        self.front_left = wpilib.Talon(constants.kDriveFrontLeftPort)
        self.back_left = wpilib.Talon(constants.kDriveBackLeftPort)
        self.back_left.setInverted(True)
        self.left_drive = wpilib.MotorControllerGroup(self.front_left, self.back_left)

        self.drive = wpilib.drive.DifferentialDrive(self.right_drive, self.left_drive)

    def curvatureDrive(self, fwd: float, rot: float) -> None:
        print(fwd, rot)
        self.drive.arcadeDrive(fwd*constants.driveFwdPower, rot*constants.driveRotPower)

    def setMaxOutput(self, maxOutput: float):
        self.drive.setMaxOutput(maxOutput)
