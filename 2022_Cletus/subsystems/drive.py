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
        self.left_drive = wpilib.MotorControllerGroup(self.front_left, self.back_left)
        self.left_drive.setInverted(True)

        self.drive = wpilib.drive.DifferentialDrive(self.right_drive, self.left_drive)

        self.gyro = wpilib.ADXRS450_Gyro()
        self.gyro.reset()
        self.gyro.calibrate()

    def arcadeDrive(self, fwd: float, rot: float) -> None:
        driveFwdPower = wpilib.Preferences.getFloat("driveFwdPower")
        driveRotPower = wpilib.Preferences.getFloat("driveRotPower")
        self.drive.arcadeDrive(fwd*driveFwdPower, rot*driveRotPower)

    def driveStraight(self, fwd: float) -> None:
        self.drive.arcadeDrive(fwd, -self.gyro.getAngle()/8)

    def setMaxOutput(self, maxOutput: float):
        self.drive.setMaxOutput(maxOutput)
